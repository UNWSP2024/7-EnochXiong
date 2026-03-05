def main():
    rainfall = []

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    for i in range(12):
        amount = float(input(f"Enter the total rainfall for {months[i]}: "))
        rainfall.append(amount)

    total_rainfall = sum(rainfall)

    average_rainfall = total_rainfall / 12

    highest = max(rainfall)
    lowest = min(rainfall)

    highest_month = months[rainfall.index(highest)]
    lowest_month = months[rainfall.index(lowest)]

    print("\nRainfall Report")
    print("----------------")
    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Highest rainfall: {highest:.2f} in {highest_month}")
    print(f"Lowest rainfall: {lowest:.2f} in {lowest_month}")

main()
