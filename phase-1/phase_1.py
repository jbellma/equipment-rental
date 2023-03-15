# Prints Main Menu
print("\n\n\n")
print("******** MAIN MENU ********")
print("1. New Lifting Equipment")
print("2. New Customer")
print("3. New Lifting Equipment Rental")
print("4. Exit")

# It prompts the user to choose one of the Main Menu choices between one and four to be executed.
option = int(input("Please select an option (1-4): "))

# option
if option<1 or option>4:
    print("Error: invalid option")
elif option==1:
    print("New Lifting Equipment")
elif option==2:
    print("New Customer")
elif option==3:
    print("New Lifting Equipment")
elif option==4:
    print("Exit")
