class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        """Add a new contact to the contact book."""
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        """View all contacts in the contact book."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Found Contact - Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print(f"No contact found with the name {name}.")

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print(f"No contact found with the name {name}.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting Contact Book...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
