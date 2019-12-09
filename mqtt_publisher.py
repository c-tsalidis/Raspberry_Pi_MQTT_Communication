import paho.mqtt.publish as publish

message = ""
def send_data(_message):
    publish.single("testChannel/topic", _message, hostname = "test.mosquitto.org")
    

while message != "cancel":
    message = input("Enter message: ")
    send_data(message)

print("Done")
