class Config(object):
    SQLALCHEMY_DATABASE_URI = '"postgresql:///flask_demo"'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'test'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
