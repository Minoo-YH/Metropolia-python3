year = int(input("Enter a year: ").strip())
if year % 4 == 0 :
    print("YES leap year")

elif year % 100 == 0 :
    print("Not leap year")

elif year % 400 == 0 :
    print("Leap year")

else:
    print("Not leap year")