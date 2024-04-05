# 1. User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:

import re
contacts = {} # contact list
def cli(): # Command Line Interface
    while True:
        print("""
        Welcome to the Contact Management System!! 📝
        
        Menu:
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export contacts to a text file
                        
        """)
        try:
            user_input = int(input("Please choose an option 1-7: "))
            if int(user_input) == 1:   # 1. Add a contact
                add_contact() 
            elif int(user_input) == 2: # 2. Edit a contact
                edit_contact()
            elif int(user_input) == 3: # 3. Delete a contact
                delete_contact()
            elif int(user_input) == 4: # 4. Search for a contact
                search_contact()
            elif int(user_input) == 5: # 5. Display all contacts
                display_contact()
            elif int(user_input) == 6: # 6. Export contacts to a text file
                export_contact()
            elif int(user_input) == 7: # 7. Quit
                break
            else: # Error Handling when the user inputs an invalid number
                print("\n\n\nInvalid input.. Try again!") 
        except (ValueError, OverflowError): # Error Handling when the user inputs a string or overflow 
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")         

def add_contact(): # This function is used to add a contact
    name = input("\nWhat is the contacts name?: ")
    address = input("\nEnter contacts address: ")
    email = ""
    while True:
            email = input("\nWhat is your contacts email address?: ")
            valid_email = re.search(r'[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+.[A-z]{2,}', email)
            if valid_email:
                break
            else:
                print("Invalid email. Please try again.")

    contacts[email] = [name, address]
    print(contacts)

    another_contact = input("\nwould you like to add another? (y/n): ")
    if another_contact == "y":
        add_contact()

def edit_contact(): #This function is to edit a contact
    user_input = input("\nWhich contact would you like to edit?: ")
    try:
        for k, v in contacts.items():
            if v[0] == user_input:
                key = k
                break
        else:
            print(f"{user_input} does not exist")
            return
        edit = input("\nWhat would you like to edit? {name, address, email}: ")
        if edit == "name":
            name = input("what is the new name?: ")
            contacts[key][0] = name
            print(f"You have updated contacts name to {name}")
        elif edit == "address":
            address = input("\nWhat is the new address?: ")
            contacts[key][1] = address
        else:
            email = input("\nWhat is the new email?: ")
            contacts[key] = email
    except Exception as e:
        print(f"you have an error at: {e}")

    edit_another = input("\nwould you like to edit another contact? (y/n): ")
    if edit_another == "y":
        edit_contact()
print(contacts)    

def delete_contact(): #This function is to delete a contact
    user_input = input(f"Who would you like to delete from your list?: ")
    try:
        for k, v in contacts.items():
            if v[0] == user_input:
                key = k
        del contacts[key]
        print(contacts)
        return k
    except Exception as e:
        print(f"There was an error at: {e}")
    

def search_contact(): #This function is to search a contact
    user_input = input(f'Please enter the name of the contact you are searching for: ')
    try:
        for k, v in contacts.items():
            if v[0] == user_input:
                name = v[0]
                address = v[1]
                print(f'You found {name} who lives at {address} with the following email: {k}')
    except Exception as e:
        print(f'There was an error at: {e}')

def display_contact(): #This function will display all contacts
    print("\nHere are your current contacts")
    for k, v in contacts.items():
        print(f"\n{v[0]} lives at {v[1]}, Email: {k}")

def export_contact(): #This function will export the contact list to a separate .txt file
    with open("contacts.txt", "w") as file:
        for k, v in contacts.items():
            name = v[0]
            address = v[1]
            email = k
            file.write(f'\nName: {name}: Address: {address} Email: {email}')


cli()
print(contacts)