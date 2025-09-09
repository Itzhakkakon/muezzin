from config import config
import logging
# from log.login import Logger
import asyncio
from utils.kafka_101.kafka_utils import AsyncKafkaConsumer
from utils.elasticsearch_101.elasticsearch_utils import ElasticSearchClient

# logger = Logger.get_logger()


logging.basicConfig(level=config.LOG_LEVEL2)
logging.getLogger("kafka").setLevel(level=config.LOG_KAFKA2)
logger = logging.getLogger(__name__)



async def main():
    logger.info("Starting elasticsearch consumer service...")
    try:
        es_client = ElasticSearchClient()
        es_client.get_clinet()
        #await es_client.create_index()
        logger.info("Elasticsearch client initialized and connected.")
    except Exception as e:
        logger.error(f"Failed to initialize Elasticsearch client: {e}")
        return


    consumer = AsyncKafkaConsumer(
                [config.KAFKA_TOPIC],
                bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
                group_id=config.KAFKA_GROUP_ID,
            )
    try:
        logger.info("Starting consumer...")
        await consumer.start()
        logger.info("Kafka consumer started successfully")
    except Exception as e:
        logger.error(f"Failed to start Kafka consumer: {e}")
        return

    try:
        while True:
            try:
                async for msg in consumer.consume():
                    logger.info(f"Received message: {msg}")
                    await es_client.create_document(msg)
                    logger.info("Document indexed successfully")
            except Exception as e:
                logger.error(f"Error in consumer loop: {e}")
                logger.debug("Continuing with next iteration after error...")
    except Exception as e:
        logger.error(f"Error in main processing loop: {e}")
        logger.debug("Continuing with next iteration after error...")



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Retriever service stopped by user")
    except Exception as e:
        logger.critical(f"Critical error in main: {e}")
        raise