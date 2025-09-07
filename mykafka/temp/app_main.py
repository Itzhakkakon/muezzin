from kafka.config import config
from kafka.kafka_utils import AsyncKafkaProducer


producer = AsyncKafkaProducer(
    bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}"
)