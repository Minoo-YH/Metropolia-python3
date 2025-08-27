# rectangle.py
# Ask for the rectangle's base and height, then print perimeter and area.

base = float(input("Enter the rectangle's base: ").replace(",", "."))
height = float(input("Enter the rectangle's height: ").replace(",", "."))

perimeter = 2 * (base + height)
area = base * height

print(f"Perimeter: {perimeter:.2f}")
print(f"Area: {area:.2f}")
