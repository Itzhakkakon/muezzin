from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', # Replace with your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Optional: Serialize messages as JSON
)

topic_name = 'my_topic'

for i in range(5):
    message_data = {'id': i, 'message': f'This is message {i}'}
    producer.send(topic_name, message_data)
    print(f"Sent: {message_data}")
    time.sleep(1)

producer.flush()
producer.close()
print("Producer closed.")