###########################

    # Functions

###########################

def read_integer(message):
    '''
    Function that requests an integer and verifies it by making exceptions.
    '''
    while True:
        entry = input(message)
        try:
            entry = int(entry)
            return entry
        except ValueError:
            print("Error, expecting a whole number! Please enter a whole number: ")

def read_whole_positive(message):
    '''
    An integer-requesting function that verifies it using exceptions till it is accurate.
    '''
    while True:
        entry = input(message)
        try:
            entry = int(entry)
            if entry<0:
                raise ValueError
            return entry
        except ValueError:
            print("Error, please enter a positive integer")

def read_float(message):
    '''
    Function that asks for a real number and verifies it using exceptions until it is accurate.
    '''
    while True:
        entry = input(message)
        try:
            float_number = float(entry)
            return float_number
        except:
            print("Error, please enter a real number")

def read_real_positive(message):
   '''
    Function that asks for a positive real number and verifies it using exceptions until it is accurate.
   '''
   while True:
       entry = input(message)
       try:
           entry = float(entry)
           if entry < 0:
               raise ValueError
           return entry
       except ValueError:
           print ("Error, please enter a real positive number: ")

def read_brand(message):
    '''
    Function that asks for a brand name and verifies until it is accurate.
    '''
    brand_type = input(message)
    while brand_type != "PALFINGER" and brand_type !="KONE" and brand_type !="SCHMALZ":
        print("Error, brand not allowed")
        brand_type = input(message)
    return brand_type

def read_length_nid(length_nid):
    '''
    Function
    '''
    if len(length_nid) == 9:
        return True
    else:
        print("Error, please enter a 9-character NID.")
        return False

def read_eight_first_digits_nid(digit_nid):
    '''
    Function
    '''
    nid = digit_nid
    raw_input_values = nid[:-1]
    numbers = '1234567890'
    for value in raw_input_values:
        if value not in numbers:
            print("Error, there must be numbers in the first 8 characters. Please provide a valid NID.")
            return False
    return True

def read_letter_nid(message):
    '''
    A NID-requesting function that establishes its validity.
    '''
    while True:
        raw_nid = input(message)
        number = int(raw_nid [:-1]) # Separating the letter from the corresponding number.
        sequence = "TRWAGMYFPDXBNJZSQVHLCKE"
        correct_letter = sequence[number%23] # By dividing the number on your identity card by 23, you may determine the letter of your NID. This division leaves you with a remainder, and each one of them has a letter assigned to it.
        try:
            if correct_letter != raw_nid [-1]:
                raise ValueError
            else:
                return raw_nid
        except ValueError:
            print("Error, please enter a valid NID")

def read_phone_number(message):
    '''
    Function that confirms the legitimacy of a phone number.
    '''
    while True:
        entry = read_whole_positive(message)
        try:
            if len(str(entry)) != 9:
                raise ValueError
            else:
                return entry
        except ValueError:
            print("Error, enter a nine-digit phone number instead, please: ")

def convert_lowercase(message):
    '''
    Function
    '''
    string = input(message)
    string = string.lower()
    return string

def print_menu():
    '''
    Prints menu.
    '''
    print("\n\n\n")
    print("******** MAIN MENU ********")
    print("1. New Lifting Equipment")
    print("2. New Customer")
    print("3. New Lifting Equipment Rental")
    print("4. Exit")

def show_menu():
    '''
    Prints menu.
    '''
    print_menu()
    option = read_whole_positive("Please select an option (1-4): ")
    while option<1 or option>4:
        print("There are four choices, numbered one through four.")
        print("\n\n\n")
        print_menu()
        option = read_whole_positive("Please select an option (1-4): ")
    return option

def insert_new_lifting_equipment(equipment_id):
    '''
    Function that requests the new lifting equipment's data.
    '''
    equipment_id =  equipment_id + 1
    equipment_brand = read_brand("Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): ")
    equipment_model = input("Please specify the model's name of the lifting apparatus: ")
    equipment_type = input("Please specify the equipment type: ")
    equipment_description = input("Please enter the lifting equipment's description here: ")
    equipment_price_before_vat = read_real_positive("Please input the cost of the lifting equipment, excluding VAT: ")
    equipment_price_after_vat = equipment_price_before_vat + equipment_price_before_vat*(VAT/100)
    equipment_units_in_stock = read_whole_positive("Please specify the number of lifting equipment units that are currently in stock: ")
    return (equipment_id, equipment_brand, equipment_model, equipment_type, equipment_description, equipment_price_after_vat, equipment_price_after_vat, equipment_units_in_stock)


def print_new_lifting_equipment(equipment_id, equipment_brand, equipment_model, equipment_type, equipment_description, equipment_price_before_vat, equipment_price_after_vat, equipment_units_in_stock):
    '''
    Function that prints the new lifting equipment's stored data.
    '''
    print ("\n\n\n")
    print("*** EQUIPMENT DATA ***")
    print("ID: ", equipment_id)
    print("Brand: ", equipment_brand)
    print("Model: ", equipment_model)
    print("Type: ", equipment_type)
    print("Description: ", equipment_description)
    print("Price before VAT: ", equipment_price_before_vat)
    print("Price after VAT: ", equipment_price_after_vat)
    print("Stock: ", equipment_units_in_stock)


def insert_new_customer():
    '''
    Function that requests the new client's data.
    '''
    name = input("Enter new customer's name: ")
    first_surname = input("Fill in new customer's first surname: ")
    second_surname = input("Complete new customer's second surname: ")
    nid = read_nid("Enter new customer's NID with a 'NNNNNNNNL' format: ")
    phone = read_phone_number("Type new customer's phone number with a 'NNNNNNNNN' format: ")
    address = input("Fill in new customer's address: ")
    return (name, first_surname, second_surname, nid, phone, address)


def print_new_customer(name, first_surname, second_surname, nid, phone, address):
    '''
    Function that prints the new customer's stored data.
    '''
    print ("\n\n\n")
    print ("Name: ", name)
    print ("First Surname: ", first_surname)
    print ("Second Surname: ", second_surname)
    print ("NID: ", nid)
    print ("Address: ", address)



###########################

    # Main Program

###########################

allowedBrands = ("palfinger", "kone", "schmalz")

list_equipment = []
list_equipment_id = []
list_customers = []
list_customers_nid = []


# Constants
VAT = 16  # consistently 16% VAT on all items
num_ID = 0

option = print_menu()
while option !=4: # Depending on the selection entered, different actions are taken as long as the exit option has not been selected.
    if option == 1:
        print("\n\n\n")
        print("NEW LIFTING EQUIPMENT")
        (iden, bra, mod, typ, des, b_vat, af_vat, sto) = insert_new_lifting_equipment(num_ID)
        print_new_lifting_equipment(iden, bra, mod, typ, des, b_vat, af_vat, sto)

        num_ID = num_ID + 1

    elif option == 2 :
        print("\n\n\n")
        print("NEW CUSTOMER")
        (name, first_sur, second_sur, nid, phon, addre) = insert_new_customer()
        print_new_customer(name, first_sur, second_sur, nid, phon, addre)

    elif option == 3:
        print("\n\n\n")
        print("NEW LIFTING EQUIPMENT RENTAL")

    option = print_menu()

print("END")
