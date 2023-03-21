# Constants

###########################

    # Functions

###########################



def print_menu():
    print("\n\n\n")
    print("******** MAIN MENU ********")
    print("1. New Lifting Equipment")
    print("2. New Customer")
    print("3. New Lifting Equipment Rental")
    print("4. Exit")

    # It prompts the user to choose one of the Main Menu choices between one and four to be executed.
    option = read_whole_positive("Please select an option (1-4): ")

    # It displays an error message if the option that was entered is invalid.
    while option<1 or option>4:
        print("\n\n\n")
        print("Error: invalid option")
        option = read_whole_positive("Please select an option (1-4): ")
    return option

def read_whole_positive(message):
    while True:
        entry = input(message)
    try:
        entry = int(entry)
        if entry<0:
            raise ValueError
        return entry
    except ValueError:
        print("Error, please enter a whole positive number")


def insert_new_lifting_equipment():
    equipment_id = int(input("Please provide the identifier for the lifting equipment: "))
    equipment_brand = input("Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): ")
    equipment_model = input("Please specify the model's name of the lifting apparatus: ")
    equipment_type = input("Please specify the equipment type: ")
    equipment_description = input("Please enter the lifting equipment's description here: ")
    equipment_price_before_vat = int(input("Please input the cost of the lifting equipment, excluding VAT: "))
    equipment_price_after_vat = equipment_price_before_vat + equipment_price_before_vat*(VAT/100)
    equipment_units_in_stock = int(input("Please specify the number of lifting equipment units that are currently in stock: "))
    return (equipment_id, equipment_brand, equipment_model, equipment_type, equipment_description, equipment_price_after_vat, equipment_units_in_stock )

# Prints the saved data.
def print_new_lifting_equipment():
    print ("\n\n\n")
    print("*** EQUIPMENT DATA ***")
    print("ID: ", equipment_id)
    print("Brand: ", equipment_brand)
    print("Model: ", equipment_model)
    print("Type: ", equipment_type)
    print("Description: ", equipment_description)
    print("Price before VAT: ", equipment_price_before_vat)
    print("Price after VAT: ", equipment_price_after_vat)

def insert_new_customer():

def print_new_customer():






###########################

    # Main Program

###########################

# Constants
VAT = 16  # consistently 16% VAT on all items

num_ID = 0

option = print_menu()
while option !=4:

    if option==1:
        print("\n\n\n")
        print("NEW LIFTING EQUIPMENT")
        insert_new_lifting_equipment()
        print_new_lifting_equipment()

    elif option==2:
        print("\n\n\n")
        print("NEW CUSTOMER")

    elif option==3:
        print("\n\n\n")
        print("NEW LIFTING EQUIPMENT RENTAL")

    option = print_menu()

print("END")
