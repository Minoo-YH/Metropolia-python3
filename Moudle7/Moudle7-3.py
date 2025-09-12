# Airport info: add (new), fetch, or quit. Stores data in a dict in memory.

airports = {}

def prompt_action():
    return input("Choose action (new, fetch, quit): ").strip().lower()

while True:
    action = prompt_action()

    if action == "new":
        code = input("Enter ICAO code (e.g., EFHK): ").strip().upper()
        name = input("Enter airport name: ").strip()

        if not code or not name:
            print("Error: both ICAO code and airport name are required.")
            continue

        airports[code] = name
        print("Saved.")

    elif action == "fetch":
        code = input("Enter ICAO code to look up: ").strip().upper()
        if not code:
            print("Error: ICAO code is required.")
            continue

        if code in airports:
            print(f"{code} -> {airports[code]}")
        else:
            print("Airport not found.")

    elif action == "quit":
        print("Goodbye!")
        break

    else:
        print("Unknown action. Please type: new, fetch, or quit.")
