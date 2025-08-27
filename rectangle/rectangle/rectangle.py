def rectangle_metrics():
    # Ask the user for base and height
    try:
        base = float(input("Enter the rectangle base: "))
        height = float(input("Enter the rectangle height: "))
    except ValueError:
        # Handle the case where conversion to float fails
        print("Invalid input. Please enter numeric values for base and height.")
        return

    # Validate positive dimensions
    if base <= 0 or height <= 0:
        print("Base and height must be greater than zero.")
        return

    # Calculate the area and perimeter
    area = base * height
    perimeter = 2 * (base + height)

    # Print the results
    print(f"Area of the rectangle: {area:.4f}")
    print(f"Perimeter of the rectangle: {perimeter:.4f}")


if __name__ == "__main__":
    # Program entry point
    rectangle_metrics()
