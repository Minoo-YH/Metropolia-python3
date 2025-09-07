

import math

n_str = input("Enter an integer: ").strip()

try:
    n = int(n_str)
except ValueError:
    print("That is not an integer.")
    raise SystemExit

if n < 2:
    print(f"{n} is NOT a prime.")
else:
    is_prime = True
    limit = int(math.sqrt(n))
    for d in range(2, limit + 1):
        if n % d == 0:
            is_prime = False
            # Optional: explain a found divisor
            # print(f"Divisible by {d} (and {n//d}).")
            break

    if is_prime:
        print(f"{n} IS a prime.")
    else:
        print(f"{n} is NOT a prime.")
