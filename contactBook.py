class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_entry(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def view_entries(self):
        if self.contacts:
            print("\nContacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts available.")

    def search_entries(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return results

    def display_search_results(self, results):
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_entry(self, name, phone, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                contact.address = address
                print(f"Contact updated: {contact}")
                return
        print(f"Contact not found: {name}")

    def delete_entry(self, name):
        updated_contacts = [contact for contact in self.contacts if contact.name != name]
        if len(updated_contacts) < len(self.contacts):
            self.contacts = updated_contacts
            print(f"Contact deleted: {name}")
        else:
            print(f"Contact not found: {name}")

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            address_book.add_entry(name, phone, email, address)
        elif choice == "2":
            address_book.view_entries()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_results = address_book.search_entries(search_term)
            address_book.display_search_results(search_results)
        elif choice == "4":
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            address_book.update_entry(name, phone, email, address)
        elif choice == "5":
            name = input("Enter contact name to delete: ")
            address_book.delete_entry(name)
        elif choice == "6":
            print("Exiting Address Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
