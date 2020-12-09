import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = os.urandom(32)
    # app.config['SECRET_KEY'] = SECRET_KEY
    # SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Avamara34@localhost/pitch_test'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Avamara34@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}