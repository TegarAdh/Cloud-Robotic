# server_bridge.py
import rospy
from std_msgs.msg import String
import paho.mqtt.client as mqtt

MQTT_BROKER = "54.169.70.0"
MQTT_TOPIC = "/broadcast"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    ros_msg = String()
    ros_msg.data = msg.payload.decode()
    pub.publish(ros_msg)
    print("Forwarded to ROS: ", ros_msg.data)

rospy.init_node('mqtt_to_ros_bridge')
pub = rospy.Publisher('/relay', String, queue_size=10)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_forever()
