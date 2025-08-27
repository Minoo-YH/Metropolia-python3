# Medieval mass converter: lev → nail → bullet → grams → kg + g
# 1 lev = 20 nails
# 1 nail = 32 bullets
# 1 bullet = 13.3 grams

# Ask for amounts
levs = int(input("Levs: "))
nails = int(input("Nails: "))
bullets = int(input("Bullets: "))

# Convert everything to bullets
total_bullets = bullets + nails * 32 + levs * 20 * 32

# Avoid floating issues by working in decigrams (0.1 g)
# 13.3 g = 133 decigrams
total_decigrams = total_bullets * 133

# Round to the nearest gram
total_grams = (total_decigrams + 5) // 10  # +5 for nearest-integer rounding

# Split into kilograms and grams
kilograms = total_grams // 1000
grams = total_grams % 1000

print(f"Mass is {kilograms} kilograms and {grams} grams.")