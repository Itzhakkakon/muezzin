import os

DIRECTORY_PATH = os.getenv("DIRECTORY_PATH", r"C:\podcasts")


KAFKA_PROTOKOL = os.getenv("KAFKA_PROTOKOL", "http")
KAFKA_URL = os.getenv("KAFKA_URL", "localhost")
KAFKA_PORT = int(os.getenv("KAFKA_PORT", 9092))
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "podcasts")