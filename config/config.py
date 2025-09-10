import os
#path
DIRECTORY_PATH = os.getenv("DIRECTORY_PATH", r"C:\podcasts")

#kafka
KAFKA_PROTOKOL = os.getenv("KAFKA_PROTOKOL", "http")
KAFKA_URL = os.getenv("KAFKA_URL", "localhost")
KAFKA_PORT = int(os.getenv("KAFKA_PORT", 9092))
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "podcasts")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "persister_service")


#logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_KAFKA = os.getenv("LOG_KAFKA", "ERROR").upper()
LOG_MONGO = os.getenv("LOG_MONGO", "ERROR").upper()

#elastic
ES_HOST = os.getenv("ES_HOST", "localhost")
ES_PORT = int(os.getenv("ES_PORT", 9200))
ES_PROTOCOL = os.getenv("ES_PROTOCOL", "http")
ES_URL = os.getenv("ES_URL", f"{ES_PROTOCOL}://{ES_HOST}:{ES_PORT}")

ES_INDEX_DATA = os.getenv("ES_INDEX_DATA", "podcasts")


# MAPPING_CONFIG = {
#     "mappings": {
#         "properties": {
#             "path": {"type": "keyword"},
#             "metadata": {
#                 "properties": {
#                     "bitdepth": {"type": "integer"},
#                     "bitrate": {"type": "float"},
#                     "channels": {"type": "integer"},
#                     "duration": {"type": "float"},
#                     "filename": {"type": "keyword"},
#                     "filesize": {"type": "integer"},
#                     "samplerate": {"type": "integer"},
#                 }
#             }
#         }
#     }
# }

#דוגמא ל-json שחוזר מ-load_data
# {'metadata': {'bitdepth': 16,
#               'bitrate': 384.0,
#               'channels': 1,
#               'duration': 51.13095833333333,
#               'filename': 'C:\\podcasts\\download (1).wav',
#               'filesize': 2454330,
#               'samplerate': 24000},
#  'path': 'C:\\podcasts\\download (1).wav'}

#docker-compose
MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "izak")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "54321")
MONGO_EXPRESS_USERNAME = os.getenv("MONGO_EXPRESS_USERNAME", "izak")
MONGO_EXPRESS_PASSWORD = os.getenv("MONGO_EXPRESS_PASSWORD", "54321")

ME_CONFIG_MONGODB_PORT = os.getenv("ME_CONFIG_MONGODB_PORT", "27017")
ME_CONFIG_MONGODB_SERVER = os.getenv("ME_CONFIG_MONGODB_SERVER", "mongodb")

#mongoDB
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_PROTOCOL = os.getenv("MONGO_PROTOCOL", "mongodb")
MONGO_URL = os.getenv("MONGO_URL", f"{MONGO_PROTOCOL}://{MONGO_HOST}:{MONGO_PORT}")

MONGO_DB = os.getenv("MONGO_DB", "muezzin")
MONGO_COLLECTION = os.getenv("MY_COLLECTION", "podcasts")