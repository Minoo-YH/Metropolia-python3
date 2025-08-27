# three_numbers.py
# Ask for three integers, then print their sum, product, and average.

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

total = a + b + c
product = a * b * c
average = total / 3

print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
