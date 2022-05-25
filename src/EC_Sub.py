import paho.mqtt.client as mqtt
from random import randrange, uniform
import random
import time 

topic = "EC-Availability"
def on_message(client, userdata, request):
    AVAILABILITY = random.randint(0, 1)
    REQUEST=str(request.payload.decode('utf-8'))
    print(f"-----------Request ---------\n {REQUEST} ")
    if "Availability" in REQUEST:
        print("\n\n----------------\n")
        print(f"Availability Status:{AVAILABILITY}")
        print("\n----------------\n\n")
    
    
mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client("Receiver")
client.connect(mqttBroker)

client.loop_start()
client.subscribe(topic)
client.on_message = on_message

time.sleep(500)
client.loop_end

