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