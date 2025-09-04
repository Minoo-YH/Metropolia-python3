FACTOR = 2.54

while True:
    s = input("Enter inches (negative = exit): ").strip()
    s = s.replace(',', '.')

    try:
        inches = float(s)
    except ValueError:
        print("Wrong")
        continue

    if inches < 0:
        print("Program stopped!")
        break

    cm = inches * FACTOR
    print(f"{inches:g} inches = {cm:.2f} cm")

