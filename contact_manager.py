import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact to the contacts dictionary."""
    print("\nAdd New Contact")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    if name in contacts:
        print(f"A contact with name '{name}' already exists.")
        return
    
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """Display all contacts in the system."""
    print("\nContact List")
    if not contacts:
        print("No contacts found.")
        return
    
    for i, (name, info) in enumerate(contacts.items(), 1):
        print(f"{i}. {name}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info['email']}")
        print()

def edit_contact(contacts):
    """Edit an existing contact."""
    print("\nEdit Contact")
    name = input("Enter the name of the contact to edit: ").strip()
    
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return
    
    print(f"\nCurrent details for {name}:")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    
    print("\nEnter new details (leave blank to keep current):")
    new_name = input(f"New name ({name}): ").strip()
    new_phone = input(f"New phone ({contacts[name]['phone']}): ").strip()
    new_email = input(f"New email ({contacts[name]['email']}): ").strip()
    
    if new_name and new_name != name:
        contacts[new_name] = contacts.pop(name)
        name = new_name
    
    if new_phone:
        contacts[name]['phone'] = new_phone
    if new_email:
        contacts[name]['email'] = new_email
    
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

def delete_contact(contacts):
    """Delete a contact from the system."""
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return
    
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully!")

def main():
    """Main program loop."""
    contacts = load_contacts()
    
    while True:
        print("\nPRODIGY INFOTECH - Contact Management System")
        print("1. Add New Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()