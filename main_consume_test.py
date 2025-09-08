from config import config
from load_data.load_data import LoadData
import logging
from utils.kafka_101.kafka_utils import AsyncKafkaProducer
from utils.kafka_101.kafka_utils import AsyncKafkaConsumer
import asyncio


logging.basicConfig(level=config.LOG_LEVEL)
logging.getLogger("kafka").setLevel(level=config.LOG_KAFKA)
logger = logging.getLogger(__name__)


async def main():
    consumer = AsyncKafkaConsumer(
                [config.KAFKA_TOPIC],
                bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
                group_id=config.KAFKA_GROUP_ID,
            )
    try:
        await consumer.start()
        logger.info("Kafka consumer started successfully")
    except Exception as e:
        logger.error(f"Failed to start Kafka consumer: {e}")
        return
    try:
        while True:
            try:
                async for msg in consumer.consume():
                    print(msg)
            except Exception as e:
                logger.error(f"Error in consumer loop: {e}")
                logger.debug("Continuing with next iteration after error...")
    except Exception as e:
        logger.error(f"Error in main processing loop: {e}")
        logger.debug("Continuing with next iteration after error...")
    logger.debug("Waiting 60 seconds before next poll...")
    await asyncio.sleep(60)  # Poll every minute




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Retriever service stopped by user")
    except Exception as e:
        logger.critical(f"Critical error in main: {e}")
        raise