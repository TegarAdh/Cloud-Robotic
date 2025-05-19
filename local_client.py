# local_client.py
import rospy
from std_msgs.msg import String
import paho.mqtt.client as mqtt

FULL_NAME = "Tegar Adhi Nugraha Christ D"  
MQTT_BROKER = "54.169.70.0"
RESPONSE_TOPIC = "/whisper"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

def callback(msg):
    original_msg = msg.data
    print("Received from ROS: ", original_msg)
    response = f"Message received: {original_msg} by {FULL_NAME}"
    client.publish(RESPONSE_TOPIC, response)
    print("Sent to MQTT /whisper: ", response)

rospy.init_node('ros_to_mqtt_client')
rospy.Subscriber('/relay', String, callback)
rospy.spin()
