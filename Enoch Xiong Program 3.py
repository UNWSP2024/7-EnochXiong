def main():
    all_entered_values = []

    num_states = int(input("How many state records would you like to enter? "))

    for i in range(num_states):
        print(f"\nEntry #{i + 1}")
        year = int(input("Enter year: "))
        state = input("Enter state name: ")
        population = int(input("Enter population: "))

        all_entered_values.append([year, state, population])

    total_population = int(input("\nEnter a year to calculate total population: "))

    sum_population_for_year(all_entered_values, total_population)

def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0

    for record in all_entered_values:
        year, state, population = record

        if year == year_to_sum:
            total_population += population

    print(f"\nTotal population for {year_to_sum}: {total_population}")

if __name__ == '__main__':
    main()
