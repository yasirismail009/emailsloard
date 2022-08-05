# Django
DJANGO_SECRET_KEY = 'django-insecure-w%#e^yonm7ri6fmbc*_5i^i^z*c$m=p*t%&sla6r26i%zv*fif'
HTTP_API_SECRET = 'ce682dfe15a227eec1101359929c54a2'
DEFAULT_DB_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'email_api_backend',
    'USER': 'yasir_cms_user',
    'PASSWORD': 'Malik@0900',
    'HOST': 'localhost',
    'PORT': '5433',
}

# Postgres
PSQL_HOST = '43.251.253.240'
PSQL_PORT = '5430'
PSQL_USER = 'airflow_usr'
PSQL_PSWD = 'zxcvzxcv'
PSQL_SCH_01_A = 'public'
PSQL_DB_01 = 'email_api_backend'
PSQL_TAB_01_A = 'user'

MONGO_URI = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

# MONGO_URI_Apps = "mongodb://threat_db_user_d_one:TE72kjWEAsm5nUnwEkL9XR9grGB8y3fasdfKdusajjvPCg26HZxrykzKZPyQMD53@privacydefender.app:27020/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=true"
# MONGO_URI_Hash = "mongodb://threat_db_filehash_user_one:TE72kjWEAsm5nUnwEkL9XR9grGB8y3fasdfKdusajjvPCg26HZxrykzKZPyQMD53@privacydefender.app:27024/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=true"

MONGO_DB_01 = 'email'


MONGO_COL_01_A = 'sender'
MONGO_COL_01_B = 'receiver'
