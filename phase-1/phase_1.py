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
    print("NEW LIFTING EQUIPMENT")
    equipment_id = int(input("Please provide the identifier for the lifting equipment: "))
    equipment_brand = input("Please provide the lifting equipment's brand name: ")
    equipment_model = input("Please specify the model's name of the lifting apparatus: ")
    equipment_type = input("Please specify the equipment type: ")
    equipment_description = input("Please enter the lifting equipment's description here: ")
    equipment_price_before_vat = int(input("Please input the cost of the lifting equipment, excluding VAT: "))
    if (equipment_price_before_vat < 0): # Verifies whether the provided price is negative. If the result is negative, an error message is displayed on the screen.
        equipment_price_before_vat = 0   # Default value used to either confirm or indicate that the information entered is incorrect.
        print("Error, negative pricing are prohibited ")
    equipment_price_after_vat = equipment_price_before_vat + equipment_price_before_vat*(VAT/100)
    equipment_units_in_stock = int(input("Please specify the number of lifting equipment units that are currently in stock: "))
    if (equipment_units_in_stock < 0): # Verifies whether the provided number is negative. If the result is negative, an error message is displayed on the screen.
        equipment_units_in_stock = 0   # Default value used to either confirm or indicate that the information entered is incorrect.
        print("Error, negative stock numbers are not permitted")

elif option==2:
    print("NEW CUSTOMER")

elif option==3:
    print("NEW LIFTING EQUIPMENT RENTAL")

elif option==4:
    print("EXIT")
