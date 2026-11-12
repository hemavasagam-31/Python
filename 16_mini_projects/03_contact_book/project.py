"""Contact book mini-project."""

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    contacts[name] = phone
    print("Contact saved.")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    for name, phone in contacts.items():
        print(f"{name} -> {phone}")


def contact_book():
    contacts = {}

    while True:
        print("\nContact Book")
        print("1. Add contact")
        print("2. Search contact")
        print("3. View all contacts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            view_contacts(contacts)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    contact_book()
