# program that solve for housing in campus area

import csv
import datetime 

today = datetime.date.today()

House_ID = 0
House_Name = 1
House_Price = 2

def houses_available():
    with open("campus_housing.csv", "r") as file:
        houses = []
        reader = csv.reader(file)
        next(reader)
        for lines in reader:
           
            ID = (lines[House_ID])
            Name = lines[House_Name]
            Price = (lines[House_Price])
            house = {"House_ID": ID, "House_Name": Name, "House_Price": Price}
            houses.append(house)
    return houses
def booking_house(houses_available):
    choose = input("Do you want to book a house? (yes/no)")
    if choose == "yes":
       
        house_id = input("Enter the ID of the house you want to book:")
        for house in houses_available:
            if house["House_ID"] == house_id:
                
                print(f"you have booked {house['House_Name']} for ${house['House_Price']} on {today}")
                return house
            
    print("House not found.")
    return None
def rent_reminder(booking_house):
    
        if today >= today.replace(day=1):
            return f"Remember to pay rent for {booking_house["House_Name"]} today!"
            
          
def Landlord_account(Name, ID,phone_number,Email):
    
    Landlord_account = {"Name": Name, "ID": ID, "phone_number": phone_number, "Email": Email}
    return Landlord_account

def Tendant_account(Name,ID,phone_number,Email):
    Tendant_acc = {"Name":Name, "ID":ID, "phone_number":phone_number, "Email":Email}
    return Tendant_acc


def main ():
    print("Welcome to the campus housing application!")
    
    # house = houses_available()
    # print(f"these are the houses available : {house}")
    
    # booking_houses = booking_house(houses_available())
    # The line `print(booking_houses)` is attempting to print the value of the variable
    # `booking_houses`. However, there seems to be an issue in the code where `booking_houses` is
    # being used before it is defined. This will result in an error when the code is executed.
    # print(booking_houses)
    
    # pay_rent = rent_reminder(booking_houses)
    # print( pay_rent)
    # ?landlord = Landlord_account("John","1233433", "555-1234", "john@example.com")
    #print(landlord)
    
    
    #Tendant = Tendant_account("John","1233433", "555-1234", "john@example.com")
    #print(Tendant)
    while True:
        print("1. View Available Houses")
        print("2.Book a house")
        
        print("3.Exit")
        
        choice = input("Enter your choice (1-3:)")
        
        if choice == "1":
            houses_available()
            
        elif choice == "2":
            booking_house()
        elif choice == "3":
            print('Thank you for using the campus housing application Goodbaye!')
            break



main()