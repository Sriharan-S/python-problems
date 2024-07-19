import json

def load_contacts(file_path):
    """Load contacts from the JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error reading the contact file. It may be corrupted.")
        return {}

def save_contacts(file_path, contacts):
    """Save contacts to the JSON file."""
    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(file_path):
    """Add a new contact."""
    contacts = load_contacts(file_path)
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(file_path, contacts)
    print(f"Contact '{name}' added successfully.")

def view_contacts(file_path):
    """View all contacts."""
    contacts = load_contacts(file_path)
    if contacts:
        print("Contacts List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print()
    else:
        print("No contacts found.")

def delete_contact(file_path):
    """Delete a contact."""
    contacts = load_contacts(file_path)
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(file_path, contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def contact_manager():
    file_path = 'contacts.json'
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_contact(file_path)
        elif choice == '2':
            view_contacts(file_path)
        elif choice == '3':
            delete_contact(file_path)
        elif choice == '4':
            print("Exiting the contact manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

contact_manager()
