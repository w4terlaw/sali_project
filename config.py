from decouple import config


class Config:
    SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL", default="sqlite:///./test.sqlite")
