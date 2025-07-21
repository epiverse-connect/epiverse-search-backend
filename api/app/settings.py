import os

class Settings:
    ENV: str = os.getenv("ENV", "local")
    DEBUG: bool = (ENV == "local")

    DEFAULT_ORIGINS = {
        "local": [
            "http://localhost",
            "http://localhost:5000",
            "http://localhost:8080",
            "epiverse-connect.github.io"
        ],
        "development": ["http://localhost"]
    }

    origins_env = os.getenv("ORIGINS")
    env = os.getenv("ENV", "local")
    ORIGINS: list = (
        origins_env.split(",") if origins_env else DEFAULT_ORIGINS.get(env, [])
    )

settings = Settings()