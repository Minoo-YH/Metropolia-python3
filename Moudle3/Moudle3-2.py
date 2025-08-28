# Ask for the cabin class
cabin = input("Enter cabin class (LUX, A, B, C): ").strip().upper()

if cabin == "LUX":
    print("LUX is a balcony cabin on the upper deck.")
elif cabin == "A":
    print("A is a cabin with a window above the car deck.")
elif cabin == "B":
    print("B is a windowless cabin above the car deck.")
elif cabin == "C":
    print("C is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class. Please enter LUX, A, B, or C.")