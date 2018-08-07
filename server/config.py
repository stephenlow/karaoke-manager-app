# DB settings
pg_db_username = 'stephenlow'
pg_db_password = ''
pg_db_name = 'karaoke-manager-db'
pg_db_hostname = 'localhost'

SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username,
                                                                                        DB_PASS=pg_db_password,
                                                                                        DB_ADDR=pg_db_hostname,
                                                                                        DB_NAME=pg_db_name)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
PORT = 5000
HOST = "127.0.0.1"
DEBUG = True
