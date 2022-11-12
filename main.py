def welcome():
    entry = int(input("""Welcome to py contact book.
        >>> Py contact book commands are: 1, 2, 3, 4 and 5 <<<
        >>> What would you like to do? <<<
        1. Display your existing contact
        2. Create a new contact
        3. Check a contact
        4. Remove a contact
        5. Exit
        Enter your entry here (1,2,3,4 or 5):  """))
    return entry


def phoneBook():
    contact = {}
    while True:
        entry = welcome()

        if entry == 1:
            if contact:
                for k, v in contact.items():
                    print(k, '-->', v)
            else:
                print("Phone book is empty, go back to menu and add a new contact")

        elif entry == 2:
            phone_number = input("Enter the phone number: ")
            contact_name = input("Enter the name, format is Firstname, Lastname: ")

            if phone_number not in contact.items():
                contact.update({contact_name: phone_number})
                print("Contact saved successfully")
                print("Updated is shown below")
                for k, v in contact.items():
                    print(k, '-->', v)
            else:
                print("The contact already exists")

        elif entry == 3:
            name = input("Enter the name of the contact you want to view: ")

            if name in contact:
                print("The contact is ", name, ':', contact[name])
            else:
                print("The contact does not exist")

        elif entry == 4:
            name = input("Enter the name of the contact you want to remove: ")
            if name in contact:
                contact.pop(name)

            print("Updated phonebook is shown below")
            for k, v in contact.items():

                print(k, '-->', v)

            else:
                print("The contact does not exist, return to the main menu ")

        elif entry == 5:
            print("Phonebook is closing")
            break
        else:
            print("Incorrect Entry!")


if __name__ == "__main__":
    phoneBook()

