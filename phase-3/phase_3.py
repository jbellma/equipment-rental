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

def read_brand(message, allowedBrands):
    '''
    Function that asks for a brand name and verifies until it is accurate.
    '''
    while True:
        brand_type = input(message)
        brand_type = brand_type.lower()
        for brand in allowedBrands:
            if brand_type == brand:
                return brand_type
        print("Error, brand not allowed, insert a valid brand.")


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

def read_letter_nid(num_id):
    '''
    A NID-requesting function that establishes its validity.
    '''
    raw_nid = num_id
    number = int(raw_nid [:-1]) # Separating the letter from the corresponding number.
    sequence = "TRWAGMYFPDXBNJZSQVHLCKE"
    correct_letter = sequence[number%23] # By dividing the number on your identity card by 23, you may determine the letter of your NID. This division leaves you with a remainder, and each one of them has a letter assigned to it.
    if correct_letter == raw_nid.upper() [-1]:
        return True
    else:
        print(f"Error, {raw_nid} is not valid.")
        return False

def nid_verification(message, list_customers_nid):
    '''
    Function that confirms the legitimacy of a NID number
    '''
    while True:
        nid = input(message)
        nid = nid.upper()
        try:
            if (read_length_nid(nid) == True) and (read_eight_first_digits_nid(nid) == True) and (read_letter_nid(nid)== True):
                if nid not in list_customers_nid:
                    list_customers_nid.append(nid)
                    number_nid = int(nid[:-1])
                    list_customers_nid_ordered_no_letter.append(number_nid)
                    for id in range(len(list_customers_nid_ordered_no_letter)):
                        for id_pos in range(len(list_customers_nid_ordered_no_letter) - 1):
                            if list_customers_nid_ordered_no_letter[id_pos] > list_customers_nid_ordered_no_letter[id_pos + 1]:
                                list_customers_nid_ordered_no_letter[id_pos + 1], list_customers_nid_ordered_no_letter[id_pos] = list_customers_nid_ordered_no_letter[id_pos], list_customers_nid_ordered_no_letter[id_pos + 1]
                    return nid
                else:
                    print("Error, that NID already exists, enter another NID.")
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Please, insert a valid NID.")

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
    Show menu.
    '''
    print_menu()
    option = read_integer("Please select an option (1-4): ")
    while option < 1 or option > 4:
        print("There are four choices, numbered one through four.")
        print("\n\n")
        print_menu()
        option = read_integer("Please select an option (1-4): ")
    return (option)

def print_dictionary_equipment(dictionary):
    '''
    Function that prints dictionary equipment.
    '''
    for key in dictionary:
        print(key, ":", dictionary[key])

def print_list_equipment(list_equipment):
    '''
    Function that prints list of equipment.
    '''
    if len(list_equipment) == 0:
        print("There are no items to display yet...")
    else:
        for header in list_equipment[0].keys():
            print(header.upper().ljust(20), end = '\t')
        print("\n*************************************************************",end = "")
        print("****************************************************************",end = "")
        print("***********************************************************************************")
        for equipment in list_equipment:
            for value in equipment.values():
                print(str(value).ljust(25), end ='\t')
            print()

def register_equipment (num_id):
    '''
    Function equipment registration.
    '''

    equipment = {} # Dictionary equipment

    equipment['equipment_id'] = num_id + 1   # We assign the following integer
    equipment['equipment_brand'] = read_brand("Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): ", allowedBrands)
    equipment['equipment_model'] = convert_lowercase("Please specify the model's name of the lifting apparatus: ")
    equipment['equipment_type'] = convert_lowercase("Please specify the equipment type: ")
    equipment['equipment_description'] = convert_lowercase("Please enter the lifting equipment's description here: ")
    equipment['equipment_price_before_vat'] = read_float("Please input the cost of the lifting equipment, excluding VAT: ")
    equipment['equipment_price_after_vat'] = equipment['equipment_price_before_vat'] + equipment['equipment_price_before_vat']*(VAT/100)
    equipment['equipment_units_in_stock'] = read_integer("Please specify the number of lifting equipment units that are currently in stock: ")

    list_equipment.append(equipment)
    list_equipment_id.append(equipment['equipment_id'])

    print("\n")
    print_dictionary_equipment(equipment)

    return equipment['equipment_id']


def print_dictionary_customer(dictionary):
    '''
    Function that prints customer dictionary.
    '''
    for key in dictionary:
        print(key, ":", dictionary[key])

def print_list_customers(list_customers):
    '''
    Function that prints list of customers.
    '''
    for header in list_customers[0].keys():
        print(header.upper().ljust(30), end = '\t')
    print("\n*************************************************************",end = "")
    print("****************************************************************",end = "")
    print("***********************************************************************************")
    for customer in list_customers:
        for value in customer.values():
            print(str(value).ljust(30), end ='\t')
        print()

def register_customer():
    '''
    Function that registers customer information.
    '''

    customer = {} # Dictionary customer

    customer['name'] = convert_lowercase("Enter new customer's name: ")
    customer['first_surname'] = convert_lowercase("Fill in new customer's first surname: ")
    customer['second_surname'] = convert_lowercase("Complete new customer's second surname: ")
    customer['nid'] = nid_verification("Enter new customer's NID with a 'NNNNNNNNL' format: ", list_customers_nid)
    customer['phone'] = read_phone_number("Type new customer's phone number with a 'NNNNNNNNN' format: ")
    customer['address'] = convert_lowercase("Fill in new customer's address: ")

    list_customers.append(customer)

    print("\n")
    print_dictionary_customer(customer)

def new_list_customers_ordered(list_customers_nid_ordered_no_letter, list_customers, list_customers_nid_ordered, list_customers_ordered):
    '''
    Function that rearranges list of customers in order.
    '''
    for number in list_customers_nid_ordered_no_letter:
        for customer in list_customers:
            sequence = 'TRWAGMYFPDXBNJZSQVHLCKE'
            string = str(number).zfill(8)
            string = string + sequence[number%23]
            if string == customer['nid']:
                list_customers_ordered.append(customer)
                list_customers_nid_ordered.append(customer['nid'])
    return list_customers_ordered

def print_new_list_customers_ordered(ordered_list):
    '''
    Function that prints n ordered list of customers.
    '''
    for header in ordered_list[0].keys():
        print(header.upper().ljust(30), end = '\t')
    print("\n*************************************************************",end = "")
    print("****************************************************************",end = "")
    print("***************************************************")
    for customer in ordered_list:
        for value in customer.values():
            print(value.ljust(30), end ='\t')
        print()




###########################

    # Main Program

###########################

allowedBrands = ("palfinger", "kone", "schmalz")

list_equipment = []
list_equipment_id = []
list_customers = []
list_customers_nid = []
list_customers_nid_ordered_no_letter = []
list_customers_nid_ordered = []
list_customers_ordered = []
list_equipment_rentals = []


# Constants
VAT = 16  # Consistently 16% VAT on all items
num_id = 0 # When the program launches, it begins by numbering  from number 1

running = True # Determines whether we proceed through the menu or the user has selected option 4
while running:
    option = show_menu() # Prints menu
    if option == 1: # New lifting equipment registration
        print("\n")
        print_list_equipment(list_equipment)
        print("\n")
        print("*** ADD NEW LIFTING EQUIPMENT DATA: ***")
        num_id = register_equipment(num_id)

    elif option == 2: # New customer data registration
        print("\n")
        print("*** ADD NEW CUSTOMER DATA: ***")
        register_customer()
        print("\n")
        new_list_customers_ordered(list_customers_nid_ordered_no_letter, list_customers, list_customers_nid_ordered, list_customers_ordered)
        print_new_list_customers_ordered(list_customers_ordered)





    elif option == 3:
        print("\n\n\n")



    elif option == 4:
        running = False

print("END")
