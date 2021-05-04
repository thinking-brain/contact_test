import os

secret_key = os.environ['SECRET_KEY']
PWD = os.environ['DATABASE_PASSWORD']
USERNAME = os.environ['DATABASE_USER']
HOST = os.environ['DATABASE_HOST']
PORT = os.environ['DATABASE_PORT']
DB = os.environ['DATABASE_NAME']
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}' \
    .format(username=USERNAME,password=PWD, host=HOST, port=PORT,db=DB)
