from mykafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
producer.send('my_topic', {'key': 'value1', 'data': 'message from Python'})
producer.flush() # Ensure all messages are sent

# Consumer Example
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest', # Start consuming from the beginning if no committed offset
    enable_auto_commit=True,
    group_id='my_python_consumer_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received message: {message.value} from topic {message.topic} partition {message.partition}")