contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contact found.")

def update_contact():
    query = input("Enter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully.")
            return
    print("No contact found.")

def delete_contact():
    query = input("Enter name or phone number of the contact to delete: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("No contact found.")

def main_menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
