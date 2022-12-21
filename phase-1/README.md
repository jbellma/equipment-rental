## <p align="center">PHASE 1</p>


### Introduction

The company ***YOURCRANE.com*** is a leading company that provides modern lifting products and services. Its main activity is the rental of fixed and mobile cranes
with operator. Given the success of the company in recent months, they have asked me for help in order to manage their equipment rentals. A software application must be developed to recognize and respond to the company's needs.

The project will be divided into three ***phases*** in order to simplify the task into a series of logical and manageable steps:

- Phase 1: Main program menu and data entry.
- Phase 2: Structuring the code into functions and data validation.
- Phase 3: Catalog of products, services and contracts.

---

### Phase 1 Tasks to be Completed
- Task 1: Main Program Menu of the application will be printed.
- Task 2: New products may also be introduced in the catalogue.

#### TASK 1: Printing the menu
When running the application, the following menu will appear on the screen (standard output).


                                          ******** MAIN MENU ********
                                           1. New Lifting Equipment
                                           2. New Customer
                                           3. New Lifting Equipment Rental
                                           4. Exit

                                          Please select an option (1-4):

The user (a worker form the company) will be asked to choose an option from the menu,**"Please select an option (1-4):"**
* If the user selects an invalid option ( a value that differs from the permissible values between 1-4), the message **"Error: invalid option"** will appear on the       screen.
* If any valid option is selected, the following will happen:
  - Depending on the option inserted by the user, the name of the option selected for execution is displayed and executed. For example, if the user selects option 1,       the output will be: **"NEW LIFTING EQUIPMENT"** and the corresponding ***task 2*** is executed.
  - If the user choses any other option (2-4), since there are no tasks associated, only the option to be executed will be printed. For example, the
    option 3 → will print **“NEW LIFTING EQUIPMENT RENTAL”** . 
  - Option 4 in particular → will print **"EXIT"** and will end the program.
  
---
 
#### TASK 2: New Lifting Equipment
As part of this task, the company's worker will enter the following data on new lifting equipment that the company has recently acquired:
* Lifting equipment identifier: sequential number given to every single piece of equipment owned by the company (no two pieces of equipment may share the same     
  identifier).
  


