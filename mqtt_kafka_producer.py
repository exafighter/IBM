import paho.mqtt.client as mqtt
from random import uniform
import time

mqtt_broker='mqtt.eclipseprojects.io'
mqtt_client=mqtt.Client('MQTTProducer2')
mqtt_client.connect(mqtt_broker)
mqtt_topic='equipment' 

while True:
	randNumber=uniform(100,900)
	print('Generated Random Equipment Power Usage', randNumber)
	mqtt_client.publish(mqtt_topic, randNumber)
	print('MQTT: Published ' + str(randNumber) + ' to topic:' + mqtt_topic)
	time.sleep(10)
