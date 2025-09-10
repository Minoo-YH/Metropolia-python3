import math


def unit_price_per_m2(diameter_cm,price_euro):
   radius_m = (diameter_cm/ 100) / 2
   area_m2 =math.pi * radius_m ** 2
   return area_m2 / price_euro

def main() :
    print("Enter two pizzas:")
    d1 = float(input("Pizza 1 diameter (cm): "))
    p1 = float(input("Pizza 1 price (€): "))
    d2 = float(input("Pizza 2 diameter (cm): "))
    p2 = float(input("Pizza 2 price (€): "))


    u1 = unit_price_per_m2(d1,p1)
    u2 = unit_price_per_m2(d2,p2)

    print(f"Pizza 1: {u1:.2f} €/m²")
    print(f"Pizza 2: {u2:.2f} €/m²")

    if u1 < u2:
            print("Better value: Pizza 1")
    elif u2 < u1:
            print("Better value: Pizza 2")
    else:
            print("Same value.")
main()