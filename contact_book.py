def display_all_contacts(contacts):
    if len(contacts) != 0:
        for name,details in contacts.items():
            print(f"Name: {name}")
            print(f" Phone: {details["phone"]}")
            print(f" Email: {details["email"]}")
            print("-"*20)
    else:
        print("No contacts found")        


def add_contacts(contacts):
    name = input("Enter your name: ")
    contacts[name] = {
            "phone" : input("Enter your phone number: "),
            "email" : input("Enter your Email Id: ")
    }
    print("Contact added successfully!")
    return contacts

def search_contacts(contacts,name):
    if name in contacts:
        print(f"Name: {name}")
        print(f" Phone: {contacts[name]["phone"]}")
        print(f" Email: {contacts[name]["email"]}")
    else:
        print("Contact not found.")


def delete_contact(contacts,name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
    return contacts

contacts = {}

def main():
    print("**************Welcome to Contact Book*********************")
    while True:
        ip = input('''
    --------------------------
    1. View all contacts
    2. Add contact
    3. Search contact
    4. Delete contact
    5. Quit
    Enter your choice: ''')
        if ip == "1":
            print()
            display_all_contacts(contacts)
        elif ip == "2":
            print()
            add_contacts(contacts)
        elif ip == "3":
            print()
            n = input("Enter contact to search: ")
            search_contacts(contacts,n)
        elif ip == "4":
            d = input("Enter contact to delete: ")
            delete_contact(contacts,d)
        elif ip == "5":
            print()
            print("GoodBye !")
            break
        else:
            print("Invalid choice. Try again.")

    
if __name__ == "__main__":
    main()