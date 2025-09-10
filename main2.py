from config import config
import asyncio
from utils.kafka_101.kafka_utils import AsyncKafkaConsumer
from utils.elasticsearch_101.elasticsearch_utils import ElasticSearchClient
from utils.mongodb_101.mongodb_utils import MongoDBClient
from utils.hashjson import compute_hash
from log.login import Logger


logger = Logger.get_logger()


async def main():
    #חיבור אלסטיק
    logger.info("Starting elasticsearch consumer service...")
    try:
        es_client = ElasticSearchClient()
        if not es_client.is_connect():
            logger.info("ElasticSearch client is not connected")
            raise Exception("ElasticSearch client is not connected")
        else:
            es_client.create_index()
            logger.info("ElasticSearch index created")
            logger.info("Connected to elasticsearch")
            logger.info("Elasticsearch client initialized and connected.")
    except Exception as e:
        logger.error(f"Failed to initialize Elasticsearch client: {e}")
        return

    #חיבור KAFKA
    consumer = AsyncKafkaConsumer(
                [config.KAFKA_TOPIC],
                bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
                group_id=config.KAFKA_GROUP_ID,
            )
    logger.info("Consumer initialized")
    try:
        await consumer.start()
        logger.info("Kafka consumer started successfully")
    except Exception as e:
        logger.error(f"Failed to start Kafka consumer: {e}")
        return

    #חיבור ל-mongoDB
    logger.info("Starting retriever service mongoDB...")
    try:
        db_client = MongoDBClient(
            url=config.MONGO_URL,
            mongodb=config.MONGO_DB,
            mongo_collection=config.MONGO_COLLECTION,
        )
        await db_client.client
        logger.info("MongoDB client initialized and connected.")
    except Exception as e:
        logger.error(f"Failed to initialize MongoDB client: {e}")
        return


    logger.info("Main loop started successfully")
    while True:
        try:
            async for topic, data in consumer.consume():
                logger.info(f"Received message: {data}")
                hashing = compute_hash(data['metadata'])
                logger.info(f"Hashing message: {hashing}")
                try:
                    response = es_client.create_document(data['metadata'], hashing)#הכנסה לאלסטיק
                    logger.info(f"Document indexed successfully{response}")
                    logger.info(f"Document hashing successfully{response}")
                except Exception as e:
                    logger.error(f"Failed to create document: {e}")
                try:
                    logger.info("Uploading the original file with hash to mongoDB...")
                    add_file_in_mongo = db_client.add_file_gridfs(data['path'], hashing)#הכנסה והעלת קובץ ל-mongoDB
                    logger.info(f"Adding file gridfs successfully{add_file_in_mongo}")
                except Exception as e:
                    logger.error(f"Failed to add file gridfs in mongoDB: {e}")
        except Exception as e:
            logger.error(f"Error in consumer loop: {e}")
            logger.debug("Continuing with next iteration after error...")



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Retriever service stopped by user")
    except Exception as e:
        logger.critical(f"Critical error in main: {e}")
        raise