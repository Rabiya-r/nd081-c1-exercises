import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world123'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'sampledb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Udacityadmin@'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'samplestorage3211'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'HbDqCBBXxwRoSAWAHZNhspnPcxb9h2C6SeqUJCEGry3WR/zEETk4qXTNsw5CJmAUJx59o0UdvaKk+AStf1CFGw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'mages'
