# Scientific Calculator System
# Combines Physics, Chemistry, and Mathematics calculations

import math


# ---------------- PHYSICS FUNCTIONS ----------------

def velocity():
    try:
      d = float(input("Enter  distance (meters):"))
      t = float(input("Enter time(seconds):"))
      v = round(d / t, 2)
      print("Velocity =", v, "m/s")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def force():
    try:
        m = float(input("Enter mass (kg): "))
        a = float(input("Enter acceleration (m/s^2): "))
        f = round(m * a, 2)
        print("Force =", f, "Newtons")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def kinetic_energy():
    try:
        m = float(input("Enter mass (kg): "))
        v = float(input("Enter velocity (m/s): "))
        ke = round(0.5 * m * v**2, 2)
        print("Kinetic Energy =", ke, "Joules")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# ---------------- CHEMISTRY FUNCTIONS ----------------

def moles():
    try:
        mass = float(input("Enter mass (grams): "))
        molar_mass = float(input("Enter molar mass (g/mol): "))
        n = round(mass / molar_mass, 2)
        print("Number of moles =", n, "mol")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def molarity():
    try:
        mol = float(input("Enter moles: "))
        volume = float(input("Enter volume (liters): "))
        M = round(mol / volume, 2)
        print("Molarity =", M, "mol/L")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def dilution():
    try:
        M1 = float(input("Enter initial molarity (M1): "))
        V1 = float(input("Enter initial volume (V1): "))
        V2 = float(input("Enter final volume (V2): "))
        M2 = round((M1 * V1) / V2, 2)
        print("Final molarity =", M2, "Mol/L")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# ---------------- MATHEMATICS FUNCTIONS ----------------

def quadratic():
    try:
        a = round(float(input("Enter a: ")), 2)
        b = round(float(input("Enter b: ")), 2)
        c = round(float(input("Enter c: ")), 2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    

    d = b**2 - 4*a*c

    if d >= 0:
        x1 = round((-b + math.sqrt(d)) / (2*a), 2)
        x2 = round((-b - math.sqrt(d)) / (2*a), 2)
        print("Solutions:", x1, "and", x2)
    else:
        print("No real solutions")


def circle_area():
    try:
        r = float(input("Enter radius: "))
        area = round(math.pi * r**2, 2)
        print("Area of circle =", area)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def pythagoras():
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = round(math.sqrt(a**2 + b**2), 2)
        print("Hypotenuse =", c)
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# ---------------- MENUS ----------------

def physics_menu():
    print("\nPhysics Calculator")
    print("1. Velocity")
    print("2. Force")
    print("3. Kinetic Energy")

    choice = input("Choose option: ")

    if choice == "1":
        velocity()
    elif choice == "2":
        force()
    elif choice == "3":
        kinetic_energy()


def chemistry_menu():
    print("\nChemistry Calculator")
    print("1. Moles")
    print("2. Molarity")
    print("3. Dilution")

    choice = input("Choose option: ")

    if choice == "1":
        moles()
    elif choice == "2":
        molarity()
    elif choice == "3":
        dilution()


def math_menu():
    print("\nMathematics Calculator")
    print("1. Quadratic Equation")
    print("2. Area of Circle")
    print("3. Pythagorean Theorem")

    choice = input("Choose option: ")

    if choice == "1":
        quadratic()
    elif choice == "2":
        circle_area()
    elif choice == "3":
        pythagoras()


# ---------------- MAIN PROGRAM ----------------

def main():

    while True:
      

        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Physics Calculations")
        print("2. Chemistry Calculations")
        print("3. Mathematics Calculations")
        print("4. Exit")
        
        
        
        

        choice = input("Choose a category: ")

        if choice == "1":
            physics_menu()

        elif choice == "2":
            chemistry_menu()

        elif choice == "3":
            math_menu()

        elif choice == "4":
            print("Program closed.")
            

        else:
            print("Invalid choice")




main()