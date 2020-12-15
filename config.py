import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    SECRET_KEY = os.urandom(32)
    #app.config['SECRET_KEY'] = SECRET_KEY
    #
    #SQL_SERVER = os.environ.get('SQL_SERVER') or '[SQL_SERVER_GOES_HERE]'
    SQL_SERVER = 'fam-udacizoo-sql-svr.database.windows.net'
    #
    #SQL_DATABASE = os.environ.get('SQL_DATABASE') or '[SQL_DATABASE_GOES_HERE]'
    SQL_DATABASE = 'fam-udacizoo-sql-db'
    #
    #SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or '[SQL_USER_NAME_GOES_HERE]'
    SQL_USER_NAME = 'famroot'
    #
    #SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[SQL_PASSWORD_GOES_HERE]'
    SQL_PASSWORD = 'Nyamurongi2'
    #
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    #
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or '[BLOB_ACCOUNT_GOES_HERE]'
    BLOB_ACCOUNT = 'famudacizoostrgacct'
    #
    #BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '[BLOB_STORAGE_KEY_GOES_HERE]'
    BLOB_STORAGE_KEY = '7gsJu11WSAjWioyaOdB9dbcbzqS25KZcKQGeadosynVHRm98rG1yuix3RzrzKV8PJcl5C+KlGfnTFMLXJ/Tr+w=='
    #BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or '[BLOB_CONTAINER_GOES_HERE]'
    BLOB_CONTAINER = 'famudacizoostrgctnr'
    #
