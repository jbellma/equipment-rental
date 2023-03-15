# Constants
VAT = 16  # consistently 16% VAT on all items

# Prints Main Menu
print("\n\n\n")
print("******** MAIN MENU ********")
print("1. New Lifting Equipment")
print("2. New Customer")
print("3. New Lifting Equipment Rental")
print("4. Exit")

# It prompts the user to choose one of the Main Menu choices between one and four to be executed.
option = int(input("Please select an option (1-4): "))

# It displays an error message if the option that was entered is invalid.
if option<1 or option>4:
    print("Error: invalid option")
# Prints the name of the option to run and calls the function it references if the inserted option is valid.
elif option==1:
    print("New Lifting Equipment")
    equipment_id = int(input("Please provide the identifier for the lifting equipment: "))
    equipment_brand = int(input("Please provide the lifting equipment's brand name: "))
    equipment_model = int(input("Please specify the model's name of the lifting apparatus: "))
    equipment_type = int(input("Please specify the equipment type: "))
    equipment_description = int(input("Please enter the lifting equipment's description here: "))
    equipment_price_before_vat = int(input("Please input the cost of the lifting equipment, excluding VAT: "))
    equipment_units_in_stock = int(input("Please specify the number of lifting equipment units that are currently in stock: "))
elif option==2:
    print("New Customer")
elif option==3:
    print("New Lifting Equipment")
elif option==4:
    print("Exit")
