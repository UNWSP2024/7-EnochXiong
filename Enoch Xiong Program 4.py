import math

def get_coordinate(point_name):
    while True:
        try:
            print(f"Enter coordinates for {point_name}:")
            x = float(input("Enter x value: "))
            y = float(input("Enter y value: "))
            z = float(input("Enter z value: "))
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

def distance(coord1, coord2):

    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    return math.sqrt((x2 - x1) ** 2 +
                     (y2 - y1) ** 2 +
                     (z2 - z1) ** 2)

def main():
    try:
        coord1 = get_coordinate("Point 1")
        coord2 = get_coordinate("Point 2")

        dist = distance(coord1, coord2)

        print(f"Distance between the two points: {dist}")

    except Exception:
        print("An unexpected error occurred:")

if __name__ == "__main__":
    main()
