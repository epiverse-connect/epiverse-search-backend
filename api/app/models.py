from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    package: str
    title: str
    description: str | None = None
    language: str = "R"  # Added static field
    logo: str | None = None
    website: str | None = None
    source: str | None = None
    vignettes: list[str] | None = Field(default=None, alias="articles")
    relevance: float

    class Config:
        validate_by_name = True  # Allows using 'vignettes' in code
        by_alias = False 


class SearchResponse(BaseModel):
    query: str
    filter: str
    response: dict[str, list[SearchResult]]

class UserQuery(BaseModel):
    query_user: str = Field(..., description="The user's search query")
