from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    package_name: str
    logo: str | None = None
    website: str | None = None
    source: str | None = None
    vignettes: list[str] | None = Field(default=None, alias="articles")
    relevance: float

    class Config:
        allow_population_by_field_name = True  # Allows using 'vignettes' in code


class SearchResponse(BaseModel):
    query: str
    filter: str
    response: dict[str, list[SearchResult]]

class UserQuery(BaseModel):
    query_user: str = Field(..., description="The user's search query")
