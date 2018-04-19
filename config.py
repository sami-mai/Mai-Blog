class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sami_mai:SmaiDB@localhost/maiblog'
    DEBUG = True


config_options = {
    "production": ProdConfig,
    "default": DevConfig
    }
