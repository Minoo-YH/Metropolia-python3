#circle_area.py
#ask for circle and print it

import math

r = float(input("Enter the radius of the circle: "))
area = math.pi * (r ** 2)
print(f"The area of the circle with radius {r} is: {area:.2f}")