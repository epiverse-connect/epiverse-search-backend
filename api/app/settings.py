import os

class Settings:
    ENV: str = os.getenv("ENV", "local")
    DEBUG: bool = (ENV == "development" or ENV == "local")
    ORIGINS: list = {
        "local": ["http://localhost", "http://localhost:8000", "http://localhost:8080", "epiverse-connect.github.io"],
        "development": ["https://collaboratory-dev.who.int", "epiverse-connect.github.io"],
        "testing": ["https://collaboratory-test.who.int"],
        "uat" : ["https://collaboratory-uat.who.int"],
        "production": ["https://collaboratory.who.int"]
    }.get(ENV, ["*"])

settings = Settings()