class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = Contact(name, phone, email, address)
        self.contacts[name] = contact
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts.values():
                print(contact)

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts.values():
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(contact)
                found = True
        if not found:
            print("No contact found with that name or phone number.")

    def update_contact(self):
        name = input("Enter the name of the contact you want to update: ")
        if name in self.contacts:
            print("Enter new details (leave blank to keep the current value).")
            phone = input(f"Enter new phone number (current: {self.contacts[name].phone}): ")
            email = input(f"Enter new email (current: {self.contacts[name].email}): ")
            address = input(f"Enter new address (current: {self.contacts[name].address}): ")

            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            if address:
                self.contacts[name].address = address

            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact you want to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    def menu(self):
        while True:
            print("\n--- Contact Manager ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.menu()
