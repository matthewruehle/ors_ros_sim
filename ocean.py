"""
Contains the Ocean class, which has values like wind and provides a coordinate frame.
"""

class Ocean(object):
	def __init__(self):
		self.wind_dir = 0.0 # 0.0 = due east. 90 = due north. [0,360)
		self.wind_speed = 0.0 # still not sure about the units.
		


if __name__ == "__main__":
	pass