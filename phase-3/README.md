## <p align="center">PHASE 3</p>


### Introduction

It should be understood ***phase 3*** as a continuation of the second phase. Unlike ***phase 2***, this phase requires the use of data structures (lists, dictionaries, sets, etc.) whenever necessary. Libraries won't be used.

***Phase 3*** adds to the code delivered in ***Phase 2*** the use of data structures for storage of information in the program and its management.


---

### Phase 3: Tasks to be Completed

- Task 1: The code will be completely error-free and capture errors with exceptions.

- Task 2: To prevent errors, data will be kept in lower case. ***NID*** will be written in all caps when stored. 

- Task 3: Clients and lifting supplies will be arranged and stored appropriately.

- Task 4: The application will allow users to add new rental records for lifting equipment and save them in a  dictionary of lists.

- Task 5: Data on lifting devices, customers, and rentals will always be displayed as indicated.

All of these features can be broken down into the ***four*** basic duties listed below.

---

### TASK 1: Robust Code

Code must be modified to ensure that it never throws unexpected runtime errors but rather detects all potential issues, primarily by user input. The following figure provides instances of various wrong ***NIDs*** along with solutions.

                              Enter new customer's NID with a 'NNNNNNNNL' format: 8917234iuyqw
                              Error, there must be numbers in the first 8 characters. Please provide a valid NID.
                              
                              Enter new customer's NID with a 'NNNNNNNNL' format: absnd3ns9
                              Error, there must be numbers in the first 8 characters. Please provide a valid NID.
                              
                              Enter new customer's NID with a 'NNNNNNNNL' format: 1234567893l
                              1234567893l is not a valid NID.
                              
                              Enter new customer's NID with a 'NNNNNNNNL' format: 123
                              123 is not a valid NID.
                              
                              Enter new customer's NID with a 'NNNNNNNNL' format: 12345678L
                              12345678L is not a valid NID.

---

### TASK 2: Data Storage in Lower Case

The program will always store all input as lowercase character strings in program variables, allowing users to enter data in both uppercase and lowercase.

For instance, the user can enter the brand name ***PALFINGER***  as ***"PalfINger,"*** and the program will still presented as a proper value and store it in lowercase.

                             Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): PALFING
                             Error, brand not allowed.
                             
                             Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): PalFING
                             Error, brand not allowed.
                             
                             Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ): PalfINger
                             Stored brand: palfinger

Only one exception applies. The ***NID*** letter will be saved using the standard format for this data, which is a capital letter. If the user types it in lowercase, the program will change it and store it with the uppercase character as we have stated.

                             Enter new customer's NID with a 'NNNNNNNNL' format: 12345678z
                             Stored NID: 12345678Z
                                            
---

### TASK 3: Storage of Lifting Equipment and Customer Information

The program will enable the storage of numerous lifting devices and custumers (no limit).


All equipment will be arranged in chronological order. Every time the user chooses to insert a new lifting equipment (***option 1***), the list of all existing equipment will be displayed.

                            Please select an option from the menu: 1
                            ## LIFTING EQUIPMENT ##
                            ID     BRAND     MODEL     TYPE     DESCRIPTION      PRICE     P.+VAT     STOCK
                            ==     =====     =====     ====     ============     =====     ======     =====
                            1      palfinger m12       crane    basic crane      1300.00   1508.0     10
                            2      kone      m1234     booster  basic booster    1500.0    1740.0      5
                            
                            *** INSERT NEW LIFTING EQUIPMENT: ***
                            
                            Please provide the lifting equipment's brand name (PALFINGER, KONE or SCHMALZ):
                            
                         
Customers will always be arranged in accordance to their NID (from lowest to highest).

Every time the user inserts a new client, the program will check that one ***NID*** is not shared by more than one client. It will also show the complete list of clients in an orderly manner. ***NID*** number 12345678 precedes ***NID*** number 8765432.
  
  
                           *** INSERT NEW CUSTOMER DATA ***
                           
                           Enter new customer's name: john
                           
                           Fill in new customer's first surname: williams
                           
                           Complete new customer's second surname: valentine
                           
                           Enter new customer's NID with a 'NNNNNNNNL' format: 23456789v
                           23456789v is not a valid NID.
                           
                           Enter new customer's NID with a 'NNNNNNNNL' format: 23456789d 
                           Error, that NID already exists, enter another NID.
                           
                           Enter new customer's NID with a 'NNNNNNNNL' format: 34567890v
                           
                           Type new customer's phone number with a 'NNNNNNNNN' format: 918273645
                          
                          
      
      
    ...
                           
                           
        
                            ## CUSTOMERS: ##
                            NAME       SURNAME1   SURNAME2       NID         PHONE          ADDRESS     
                            ===        =====      ========      ========     =====          =======     
                            laura      moon       donegal       12345678Z    918273645      ann square, 1
                            maria      hololan    richards      23456789D    928374628      clogersaint, 4
                            john       williams   valentine     34567890V    918273645      kinsal, 7
                            
                            
                            
                            
                            ******** MAIN MENU ********
                            1. New Lifting Equipment
                            2. New Customer
                            3. New Lifting Equipment Rental
                            4. Exit

                            Please select an option from the menu:
                                          
---

### TASK 4: Lifting Equipment Rental

The appliacation will allow the user to enter information on new rental equipment. This requires the user to provide the following information:

- ***NID*** of the client attempting to rent lifting gear: the application will verify that the user exists previousy in the system. Until the user enters an NID that is already registered in the system, the software will continuously request the ***NID***.

                          Please select an option from the menu: 3
                          NEW LIFTING EQUIPMENT RENTAL
                          EQUIPMENT: [1, 2, 3]
                          CUSTOMERS: ['12345678Z', '23456789D']
                          
                          Enter the lifting equipment identifier: 5
                          Error, the equipment must be registered in the system: [1, 2, 3]
                          
                          Insert an existing lifting equipment's identification number: 3
                          
                          Enter the NID of the customer who is going to rent the lifting equipment: 123984761234
                          Error, the customer must be registered in the system: ['12345678Z', '23456789D']
                          
                          Insert an existing customer's NID identification number: 12345678z

- ***Identifier*** of the lifting equipment to be rented: the application will verify that the equipment exists previously in the system before being rented. For this last ***phase 3***, the application won't check to see whether more equipment is being rented than is available given its complexity.

- Start and end date of the rental: the program will not check if days are correct,
but they will have to follow the following format "DD/MM/YYYY" at all times, requesting
repeatedly until it is correct. 


                           Please insert a date with a DD/MM/AAAA format: as/as/asdf
                           Error, integers were expected to indicate DD, MM and AAAA. The expected format is DD/MM/AAAA.
                           
                           Please insert a date with a DD/MM/AAAA format: 1/11/2021
                           
                           Please insert a date with a DD/MM/AAAA format: 01/15/2021
                           01/15/2021
                           
                                                     

- Price without VAT: program will check if is a positive integer.

Rental data is very important to the company, so it will be necessary to store it properly in the system. In this case, it will be stored as a dictionary where the ***Identifier*** of the lifting equipment will be considered the ***Key***. As ***Value*** in the dictionary, a list will be included with all the rental data for that lifting equipment (customer ID, start_date, end_date and price). 

To facilitate the user's work when inserting a new rental, the ***NID*** of all existing customers + the ***Identifiers*** of all lifting equipment will be shown previously on the screen as if they were two lists. A function will be created to return a list of ***NIDs*** of registered customers and another function to return a list of ***Identifiers*** of all registered lifting equipment. 

                           ******** MAIN MENU ********
                           1. New Lifting Equipment
                           2. New Customer
                           3. New Lifting Equipment Rental
                           4. Exit

                           Please select an option from the menu: 3
                           NEW LIFTING EQUIPMENT RENTAL
                           EQUIPMENT: [1, 2, 3]
                           CUSTOMERS: ['12345678Z', '23456789D']

Finally, to make it easier for the user to insert a suitable price, the lowest and highest price of the rentals that have already been made for that same lifting equipment will be displayed on the screen, displaying the message ***"no previous rentals have been made for that equipment”*** if none exists. 

A function will be created to accurately display all rentals.
 
                           For equipment 3 the HIGHEST rental price so far is 300 and the lowest is 0
                          
                           Please type the rental price: 200
                           ############## RENTALS ###############################################
                           LIFTING EQUIPMENT 3
                           - ['12345678Z', '11/11/1111', '11/11/1111', 300]
                           - ['23456789D', '22/22/2222', '22/22/2222', 200]
                           LIFTING EQUIPMENT 1
                           - ['12345678Z', '11/11/1111', '11/11/1111', 250]
                          
                          
                          




