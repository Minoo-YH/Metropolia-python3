import random

def roll_die(sides):
    """Return a random integer from 1 to `sides` (inclusive)."""
    if sides < 2:
        raise ValueError("Die must have at least 2 sides.")
    return random.randint(1, sides)

def main():
    # Ask the user for the die's maximum face (i.e., total number of sides)
    while True:
        try:
            sides = int(input("Enter the die's number of sides (max face): "))
            if sides < 2:
                print("Please enter an integer >= 2.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    print(f"Rolling a {sides}-sided die until we get {sides}...")
    while True:
        value = roll_die(sides)
        print(value)  # show the result of this roll
        if value == sides:
            break

if __name__ == "__main__":
    main()

