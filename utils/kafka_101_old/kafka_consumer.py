from kafka import KafkaConsumer
import logging
import json
from utils.kafka_101.kafka_configurations import get_consumer_events

def consumer_with_auto_commit(topic):
    """

    :param topic: Topic to consume message from
    :return:
    """
    #Create consumer object which consumes any message from the topic

    events = get_consumer_events(topic)
    print_messages(events)


def print_messages(events):
    # Iterate through the messages
    for message in events:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))


if __name__ == '__main__':
    logging.getLogger('kafka').setLevel(logging.ERROR)
    #logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info("Consumer app started")
    topics = "topic1"
    consumer_with_auto_commit(topics)
    logging.info("consumer_with_auto_commit completed")











# # consumer.py - גרסה נקייה
#
# from kafka import KafkaConsumer
# import json
# from datetime import datetime
# import logging
#
# # מבטל את כל הלוגים הטכניים
# logging.getLogger('kafka').setLevel(logging.WARNING)
#
#
# def consumer_with_auto_commit(topic):
#     print("=" * 60)
#     print(f"מתחיל להאזין להודעות מTopic: {topic}")
#     print("=" * 60)
#
#     events = get_consumer_events(topic)
#     print_messages(events)
#
#
# def print_messages(events):
#     message_count = 0
#
#     for message in events:
#         message_count += 1
#
#         # הופך timestamp לזמן קריא
#         now = datetime.now().strftime('%H:%M:%S')
#
#         print(f"\n📨 הודעה #{message_count} ({now})")
#         print(f"🔑 Key: {message.key}")
#         print(f"💬 Content: {message.value}")
#         print(f"📍 Partition: {message.partition}, Offset: {message.offset}")
#         print("-" * 50)
#
#
# if __name__ == '__main__':
#     print("🎧 Consumer נקי מתחיל...")
#     consumer_with_auto_commit("topic1")