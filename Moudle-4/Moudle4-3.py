nums = []

while True:
    s = input("Enter a number (empty to finish): ").strip()
    if s == "":
        break

    s = s.replace(',', '.')
    try:
        x = float(s)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    nums.append(x)

if nums:
    print(f"min = {min(nums):g}, max = {max(nums):g}")
else:
    print("No numbers entered.")

