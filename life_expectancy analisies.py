# life expectancy analisies

# tracking variables
overall_min = 999
overall_min_country = ""
overall_min_year = ""

overall_max = -1
overall_max_country = ""
overall_max_year = ""

# ask user for the year of interest

year_of_interest = input("Enter the of interest:")

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
        parts = line.split(",")
        
        
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        
         # Update overall min and max
        
        if overall_min > life_expectancy:
            overall_min = life_expectancy
            overall_min_country = country
            overall_min_year = year
            
        if overall_max > life_expectancy:
            overall_max = life_expectancy
            overall_max_country = country
            overall_max_year = year 
            
            
       # If this row matches the user's year of interest
       
        if year == life_expectancy:
           year_sum += life_expectancy
           year_count += 1
           
        if life_expectancy < year_min:
            year_min = life_expectancy
            year_min_country = country
            
        if life_expectancy > year_min:
            year_max = life_expectancy
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
      
        
    