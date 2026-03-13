# ask user for two integer numbers
num1 = int(input("Enter 1st integr:"))
num2 = int(input("Enter 2nd integer:"))

# use if_statment

if num1 > num2:
    print("The first number is greater")
else:
    print("The first number is not greater")
if num1 == num2:
     print("The  numbers are equal")
else:
     print("The numbers are not equal")
if num2 > num1:
    print("The second number is greater ")
else:
    print("The second number is not greater")
    
# ask the user for thier favorite animal

animal = input("Which is your favorite animal:")



if animal.lower() == "Dog":
    print("That's also my favorite too!")

else:
    print("That is not my favorite!")

