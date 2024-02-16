#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def publish_test_data():
    # Initialize the ROS Node
    rospy.init_node('test_data_publisher', anonymous=True)

    # Create a publisher object publishing to the 'test_data' topic
    publisher = rospy.Publisher('/test_data', String, queue_size=10)

    # Set the loop rate (1 Hz, i.e., once per second)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Your test data
        test_data_str = "test data %s" % rospy.get_time()

        # Log the message to the ROS log for debugging
        rospy.loginfo(test_data_str)

        # Publish the message
        publisher.publish(test_data_str)

        # Sleep to maintain the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_test_data()
    except rospy.ROSInterruptException:
        pass
