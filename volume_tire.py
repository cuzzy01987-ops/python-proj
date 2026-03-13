# program that accept user input that describe a tire and calculates the volume of the tire
import math
from datetime import date, datetime
today = date.today()
price1 = 0
price2 = 0
price3 = 0


width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))



if width <= 0 or aspect_ratio <= 0 or diameter <= 0:
    print("Invalid input. Please enter positive values for width, aspect ratio, and diameter.")
# calculate the price of the tire based on the dimensions
price = width * aspect_ratio * diameter
if price < 1000:
    price1 = 550
    print("The price of the tire is $550.")
elif price < 2000:
    price2 = 750
    print("The price of the tire is $750.")
elif price < 3000:
    price3 = 950
    print("The price of the tire is $950.")
else:
    price4 = 2500
    print(f"The price of the tire is ${price4}.")
    

volume = (math.pi * (width **2) * aspect_ratio * (width*aspect_ratio + 2540 * diameter)/10000000000)
print(f"The volume of the tire is {volume:.2f} liters.")

buy = input("Do you want to buy the tire with the above dimensions? (yes/no): ")
if buy.lower() == "yes":
    phone_number = int(input("Enter your phone number: "))
else:
    print("Thank you for using the tire volume calculator. Have a great day!")




with open("volumes.txt", "at") as file:
        if phone_number:
            print(f"{today}, {width:.2f}, {aspect_ratio:.2f}, {diameter:.2f}, {volume:.2f}, {phone_number}", file=file)
        else:
          print(f"{today}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}", file=file)
             
print(f"{today}, {width} mm , {aspect_ratio}%, {diameter}, {volume:.2f} liters")
    


 



