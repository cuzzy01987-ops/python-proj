from pathlib import Path
import csv
import logging

# ----- Logging setup -----
logging.basicConfig(
    filename="life_expectancy.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----- Data file path -----
DATA_FILE = Path(r"C:\Users\User\Desktop\BYU_Classes\CSE110\CSE110\main_project\w6\life-expectancy.csv")

# ----- Get user input for year -----
def get_year():
    while True:
        try:
            return int(input("Enter year of interest: "))
        except ValueError:
            print("Please enter a valid year.")

# ----- Analyze life expectancy data -----
def analyze_data(year):
    overall_min = float("inf")
    overall_max = float("-inf")
    year_sum = 0
    year_count = 0
    year_min = float("inf")
    year_max = float("-inf")

    # Open CSV file
    with DATA_FILE.open() as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            country, code, data_year, life = row
            data_year = int(data_year)
            life = float(life)

            # Update overall min/max
            if life < overall_min:
                overall_min = life
                min_country = country
                min_year = data_year

            if life > overall_max:
                overall_max = life
                max_country = country
                max_year = data_year

            # Update year-specific stats
            if data_year == year:
                year_sum += life
                year_count += 1
                year_min = min(year_min, life)
                year_max = max(year_max, life)

    year_avg = year_sum / year_count if year_count > 0 else None

    return {
        "overall_min": (overall_min, min_country, min_year),
        "overall_max": (overall_max, max_country, max_year),
        "year_min": year_min if year_count > 0 else None,
        "year_max": year_max if year_count > 0 else None,
        "year_avg": year_avg,
    }

# ----- Display results -----
def display_results(results, year):
    overall_min, min_country, min_year = results["overall_min"]
    overall_max, max_country, max_year = results["overall_max"]
    year_min = results["year_min"]
    year_max = results["year_max"]
    year_avg = results["year_avg"]

    print(f"Overall Minimum Life Expectancy: {overall_min} in {min_country} ({min_year})")
    print(f"Overall Maximum Life Expectancy: {overall_max} in {max_country} ({max_year})")

    if year_avg is not None:
        print(f"\nFor the year {year}:")
        print(f"  Minimum Life Expectancy: {year_min}")
        print(f"  Maximum Life Expectancy: {year_max}")
        print(f"  Average Life Expectancy: {year_avg:.2f}")
    else:
        print(f"\nNo data available for the year {year}.")

# ----- Main function -----
def main():
    year = get_year()
    results = analyze_data(year)
    display_results(results, year)

if __name__ == "__main__":
    main()

Pass: Prinky

