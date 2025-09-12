seasons_by_month = (
        "winter", # 1: January
        "winter",  # 2: February
        "spring", # 3: March
        "spring", # 4: April
        "spring",  # 5: May
        "summer",   # 6: June
        "summer", # 7: July
        "summer",  # 8: August
        "fall",  # 9: September
        "fall", # 10: October
        "fall",  # 11: November
        "winter", # 12: December (first month of winter per the task)
    )

month_names = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

raw = int(input("Enter month number (1-12):"))


try:
         month = int(raw)
         if 1 <= month <= 12:
             name = month_names[month - 1]
             season = seasons_by_month[month - 1]
             print(f"Month {month}: {name} — {season}")

         else:
             print("Invalid input")
except ValueError:
          print("Error: please enter a number.")
