import paho.mqtt.publish as publish

message = ""
def send_data(_message):
    publish.single("testChannel/topic", _message, hostname = "test.mosquitto.org")
    
'''
while message != "cancel":
    message = input("Enter message: ")
    send_data(message)
'''
send_data("Hello World!")
send_data("Message sent from another device to the Rasp Pi via Internet and MQTT communication")
send_data("False")
print("Done")
