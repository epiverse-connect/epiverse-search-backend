import os

class Settings:
    ENV: str = os.getenv("ENV", "local")
    DEBUG: bool = (ENV == "local")
    ORIGINS: list = {
        "local": ["http://localhost", "http://localhost:8000", "http://localhost:8080", "epiverse-connect.github.io"],
        "development": ["http://localhost"],
        "testing": ["http://localhost"],
        "uat" : ["http://localhost"],
        "production": ["http://localhost"]
    }.get(ENV, ["*"])

settings = Settings()