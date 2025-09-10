from config import config
from load_data.load_data import LoadData
from log.login import Logger
from utils.kafka_101.kafka_utils import AsyncKafkaProducer
import asyncio

logger = Logger.get_logger()



async def main():
    datas = LoadData()
    producer = AsyncKafkaProducer(
        bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}"
    )

    try:
        await producer.start()
        logger.info("Kafka producer started successfully")
    except Exception as e:
        logger.error(f"Failed to start Kafka producer: {e}")
        return

    logger.info("Starting main processing loop...")
    poll_count = 0


    try:
        poll_count += 1
        logger.debug(f"Polling iteration #{poll_count}")

        meseege_count = 0
        for data in datas.load():
            await producer.send_json(config.KAFKA_TOPIC, data)
            meseege_count += 1
            logger.info(f"Sent {meseege_count} messages to Kafka topic {config.KAFKA_TOPIC}")
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