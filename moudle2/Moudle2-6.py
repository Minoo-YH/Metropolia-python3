# lock_codes.py
# Generate and print two lock codes:
# - a 3-digit code with digits 0..9
# - a 4-digit code with digits 1..6

import random

three_digit = "".join(str(random.randint(0, 9)) for _ in range(3))
four_digit  = "".join(str(random.randint(1, 6)) for _ in range(4))

print("Three-digit code (0-9):", three_digit)
print("Four-digit code (1-6):", four_digit)

