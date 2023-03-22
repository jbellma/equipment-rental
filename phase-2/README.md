## <p align="center">PHASE 2</p>


### Introduction

There will now be three more features added to the program executed in phase one. Iteration in the program’s execution, validation of data, and the use of functions.

---

### Phase 2 Tasks to be Completed
- Task 1: Iteration.
- Task 2: Validation of Data.
- Task 3: Using Functions.

---

### TASK 1: Iteration

Only ***option 4*** will cause the program to quit; if any other option is selected, the appropriate duties will be performed, and the menu will then be shown once more. This is preferable to the program terminating after picking any option.

---

### TASK 2: Validation of Data

The application must verify user input if we want the data to be reliable. There must be standards for input data and procedures in place to verify the following:
- That the brand is one of the three allowed brands (***PALFINGER***, ***KONE*** and ***SCHMALZ***). 
- When adding a new piece of lifting equipment using ***option 1*** of the menu, the program will automatically assign the following ID number to the one previously used. It will start out with a ***value of 1***.
- It's also crucial to confirm that the user can only enter numbers in the data that requests them, such as menu options, pricing, etc (whole or real)

Moreover, the user must submit the following information when adding new customers:

- ***Name***:
- ***First Surname***: 
- ***Second Surname***:
- ***NID*** (National ID): If the number of digits is fewer than eight, it must be confirmed that the NID of the client is correct and written in the most popular format (NNNNNNL) without leading zeros. (N: Number, L: Letter)
- ***Phone***: All phones will be stored as 9-digit integer numbers
- ***Address***:


                                                      
                                                      
                                                 Please, select an option (1-4):  2
                           
                                                 Enter new customer's name:  Michael
                           
                                                 Fill in new customer's first surname:  Rodgers
                           
                                                 Complete new customer's second surname:  Martinez
                           
                                                 Enter new customer's NID with a 'NNNNNNNNL' format:  6273514H
                                                 NID 6273514H is not valid
                           
                                                 Enter new customer's NID with a 'NNNNNNNNL' format:  31734403S
                           
                                                 Type new customer's phone number:  913526271
                           
                                                 Fill in new customer's address:  Mount Avenue, 1  
                           
                                                 ### CUSTOMER DATA ### 
                                                 Name:  Michael
                                                 First Surname:  Rodgers
                                                 Second Surname:  Martinez
                                                 NID:  31734403S
                                                 Phone Number:  913526271
                                                 Address:  Mount Avenue, 1
                                                   


---

### TASK 3: Using functions

The usage of functions, as was already said, is a significant difference in this phase. Among other things, this will enable us to finish the program's logic, though not the full program. 

At the very least, we'll implement the following features:
- A method for displaying menus and returning the user's chosen option (only valid options).
- A function that carries out ***option 1*** (register a new product). The user will be prompted for the information, and the function will do the necessary checks. The dataset for the new product will be returned as a parameter.
- A function that carries out menu item "***option 2***" (new customer). By calling the relevant function, it must be established the NID's accuracy. The entire client data will be returned as a dataset.
- A function that repeatedly requests a genuine number from the user until it receives it.
- A function that shows all the information for a piece of lifting gear and another function that shows all the information for a particular client



                                                  ### EQUIPMENT DATA ###
                                                  ID:  1
                                                  Brand: PALFINGER
                                                  Model:  SM 100.2
                                                  Type: Caterpillar crane
                                                  Description:  Crane with exceptional off-road mobility
                                                  Price before VAT:  350.2
                                                  Price after VAT:  406.23199999999997
                                                  Stock :  4                                       

                                           
                                                  ### CUSTOMER DATA ###
                                                  Name:  Michael
                                                  First Surname:  Rodgers
                                                  Second Surname:  Martinez
                                                  NID:  31734403S
                                                  Phone Number:  913526271
                                                  Address:  Mount Avenue, 1
                                  

                                             
                                             


