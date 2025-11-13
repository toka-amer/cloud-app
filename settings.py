import os
#--------- Flask settings
SERVER_HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
SERVER_PORT = int(os.environ.get('SERVER_PORT', 8000))
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

# for local host if Azure functions served locally
API_URL = "http://neighborly-webapi-cmbxd6dcg2ffdvdb.canadacentral-01.azurewebsites.net/api"
