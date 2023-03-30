"""
Proyect status: COMPLETED

Author: Jose Bello

Phase 3: Storage and rental of products.

"""



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
    A positive integer-requesting function that verifies it using exceptions till it is accurate.
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

    Function that requests and checks if the brand entered corresponds to one of the allowed brands.
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
    Function that checks if the NID entered has nine characters.
    '''
    if len(length_nid) == 9:
        return True
    else:
        print("Error, please enter a 9-character NID.")
        return False

def read_eight_first_digits_nid(digit_nid):
    '''
    Function that checks if the first eight characters of the NID are numbers.
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
    Function that checks by means of the confirmation letter if the NID entered is valid or not.
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
    Function that validates if the NID entered complies with the necessary format. If not, requests an NID again.
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
    Function that verifies a phone number's validity by determining whether it has nine digits.
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
    Function that requests and converts input string data to lowercase.
    '''
    string = input(message)
    string = string.lower()
    return string

def print_menu():
    '''
    This function prints the program menu on the screen.
    INPUT: None.
    OUTPUT: None.
    EXCEPTIONS: It does not raise exceptions.
    '''
    print("\n\n\n")
    print("******** MAIN MENU ********")
    print("1. New Lifting Equipment")
    print("2. New Customer")
    print("3. New Lifting Equipment Rental")
    print("4. Exit")

def show_menu():
    '''
    This function displays the application menu on the screen. Asks to
    select and type an option, it verifies that the option is correct.
    Redisplays the menu if the selected option is incorrect.
    It returns the integer of the selected option if the option is correct.
    INPUT: None.
    OUTPUT: An integer of the selected option.
    EXCEPTIONS: It does not raise exceptions.
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
    Function that prints on the screen the key-value pairs of the dictionary with information about the equipment entered.
    '''
    for key in dictionary:
        print(key, ":", dictionary[key])

def print_list_equipment(list_equipment):
    '''
    Function that prints the list of equipment entered in tabulated form.
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
    Function that requests and checks the data entered for each registered
    device or equipment. It makes a keyboard request for the new equipment's info.
    It asks for the data, checks it, and if necessary, asks for it again.
    '''

    equipment = {} # The equipment data is saved in a dictionary.

    equipment['equipment_id'] = num_id + 1   # We assign the following integer.
    equipment['equipment_brand'] = read_brand("Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): ", allowedBrands)
    equipment['equipment_model'] = convert_lowercase("Please specify the model's name of the lifting apparatus: ")
    equipment['equipment_type'] = convert_lowercase("Please specify the equipment type: ")
    equipment['equipment_description'] = convert_lowercase("Please enter the lifting equipment's description here: ")
    equipment['equipment_price_before_vat'] = read_float("Please input the cost of the lifting equipment, excluding VAT: ")
    equipment['equipment_price_after_vat'] = equipment['equipment_price_before_vat'] + equipment['equipment_price_before_vat']*(VAT/100)
    equipment['equipment_units_in_stock'] = read_integer("Please specify the number of lifting equipment units that are currently in stock: ")

    list_equipment.append(equipment) # A list is created with the equipment entered.
    list_equipment_id.append(equipment['equipment_id']) # Only the equipment's identifiers are entered to produce a list.

    print("\n")
    print_dictionary_equipment(equipment)

    return equipment['equipment_id']


def print_dictionary_customer(dictionary):
    '''
    Function that prints on the screen the key-value pairs of the
    dictionary with information about customers.
    '''
    for key in dictionary:
        print(key, ":", dictionary[key])

def print_list_customers(list_customers):
    '''
    Function that prints the list of customers entered in tabulated form.
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
    Function that requests and checks the data entered for each registered customer.
    It makes a keyboard request for the new customer's info.
    It asks for the data, checks it, and if necessary, asks for it again.
    '''

    customer = {} # Cusotomer data is saved in a dictionary.

    customer['name'] = convert_lowercase("Enter new customer's name: ")
    customer['first_surname'] = convert_lowercase("Fill in new customer's first surname: ")
    customer['second_surname'] = convert_lowercase("Complete new customer's second surname: ")
    customer['nid'] = nid_verification("Enter new customer's NID with a 'NNNNNNNNL' format: ", list_customers_nid)
    customer['phone'] = read_phone_number("Type new customer's phone number with a 'NNNNNNNNN' format: ")
    customer['address'] = convert_lowercase("Fill in new customer's address: ")

    list_customers.append(customer) # A list is created with the registered customers.

    print("\n")
    print_dictionary_customer(customer)

def new_list_customers_ordered(list_customers_nid_ordered_no_letter, list_customers, list_customers_nid_ordered, list_customers_ordered):
    '''
    A feature that lists customers in ascending order.
    '''
    for number in list_customers_nid_ordered_no_letter:
        for customer in list_customers:
            sequence = 'TRWAGMYFPDXBNJZSQVHLCKE'
            string = str(number).zfill(8) # Makes sure the leading zeros print on the screen.
            string = string + sequence[number%23] # NID receives back again its letter.
            if string == customer['nid']: # The customer list is sorted in ORDERED form.
                list_customers_ordered.append(customer)
                list_customers_nid_ordered.append(customer['nid'])
    return list_customers_ordered

def print_new_list_customers_ordered(ordered_list):
    '''
    Prints the list of customers that was entered in tabular and ascending form.
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
    Function that prints on the screen the equipment and customers already registered in the system.
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
    Function that checks if the equipment is registered or not in the system.
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
    Function that checks if the customer is registered or not in the system.
    '''
    while True:
        rental_customer = input(message).upper()
        if rental_customer in list_customers_nid_ordered:
            return rental_customer
        else:
            print(f"Error, the customer must be registered in the system:: {list_customers_nid_ordered}. ")
            print("Enter an existing customer's NID ")
    return

def format_date(message):
    '''
    Date format verification function.
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
    Function that requests and checks the data entered for each rental.
    '''

    rental_equipment = {}

    rental_equipment['equipment_id'] = read_register_identifier("Insert lifting equipment identifier: ",list_equipment_id)
    rental_equipment['NID_Customer'] = read_register_nid_customer("Enter the client's ID who rents the lifting equipment: ",list_customers_nid_ordered)
    rental_equipment['date_start'] = format_date("Please, enter a start date with a DD/MM/AAAA format: ")
    rental_equipment['date_end'] = format_date("Please, enter an end date with a DD/MM/AAAA format: ")
    rental_equipment['price'] = read_whole_positive("Please, enter rental service price: ")

    list_equipment_rentals.append(rental_equipment) # Rentals made are compiled into a list.

def print_dictionary_rentals(list_equipment_rentals):
    '''
    Function that stores, orders and prints all rentals.
    '''
    dictionary_rental = {} # A dictionary is created to store the data of each rental.

    for equipment in list_equipment_rentals:
        newkey = equipment['equipment_id'] # The identifier of each piece of rented equipment will be the key of each key-value pair.
        dictionary_rental[newkey]=[]
    print("\n")

    for equipment in list_equipment_rentals: # We store each rented equipment based on its equipment identifier.
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
    Function that determines which equipment has not been rented yet.
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

# Potential values included in a tuple.
allowedBrands = ("palfinger", "kone", "schmalz")

list_equipment = [] # List containing the devices or equipment.
list_equipment_id = [] # List containing the equipment identifiers.
list_customers = [] # List containing customers.
list_customers_nid = [] # List containing only the NIDs of the clients.
list_customers_nid_ordered_no_letter = [] # List that contains the NIDs of the customers in an orderly manner and WITHOUT a verification letter.
list_customers_nid_ordered = [] # List that contains the NIDs of the customers in an orderly manner and WITH a verification letter.
list_customers_ordered = [] # List containing customer information in an ordered manner.
list_equipment_rentals = [] # List containing information of the rental equipment.


# Constants
VAT = 16  # Consistently 16% VAT on all items.
num_id = 0 # When the program launches, it begins by numbering  from number 1.

running = True # Determines whether we proceed through the menu or the user has selected option 4.
while running:
    option = show_menu() # Prints menu.
    if option == 1: # New lifting equipment data registration.
        print("\n")
        print_list_equipment(list_equipment)
        print("\n")
        print("*** ADD NEW LIFTING EQUIPMENT DATA: ***")
        num_id = register_equipment(num_id)

    elif option == 2: # New customer data registration.
        print("\n")
        print("*** ADD NEW CUSTOMER DATA: ***")
        register_customer()
        print("\n")
        new_list_customers_ordered(list_customers_nid_ordered_no_letter, list_customers, list_customers_nid_ordered, list_customers_ordered)
        print_new_list_customers_ordered(list_customers_ordered)
        list_customers_ordered = []

    elif option == 3: # New equipment rental data registration.
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

    elif option == 4: # Program ends.
        running = False

print("END")
