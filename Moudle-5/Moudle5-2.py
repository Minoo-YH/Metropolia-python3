# Python 3.7+

numbers = []

# Read numbers until the user enters an empty line
for s in iter(lambda: input("Enter a number (empty to finish): ").strip(), ""):
    try:
        x = float(s.replace(",", "."))  # accept 12.5 or 12,5
        numbers.append(x)
    except ValueError:
        print("Invalid number, try again.")

if len(numbers) < 3:
    print("Need at least 3 numbers to exclude the largest and smallest.")
else:
    numbers.sort(reverse=True)          # descending: max ... min
    trimmed = numbers[1:-1]             # drop one overall max and one overall min
    top5 = trimmed[:5]                  # take the next five largest

    def fmt(v: float) -> str:
        return str(int(v)) if v.is_integer() else f"{v:g}"

    print("Five largest (excluding overall max & min):",
          ", ".join(fmt(v) for v in top5))


