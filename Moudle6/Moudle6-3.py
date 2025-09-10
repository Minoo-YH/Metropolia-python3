GALLON_TO_LITTER= 3.785

def gallon_to_litter(gallon):
    return gallon * GALLON_TO_LITTER
def main():
    print("Gallon to  litter: ", gallon_to_litter(gallon))
    while True:
        try:
            g=float(input("Gallon to  litter: "))
        except ValueError:
            print("Gallon to  litter: ", gallon_to_litter)
            continue

        if g <= 0:
            print("Done.")
            break

        litter = gallon_to_litter(g)
        print("Gallon to  litter: ", gallon_to_litter(g))


if __name__ == "__main__":
    main()