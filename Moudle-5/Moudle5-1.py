import random
n = int (input("How manay dice?"))
total = 0

for i in range(n):
     roll = random.randint(1,6)
     total += roll

print("Sum of the face values:",total)