# Composition function
import math
def circleData():
    print("Enter Centre Coordinates: ")
    centre_x = int(input("Enter x: "))
    centre_y = int(input("Enter y: "))   
    print("Enter Coordinates at circumference: ")
    circum_x = int(input("Enter x: "))
    circum_y = int(input("Enter y: "))  
    return 3.14 * (dist(centre_x, circum_x, centre_y, circum_y) ** 2)
def dist(x1, x2, y1, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance
print("Area of circle: ", circleData())