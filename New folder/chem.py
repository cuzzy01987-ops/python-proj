from formula import parse_formula
# program that will calculate the molar mass and number of moles for a given quantity

def main():
        #ask user for chemical formula
        chemical_formular = input("Enter the chemical formula:")

        # ask the user for the amount of the compound in grams
        compound_grams = input("Enter the amount of the compound(grams):")

        periodic_table_dict = make_periodic_table()
        symbols_quantity_list = parse_formula(chemical_formular,periodic_table_dict)
        molar_mass = compute_molar_mass(symbols_quantity_list,periodic_table)
        number_Of_molar = compound_grams / molar_mass

        print(f"molar mass is:{number_Of_molar} g/mol")


    
        
    

    
        

# compute and display molar mass
def make_periodic_table(none):
        periodic_table_dict = {
                "AC": ["Actinium",227],
                "Ag": ["Silver",107.8682],
                "Al": ["Aluminium",26.9815386],
                "Ar": ["Argon",39.948],
                "As": ["Arsenic",74.9216],
                "At" : ["Astatine",210],
                "Au": ["Gold",196.966569],
                "B": ["Boron",10.811],
                "Ba": ["Barium",137.327],
                "Be": ["Beryllium",9.012282],
                "Bi": ["Bismuth",74.9815386],
                "Br": ["Bromine",74.9815386],
                "C": ["Carbon",74.9815386],
                "Ca": ["Calcium",74.9815386],
                "Cd": ["Cadmium",74.9815386],
                "Ce": ["Cerium",74.9815386],
                "Cl": ["Chlorine",74.9815386],
                "Co": ["Cobalt",74.9815386],
                "Cr": ["Chromium",74.9815386],
                "Cs": ["Cesium",74.9815386],
                "Cu": ["Copper",74.9815386],
                "Dy": ["Dysprosium",74.9815386],
                "Er": ["Erbium",74.9815386],
                "Eu": ["Europium",74.9815386],
                "F": ["Fluorine",74.9815386],
                "Fe": ["Iron",74.9815386],
                "Fr": ["Francium",74.9815386],
                "Ga": ["Gallium",74.9815386],
                "Gd": ["Gadolinium",74.9815386],
                "Ge": ["Germanium",74.9815386],
                "H": ["Hydrogen",74.9815386],
                "He": ["Helium",178.49],
                "Hf": ["Hafnium",164.90447],
                "Hg": ["Mercury",200.59],
                "Ho": ["Iodine",126.90447],
                "In": ["Inium",114.818],
                "Ir": ["Iridium",192.217],
                "K": ["Potassium",39.0983],
                "Kr": ["Krypton",83.798],
                "Li": ["Lanthanum",138.9815386],
                "La": ["lithium",6.941],
                "Lu": ["Lutetium",174.9815386],
                "Mg": ["Mgnisium",24.305],
                "Mn": ["Manganese",54.938045],
                "Mo": ["Molybdenum",95.98],
                "N": ["Nitrogen",14.0067],
                "Na": ["Sodium",22.98976928],
                "Nb": ["Niobium",92.90638],
                "Nd": ["Neodymium",144.242],
                "Ne": ["Neon",20.1797],
                "Ni": ["Nickel",58.6934],
                "Np": ["Neptunium",237],
                "O": ["Oxygen",15.994],
                "Os": ["Osimium",190.23],
                "P": ["Phoshorus",30.973762],
                "Pa": ["Protactinium",231.03588],
                "Pb": ["Lead",20.72],
                "Pd": ["Palladium",106.42],
                "Pm": ["Promethium",145],
                "Po": ["Polonium",209],
                "Pt": ["Praseodymium",140.90765],
                "Pu": ["Plutominium",244],
                "Ra": ["Radium",226],
                "Rh": ["Rhodium",102.9055],
                "Re": ["Rhenuim",186.207],
                "Rb": ["Rubidium",102.9055],
                "Rh": ["Randon",222],
                "Rn": ["Radon",74.9815386],
                "Ru": ["Ruthenium",102.07],
                "S": ["Sulfur",32.065],
                "Sb": ["Antimony",121.76],
                "Sc": ["Scandium",44.955912],
                "Se": ["Selenium",78.96],
                "Si": ["Silicon",28.0855],
                "Sm": ["Samarium",150.36],
                "Sn": ["Tin",118.71],
                "Ta": ["Tantalum",180.94788],
                "Sr": ["Strontium",87.62],
                "Tb": ["Terbium",158.926],
                "Tc": ["Technetium",98],
                "Te": ["Tellurim",127.6],
                "Th": ["Throrium",232.03806],
                "Ti": ["Titanium",47.867],
                "Tl": ["Thallium",168.93421],
                "Tm": ["Thulium",204.465],
                "U": ["Uranium",238.02891],
                "V": ["Vanadium",50.9415],
                "W": ["Tungsten",183.84],
                "Xe": ["Xenon",131.293],
                "Y": ["Ytterbrium",173.054],
                "Yb": ["Ytterbim",88.90585],
                "Zn": ["Zinc",65.38],
                "Zr": ["Zirconium",91.224],

    }    
        
        return periodic_table_dict



      
                 


def compute_molar_mass(symbols_quantity_list,periodic_table_dict):
        total_mas = 00
        for symbol, quantity in symbols_quantity_list:
                element_data = periodic_table_dict[symbol][1]
                total_mas += element_data * quantity
        return total_mas
       
                

        
        

if __name__=="__main__":
        main()
