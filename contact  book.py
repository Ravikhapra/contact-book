# Contact Book Program

# an empty dictionary to store contacts
contact_book = {}

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    #   line 12 ,The contact_information() function is responsible for viewing the contact list.
    print("4. View Contact Information")
    print("5. Update Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_book[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    name = input("Enter name of contact to search: ")
    if name in contact_book:
        print("Contact found!")
        print("Phone:", contact_book[name]["phone"])
        print("Email:", contact_book[name]["email"])
    else:
        print("Contact not found!")

def contact_information():
    # line 40, The contact_information() function is responsible for viewing the contact list.
    if contact_book:
        print("Contact Information:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact book is empty!")

def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contact_book:
        print("Enter new details (press enter to keep current value):")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        if phone:
            contact_book[name]["phone"] = phone
        if email:
            contact_book[name]["email"] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        contact_information()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again!")