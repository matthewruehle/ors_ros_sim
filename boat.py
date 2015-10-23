"""
Contains the Boat class; 
"""
import math
import rospy
import rospkg
from geometry_msgs.msg import Point
from std_msgs.msg import Float64


class Sailboat(object):
	def __init__(self, ocean=None, nodename="boat_simulator"):
		self.orientation = 0.0 # degrees; FIAT: 0 = straight right; range = [0, 360)
		self.x = 0.0
		self.y = 0.0
		self.sail_slack = 0.0 # 0-90; it should go to the downwind side. this is how far out it goes.
		self.rudder_angle = 0.0 # [-45,45] ; relative to the boat itself ofc.
		self.velocity = 0.0
		self.acceleration = 0.0
		self.angular_velocity = 0.0
		self.angular_acceleration = 0.0 # not sure how relevant these will be.
		self.last_updated = rospy.Time.now() # keeps track of how often this thing updates.
		self.ocean = ocean
		self.mass = 0.0
		self.drag_coefficient = 0.0

		rospy.init_node(nodename)
		#rospy.Subscriber('/node_to_call', message_type_of_node, self.handle_instructions)
		self.position_pub = rospy.Publisher("/sim_boat_position", Point)		



	def refresh(self):
		self.x += self.velocity*math.cos(math.radians(self.orientation))
		self.y += self.velocity*math.sin(math.radians(self.orientation))

	def print_two(self):
		print "2"

	def query_ocean(self):
		conditions = self.ocean.get_conditions()

	def spoof_gps(self):
		"""
		TODO: get it to translate self.x and self.y into something approximating GPS positions.
		"""
		pass

	def spoof_wind_speed(self):
		"""
		TODO: self-explanatory.
		"""
		pass

	def spoof_wind_direction(self):
		"""
		TODO: get it to query the world; basically just gets the relative wind location.
		"""
		wind_dir = self.world.get_wind();
		pass

	def spoof_all_sensor_data(self):
		self.spoof_wind_direction()
		self.spoof_wind_speed()
		self.spoof_gps()



if __name__ == "__main__":
	sb = Sailboat()
