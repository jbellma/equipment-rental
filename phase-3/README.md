## <p align="center">PHASE 3</p>


### Introduction

It should be understood ***phase 3*** as a continuation of the second phase. Unlike ***phase 2***, this phase requires the use of data structures (lists, dictionaries, sets, etc.) whenever necessary. Libraries won't be used.

***Phase 3*** adds to the code delivered in ***Phase 2*** the use of data structures for storage of information in the program and its management.


---

### Phase 2: Tasks to be Completed

- Task 1: The code will be completely error-free and capture errors with exceptions.

- Task 2: To prevent errors, data will be kept in lower case. ***NID*** will be written in all caps when stored. 

- Task 3: Clients and lifting supplies will be arranged and stored appropriately.

- Task 4: The application will allow users to add new rental records for lifting equipment and save them in a  dictionary of lists.

- Task 5: Data on lifting devices, customers, and rentals will always be displayed as indicated.

All of these features can be broken down into the ***four*** basic duties listed below.

---

### TASK 1: Robust Code

Code must be modified to ensure that it never throws unexpected runtime errors but rather detects all potential issues, primarily by user input. The following figure provides instances of various wrong NIDs along with solutions.

FIGURE NEEDED

---

### TASK 2: Data Storage in Lower Case

The program will always store all input as lowercase character strings in program variables, allowing users to enter data in both uppercase and lowercase.

For instance, the user can enter the brand name ***PALFINGER***  as ***"PalfINger,"*** and the program will still presented as a proper value and store it in lowercase.

FIGURE NEEDED

Only one exception applies. The ***NID*** letter will be saved using the standard format for this data, which is a capital letter. If the user types it in lowercase, the program will change it and store it with the uppercase character as we have stated.

FIGURE NEEDED
                                            
---

### TASK 3: Storage of Lifting Equipment and Customer Information

The program will enable the storage of numerous lifting devices and costumers (no limit).
Equipment and customer data can be modified at any moment.

- All equipment will be arranged in chronological order. Every time the user chooses to insert a new lifting equipment (***option 1***), the list of all existing         equipment will be displayed.

- Customers will always be arranged in accordance with their NID (from lowest to highest).

  Every time the user inserts a new client, the program will check that one ***NID*** is not shared by more than one client. It will also show the complete list of clients in an orderly manner. ***NID*** number 12345678 precedes ***NID*** number 8765432.
  
  FIGURE NEEDED
  
  FIGURE NEEDED

---

### TASK 4: Lifting Equipment Rental

The appliacation will allow the user to enter information on new rental equipment. This requires the user to provide the following information:

- ***NID*** of the client attempting to rent lifting gear: the application will verify that the user exists previousy in the system. Until the user enters an NID that is already registered in the system, the software will continuously request the ***NID***.

FIGURE NEEDED

- ***Identifier*** of the lifting equipment to be rented: the application will verify that the equipment exists previously in the system before being rented. For this last ***phase 3***, the application won't check to see whether more equipment is being rented than is available given its complexity.

- Start and end date of the rental: the program will not check if days are correct,
but they will have to follow the following format "DD/MM/YYYY" at all times, requesting
repeatedly until it is correct. 

FIGURE NEEDED

- Price without VAT: program will check if is a positive integer.

Rental data is very important to the company, so it will be necessary to store it properly in the system. In this case, it will be stored as a dictionary where the ***Identifier*** of the lifting equipment will be considered the ***Key***. As ***Value*** in the dictionary, a list will be included with all the rental data for that lifting equipment (customer ID, start_date, end_date and price). 

To facilitate the user's work when inserting a new rental, the ***NID*** of all existing customers + the ***Identifiers*** of all lifting equipment will be shown previously on the screen as if they were two lists. A function will be created to return a list of ***NIDs*** of registered customers and another function to return a list of ***Identifiers*** of all registered lifting equipment. 





