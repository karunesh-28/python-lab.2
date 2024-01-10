'''To find the Euclidean distance between two points in a two dimensional space
using class and object'''

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def euclidean_distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

# Example usage:
point1 = Point(1, 2)
point2 = Point(4, 6)

# Displaying the coordinates of the points
print(f"Point 1 coordinates: ({point1.x}, {point1.y})")
print(f"Point 2 coordinates: ({point2.x}, {point2.y})")

# Calculating and displaying the Euclidean distance
distance = point1.euclidean_distance(point2)
print(f"Euclidean Distance between Point 1 and Point 2: {distance}")
