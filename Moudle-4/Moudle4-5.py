correct_user = "python"
correct_pass = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user = input("Username: ")
    pwd = input("Password: ")

    if user == correct_user and pwd == correct_pass:
        print("Welcome")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Wrong username or password. Try again.")
else:
    # Runs only if the loop finished without 'break' (i.e., 5 wrong tries)
    print("Access denied")
