import paho.mqtt.client as mqtt
from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO

led = LED(14)
ledOn = True
run = True

def update_pins():
    print("ledOn: " + ledOn)
    if ledOn == True:
        GPIO.output(14, GPIO.HIGH)
    else:
        GPIO.output(14, GPIO.LOW)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("testChannel/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print("onmessage called")
    messageReceived = ""
    if "False" not in str(msg.payload):
        messageReceived = str(msg.payload).replace("b","").replace("'","")
        print("Received message: " + messageReceived)
        if (messageReceived == "on"):
            print("on")
            ledOn = True
            # GPIO.output(14, GPIO.HIGH)
            # update_pins()
            led.on()
        elif (messageReceived == "off"):
            print("off")
            ledOn = False
            # update_pins()
            # GPIO.output(14, GPIO.LOW)
            led.off()
        else:
            ledOn = False
            # GPIO.output(14, GPIO.LOW)
            print("neither, so off")
            led.off()
    else:
        run = False
        ledOn = False
        print("Publisher said False --> Client will be disconnected.")
        client.disconnect()
        exit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

while run == True:
    client.loop()