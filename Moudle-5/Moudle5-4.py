cities = []

for i in range(5):
    while True:
        city = input(f"Enter city #{i + 1}: ").strip()
        if city:
            cities.append(city)
            break
        print("City name cannot be empty. Please try again.")

for city in cities:
    print(city)
