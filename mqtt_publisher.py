import paho.mqtt.publish as publish

def send_data(message):
    publish.single("testChannel/topic", message, hostname = "test.mosquitto.org")
    
# MQTT_SERVER = "192.168.0.37"
'''
while message != "cancel":
    message = input("Enter message: ")
    publish.single("testChannel/topic", message, hostname = "test.mosquitto.org")
'''
send_data("Hello World!")
send_data("False")
# publish.single(MQTT_PATH, "Hello World!", hostname = MQTT_SERVER)
# publish.single("testChannel/test", "Hello", hostname = "test.mosquitto.org")


print("Done")