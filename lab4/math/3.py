import math

def regular_polygon_area(sides, length):
    return round((sides * (length ** 2)) / (4 * math.tan(math.pi / sides)), 2)

sides = 4
length = 25
print(f"Input number of sides: {sides}")
print(f"Input the length of a side: {length}")
print(f"The area of the polygon is: {regular_polygon_area(sides, length)}")
