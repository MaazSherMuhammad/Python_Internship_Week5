import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

# Get radius from user
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)

print(f"Area of circle: {area:.2f}")
