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
        print("*****************************************************************",end = "")
        print("***************************************************************************")
        for equipment in list_equipment:
            for value in equipment.values():
                print(str(value).ljust(20), end ='\t')
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
    Function that prints an ordered list of customers.
    '''
    for header in ordered_list[0].keys():
        print(header.upper().ljust(30), end = '\t')
    print("\n*************************************************************",end = "")
    print("****************************************************************",end = "")
    print("***************************************************")
    for customer in ordered_list:
        for value in customer.values():
            print(str(value).ljust(30), end ='\t')
        print()

def show_rentals_data(list_customers_nid_ordered, list_equipment_id):
    '''
    Function that shows rental information.
    '''
    print("\n\n")
    print("NEW LIFTING EQUIPMENT RENTAL")
    print("\n")
    print("EQUIPMENT: ",end = '' )
    print(list_equipment_id)
    print("CUSTOMERS: ",end = '')
    print(list_customers_nid_ordered)

def read_register_identifier(message, list_equipment_id):
    '''
    Function that verifies equipment's existance.
    '''
    while True:
        rental_id = read_integer(message)
        if rental_id in list_equipment_id:
            return rental_id
        else:
            print(f"Error, the equipment must be registered in the system:: {list_equipment_id}. ")
            print("Enter an existing lifting equipment identifier. ")

def read_register_nid_customer(message,list_customers_nid_ordered):
    '''
    Function that verifies customers' existance.
    '''
    while True:
        rental_customer = input(message).upper()
        if rental_customer in list_customers_nid_ordered:
            return rental_customer
        else:
            print(f"Error, the customer must be registered in the system:: {list_customers_nid_ordered}. ")
            print("Enter an existing lifting equipment identifier. ")
    return

def format_date(message):
    '''
    Function that verifies date format.
    '''
    while True:
        entry = input(message)
        if len(entry) == 10:
            if entry[2] == "/" and entry[5] == "/":
                try:
                    int(entry[0:2])
                    int(entry[3:5])
                    int(entry[6:10])
                    return entry
                except ValueError:
                    print("Error, positive integers are needed.")
            else:
                print("Error, slashes are needed at positions two and five of the string.")
        else:
            print("Error, ten characters are needed for the date.")

def rental_equipment(list_equipment_id, list_customers_nid_ordered):
    '''
    Function that prints an ordered list of customers.
    '''

    rental_equipment = {}

    rental_equipment['equipment_id'] = read_register_identifier("Insert lifting equipment identifier: ",list_equipment_id)
    rental_equipment['NID_Customer'] = read_register_nid_customer("Enter the client's ID who rents the lifting equipment: ",list_customers_nid_ordered)
    rental_equipment['date_start'] = format_date("Please, enter a start date with a DD/MM/AAAA fromat: ")
    rental_equipment['date_end'] = format_date("Please, enter an end date with a DD/MM/AAAA fromat: ")
    rental_equipment['price'] = read_whole_positive("Please, enter rental service price: ")

    list_equipment_rentals.append(rental_equipment)

def print_dictionary_rentals(list_equipment_rentals):
    '''
    Function that stores, orders and prints all rentals.
    '''
    dictionary_rental = {}

    for equipment in list_equipment_rentals:
        newkey = equipment['equipment_id']
        dictionary_rental[newkey]=[]
    print("\n")

    for equipment in list_equipment_rentals:
        dictionary_rental[equipment['equipment_id']].append(equipment)

    print("################################################# RENTALS #####################################################")
    print("\n")

    for key, value in dictionary_rental.items():
        print(f"LIFTING EQUIPMENT: {key}")
        for rental in value:
            list_values = list(rental.values())
            print(list_values)

def equipment_not_in_use(list_equipment_id, list_equipment_rentals):
    '''
    Function that determines which equipment is still not in use
    '''
    list_used = []

    for equipment in list_equipment_rentals:
        list_used.append(equipment['equipment_id'])

    for id in list_equipment_id:
        if id not in list_used:
            print(f"No previous rentals have been made for the equipment {id}")


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
        list_customers_ordered = []

    elif option == 3:
        print("\n")
        print("*** ADD NEW LIFTING EQUIPMENT RENTAL: ***")

        if len(list_customers_nid) == 0 and len(list_equipment_id) == 0:
            print("Error, no liftinng equipment and no customers in the data base. Add equipment and clients.")
        if len(list_customers_nid) == 0:
            print("Error, no customers in the data base. Add clients.")
        if len(list_equipment_id) == 0:
            print("Error, no lifting equipment in the data base. Add lifting equipment.")
        else:
            show_rentals_data(list_customers_nid_ordered, list_equipment_id)
            rental_equipment(list_equipment_id, list_customers_nid_ordered)
            print_dictionary_rentals(list_equipment_rentals)
            print("\n")
            print("\n")
            equipment_not_in_use(list_equipment_id, list_equipment_rentals)

    elif option == 4:
        running = False

print("END")
