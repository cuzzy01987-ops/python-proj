

# Life Expectancy Data Analysis Program
# No external libraries used



# Prepare tracking variables
overall_min = 9999
overall_min_country = ""
overall_min_year = ""

overall_max = -1
overall_max_country = ""
overall_max_year = ""

# Ask the user for the year of interest
year_of_interest = input("Enter the year of interest: ")

# Tracking variables for the chosen year
year_count = 0
year_sum = 0
year_min = 9999
year_min_country = ""
year_max = -1
year_max_country = ""

with open(r"C:\Users\User\Desktop\BYU_Classes\CSE110\CSE110\main_project\w6\life-expectancy.csv") as file:
    next(file)
    
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = parts[2]
        life = float(parts[3])

        # Update overall min and max
        if life < overall_min:
            overall_min = life
            overall_min_country = country
            overall_min_year = year

        if life > overall_max:
            overall_max = life
            overall_max_country = country
            overall_max_year = year
2
        # If this row matches the user's year of interest
         if year == year_of_interest:
                year_sum += life
               year_count += 1

       if life < year_min:
                year_min = life
                year_min_country = country
2
        if life > year_max:
                year_max = life
                year_max_country = country

# ------ Output Results ------

print()
print(f"The overall max life expectancy is: {overall_max} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min} from {overall_min_country} in {overall_min_year}")

print()

if year_count > 0:
    avg_life = year_sum / year_count

    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max}")
    print(f"The min life expectancy was in {year_min_country} with {year_min}")
else:
    print(f"No data found for the year {year_of_interest}.")
    



