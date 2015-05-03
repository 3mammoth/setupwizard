import os

BACKUP_FOLDER = os.getcwd() + "/backup"
USAGE_STRING = "\nUsage \npython setup.py shell\n" \
               "python setup.py backup [option, e.g. \"-s\"]\n" \
               "python setup.py restore [option, e.g. \"-s\"]"
