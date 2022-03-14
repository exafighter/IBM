import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

mqtt_broker='mqtt.eclipseprojects.io'
mqtt_client=mqtt.Client('MQTTBridge')
mqtt_client.connect(mqtt_broker)
mqtt_topic='equipment' 

kafka_client=KafkaClient(hosts='localhost:9092')
kafka_topic=kafka_client.topics['micro']
kafka_producer=kafka_topic.get_sync_producer()

def on_message(client, userdata, message):
	msg_payload = message.payload
	msg_payload_str = str(message.payload.decode("utf-8"))
	print('MQTT: Received message from MQTT topic: ' + mqtt_topic + '  ' + msg_payload_str)
	kafka_producer.produce(msg_payload)
	print('Kafka: Published the value: ' + msg_payload_str + ' to Kafka topic: micro')
	print('=== End of Single Message MQTT->Kafka Transmission ===')

mqtt_client.loop_start()
mqtt_client.subscribe(mqtt_topic)
mqtt_client.on_message = on_message
time.sleep(300)
mqtt_client.loop_stop()


