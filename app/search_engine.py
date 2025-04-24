import torch
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import pandas as pd
from utils import get_value, setup_logging
import logging

# Setup logging
setup_logging()
logger = logging.getLogger('search_engine')



class SemanticSearchEngine:
    def __init__(self, corpus_embeddings_path: str, analysis_df_path: str, package_descr_path: str, device: str = "cpu"):
        
        self.corpus_embeddings = torch.load(corpus_embeddings_path, map_location=torch.device(device))
        logger.info("Loaded embeddings.") 
        self.bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        self.bi_encoder.max_seq_length = 256
        self.cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        self.analysis_df = pd.read_csv(analysis_df_path)
        package_descr_df = pd.read_json(package_descr_path, dtype=str)
        package_descr_df.columns = ['package', 'logo', 'website', 'source', 'articles']
        package_descr_df = package_descr_df.map(lambda x: str(x)[2:-2])
        self.analysis_df = self.analysis_df.merge(package_descr_df, left_on='package_name', right_on='package', how='left')
        self.paragraphs = [str(s) for s in self.analysis_df['tokenized_content'].to_list()]
        self.window_size = 7
        self.passages = self._create_passages()
        self.device = torch.device(device)

    def _create_passages(self):
        passages = []
        for start_idx in range(0, len(self.paragraphs), self.window_size):
            end_idx = min(start_idx + self.window_size, len(self.paragraphs))
            passages.append(";".join(self.paragraphs[start_idx:end_idx]))
        return passages

    def search(self, query: str, top_k: int = 5, num_results: int = 5):
        try:
            # Get question embedding
            question_embedding = self.bi_encoder.encode(query, convert_to_tensor=True).to(self.device)
            
            # Ensure top_k doesn't exceed the number of available passages
            max_hits = min(top_k, len(self.passages))
            logger.info(f"Searching with max_hits: {max_hits}, total passages: {len(self.passages)}")
            
            # Get semantic search hits
            hits = util.semantic_search(question_embedding, self.corpus_embeddings, top_k=max_hits)[0]
            
            # Validate corpus_ids
            valid_hits = []
            for hit in hits:
                if 0 <= hit['corpus_id'] < len(self.passages):
                    valid_hits.append(hit)
                else:
                    logger.warning(f"Invalid corpus_id: {hit['corpus_id']}, max allowed: {len(self.passages)-1}")
            
            if not valid_hits:
                logger.warning("No valid hits found")
                return []
                
            # Process valid hits
            cross_inp = [[query, self.passages[hit['corpus_id']]] for hit in valid_hits]
            cross_scores = self.cross_encoder.predict(cross_inp)

            for idx in range(len(cross_scores)):
                valid_hits[idx]['cross-score'] = cross_scores[idx]

            hits = sorted(valid_hits, key=lambda x: x['cross-score'], reverse=True)
            results = []
            
            # Process top results
            for hit in hits[:min(5, len(hits))]:
                package_name = get_value(self.analysis_df, 'package_name', 
                                    self.analysis_df['cluster_id'] == hit['corpus_id'])
                if package_name:
                    logo = get_value(self.analysis_df, 'logo', 
                                self.analysis_df['cluster_id'] == hit['corpus_id'])
                    website = get_value(self.analysis_df, 'website', 
                                    self.analysis_df['cluster_id'] == hit['corpus_id'])
                    source_package = get_value(self.analysis_df, 'source', 
                                            self.analysis_df['cluster_id'] == hit['corpus_id'])
                    vignettes = ["To be added to scrapper"]
                    results.append({
                        "package_name": package_name,
                        "logo": logo,
                        "website": website,
                        "source": source_package,
                        "vignettes": vignettes,
                        "relevance": round(hit['score'], 4),
                    })

            # Remove duplicates and sort by relevance
            if results:
                results_df = pd.DataFrame(results).drop_duplicates(subset=['package_name'], keep='first')
                results_df = results_df.sort_values(by='relevance', ascending=False).head(num_results)
                return results_df.to_dict('records')
            return []
            
        except Exception as e:
            logger.error(f"Error in search: {str(e)}", exc_info=True)
            return []