import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import requests
from datetime import datetime

def httpPost(Host):
    pload = {
            'Host': Host, 
            'request':input("request:"), 
            'datetime':datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
            } 
    r = requests.post('https://httpbin.org/post', data = pload)
    r_dictionary= r.json()
    return r_dictionary

Host = input("Host:")
mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client(Host)

client.connect(mqttBroker)
topic = "EC-Availability"

while True:
    request = httpPost(Host)
    client.publish(topic, f"At:{request['form']['datetime']} \n From:{request['form']['Host']} Request : {request['form']['request']}")
    print(f"{Host} just published {request['form']['request']} to Topic {topic}.")
