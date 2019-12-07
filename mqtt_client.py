import paho.mqtt.client as mqtt
 
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
run = True
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("testChannel/test")
    client.subscribe("testChannel/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("onmessage called")
    messageReceived = ""
    # print(msg.topic + "-" + str(msg.payload))
    # if str(msg.payload) == "False":
    if "False" not in str(msg.payload):
        messageReceived = str(msg.payload).replace("b","").replace("'","")
        print("Received message: " + messageReceived)
    else:
        run = False
        print("Client will be disconnected")
        client.disconnect()
        exit()
# while run == True:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
# client.loop()    
while run == True:
    client.loop()
    
    # do something
    # if run: client.loop()
    # else: exit()

 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# client.loop_forever()

