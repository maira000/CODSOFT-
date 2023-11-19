class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"\nContact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, info in self.contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("-" * 20)

    def search_contact(self, keyword):
        matching_contacts = []
        for name, info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in info['phone']:
                matching_contacts.append((name, info))
        return matching_contacts

    def update_contact(self, name, new_phone, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"\nContact {name} updated successfully.")
        else:
            print(f"\nContact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"\nContact {name} deleted successfully.")
        else:
            print(f"\nContact {name} not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            matching_contacts = contact_manager.search_contact(keyword)
            if matching_contacts:
                print("\nMatching Contacts:")
                for name, info in matching_contacts:
                    print(f"\nName: {name}")
                    print(f"Phone: {info['phone']}")
                    print(f"Email: {info['email']}")
                    print(f"Address: {info['address']}")
                    print("-" * 20)
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone, new_email, new_address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("\nExiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
