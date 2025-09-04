import random

N = int(input("How many random points to draw? "))

if N <= 0:
    print("Please enter a positive integer.")
else:
    inside = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y < 1.0:  # inside the unit circle
            inside += 1

    pi_est = 4 * inside / N
    print(f"Estimated pi: {pi_est}")
