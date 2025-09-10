import random

def roll_die():
    """Return a random integer from 1 to 6 (like a die roll)."""
    return random.randint(1, 6)

def main():
    print("Rolling the die until we get a 6...")
    while True:
        value = roll_die()
        print(value)  # show the result of this roll
        if value == 6:
            break

if __name__ == "__main__":
    main()
