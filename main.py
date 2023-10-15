from datetime import date

from contact import Contact
from contact_list import ContactList


def main():
    contact_1 = Contact("Andrzej", "Wrocław", "000000000", "andrzej.b.czajka@gmail.com", date(1970, 1, 1))
    contact_2 = Contact("Marta", "Wrocław", "000000000", "adres@gmail.com", date(1970, 1, 1))
    contact_3 = Contact("Gabriela", "Wrocław", "000000000", "adres@wp.pl", date(1970, 1, 1))
    contacts = ContactList([contact_1, contact_2])
    contacts.add_new_contact(contact_3)
    print(20 * f"-")
    print(contacts.get_whole_contact_list())
    contacts.edit_contact_in_contact_list("Marta", "address", "Kraków")
    print(20 * f"-")
    print(contacts.get_whole_contact_list())
    contacts.delete_contact_from_contact_list(f"Andrzej")
    print(20 * f"-")
    print(contacts.get_whole_contact_list())
    print(contacts.get_contact_from_contact_list("Marta"))
    print(contacts.get_contact_from_contact_list("Monika"))


if __name__ == "__main__":
    main()
