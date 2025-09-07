from kafka import KafkaConsumer
import json

# Configure the consumer
consumer = KafkaConsumer(
    'my_topic',  # The topic(s) to subscribe to
    bootstrap_servers=['localhost:9092'],  # Kafka broker address
    auto_offset_reset='earliest',  # Start consuming from the beginning if no committed offset
    enable_auto_commit=True,  # Automatically commit offsets
    group_id='my_consumer_group',  # Consumer group ID for coordinated consumption
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # Deserializer for message value
)

# Consume messages
for message in consumer:
    print(f"Received message: Topic={message.topic}, Partition={message.partition}, "
          f"Offset={message.offset}, Key={message.key}, Value={message.value}")

# Close the consumer when done (optional, can be handled by program termination)
consumer.close()