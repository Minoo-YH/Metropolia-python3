fish_lenght = float(input("Enter the pike perch length in centimeters: "))
min_size=37.0
missing=37-fish_lenght
if fish_lenght >= 37:
    print("take fish ")

elif fish_lenght < min_size:
    print("fish too small back it to the lake ")
    print(f"It is {missing:.1f} cm below the minimum allowed size ({min_size:.0f} cm).")
