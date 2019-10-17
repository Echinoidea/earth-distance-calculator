# Find the distance between 2 points on Earth
# The regular expressions are overkill. I'm just trying to practice using them :)
# Created by Gabriel Hooks on 2019-10-17

import re
import math

class Point:
	latitude = 0.0  # In radians
	longitude = 0.0 # In radians

	def __init__(self, lat, lon):
		self.latitude = lat
		self.longitude = lon

def input_coords(prompt):
	try:
		c = input(prompt)
		pattern = re.search(r"^(\-?\d{1,3})\s(\-?\d{1,2})\'\s(\-?\d{1,2})\"$", c)
		if pattern:
			dms = []
			dms.append(pattern.group(1))
			dms.append(pattern.group(2))
			dms.append(pattern.group(3))
			return dms
		else:
			print(c + " does not match")
			input_coords(prompt)
	except ValueError:
		print("Invalid input!")
		input_coords(prompt)

def DMS_to_rad(dms):
	deg = (int(dms[0])) + (int(dms[1])/60) + (int(dms[2]) / 3600)
	return deg * (math.pi / 180)

# Distance formula:
# 1: Use haversine formula
# a = sin^2(Δφ/2) + cos(φ1) * cos(φ1) * sin^2(Δλ/2)
# c = 2 * atan(sqrt(a), sqrt(1-a))
# d = r * c
# φ = latitude
# λ = longitude
# r = radius = 6371 * 10^3 (km to meters)
# a and b are the two points on the sphere
def calculate_distance(a, b):
	r = 6371000
	lat_1 = a.latitude
	lat_2 = b.latitude
	delta_lat = lat_1 - lat_2
	delta_lon = a.longitude - b.longitude

	a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(lat_1) * math.cos(lat_2) * math.sin(delta_lon/2) * math.sin(delta_lon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = r * c
	return d

def main():
	print("Enter coordinates in this format: d m' s\"\nFor bearings, use negative numbers instead of W and S\n")

	print("POINT A:")
	A = Point(DMS_to_rad(input_coords("Latitude: ")), DMS_to_rad(input_coords("Longitude: ")))
	print("POINT B:")
	B = Point(DMS_to_rad(input_coords("Latitude: ")), DMS_to_rad(input_coords("Longitude: ")))

	print("D = " + str(round(calculate_distance(A, B)/1000, 4)) + " km")

	print("\nI know the format requirements are overkill but I'm practicing regular expressions :)")

if __name__ == "__main__":
	main()
