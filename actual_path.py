import rospy
from nav_msgs.msg import Path
import csv
from geometry_msgs.msg import PoseStamped, PointStamped

rospy.init_node("create_1_path_followed")

plan_publisher = rospy.Publisher('/path_taken', Path, queue_size=10)

rate = rospy.Rate(10.0)


new_plan = Path()
new_plan.header.frame_id = 'map'


while not rospy.is_shutdown():
	point = rospy.wait_for_message('/roomba/location', PointStamped)
	way_point = PoseStamped()
	x = point.point.x 
	y = point.point.y
	way_point.pose.position.x = x
	way_point.pose.position.y = y
	new_plan.poses.append(way_point)
	plan_publisher.publish(new_plan)

	 
