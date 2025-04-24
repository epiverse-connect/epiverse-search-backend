import pandas as pd
import logging.config
import yaml
import os
from logging.handlers import RotatingFileHandler

def setup_logging(default_path='logging_config.yaml', default_level=logging.INFO):
    """Setup logging configuration"""
    try:
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', default_path)
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                # Ensure logs directory exists
                os.makedirs('logs', exist_ok=True)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            logging.warning(f"Logging config file not found at {config_path}")
    except Exception as e:
        logging.basicConfig(level=default_level)
        logging.error(f"Error in logging setup: {str(e)}")

        
def get_value(df: pd.DataFrame, column: str, condition: pd.Series):
    try:
        return df.loc[condition, column].iloc[0]
    except IndexError:
        return None