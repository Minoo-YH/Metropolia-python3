# Get and normalize gender input
gender = input("Enter biological gender (male/female) [m/f]: ").strip().lower()

# Decide normal range based on gender
if gender in ("male", "m"):
    low, high = 134.0, 195.0
    gender_label = "male"
elif gender in ("female", "f"):
    low, high = 117.0, 175.0
    gender_label = "female"
else:
    print("Invalid gender. Please try again.")
    raise SystemExit

# Get hemoglobin safely
try:
    hg = float(input("Enter hemoglobin (g/L): ").strip())
except ValueError:
    print("Invalid input. Please enter a number like 145 or 146.5.")
    raise SystemExit

# Optional sanity check
if hg <= 0:
    print("Hemoglobin must be a positive number.")
    raise SystemExit

# Classify
if hg < low:
    status = "LOW"
elif hg > high:
    status = "HIGH"
else:
    status = "NORMAL"

# Output
print(f"Hemoglobin status: {status}")
print(f"For {gender_label}, normal range is {low:.0f}–{high:.0f} g/L. You entered {hg:.1f} g/L.")


