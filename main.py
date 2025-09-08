from config import config
from load_data.load_data import LoadData
from utils.kafka_101.kafka_configurations import get_consumer_events
from utils.kafka_101.kafka_configurations import get_producer_config
from utils.kafka_101.kafka_producer import publish_message
from utils.kafka_101.kafka_consumer import consumer_with_auto_commit


def main():
    datas = LoadData()
    consumer_with_auto_commit(config.KAFKA_TOPIC)
    producer = get_producer_config()
    for data in datas.load():
        publish_message(producer, config.KAFKA_TOPIC, data)
    consumer_with_auto_commit(config.KAFKA_TOPIC)


if __name__ == "__main__":
    main()



