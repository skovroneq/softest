import Levenshtein
class ContactList:
    BACKUP_FILENAME = "contacts_backup.txt"

    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.contact_names = None

    def add_new_contact(self, contact):
        if self.check_if_contact_exists_in_contact_list(contact.name):
            return (f'Niepowodzenie! Kontakt z imieniem {contact.name} już istnieje, wybierz inne imię stosując '
                    f'indeksację, np {contact.name}_2121')
        self.contact_list.append(contact)
        return "Sukces!"

    def check_if_contact_exists_in_contact_list(self, contact_name):
        self.refresh_contact_names()
        return contact_name in self.contact_names

    def refresh_contact_names(self):
        self.contact_names = []
        for contact in self.contact_list:
            self.contact_names.append(contact.name)

    def suggest_contact_name(self, contact_name):
        best_match = None
        min_distance = float("inf")

        for name in self.contact_names:
            distance = Levenshtein.distance(name, contact_name)
            if distance < min_distance:
                min_distance = distance
                best_match = name

        return best_match

    def get_contact_from_contact_list(self, contact_name):
        for contact in self.contact_list:
            if contact.name == contact_name:
                return contact

        suggestion = self.suggest_contact_name(contact_name)
        return suggestion if suggestion else None

    def edit_contact_in_contact_list(self, contact_name, contact_feature, new_value):
        contact_to_edit = None

        for contact in self.contact_list:
            if contact.name == contact_name:
                contact_to_edit = contact
                break

        if contact_to_edit:
            setattr(contact_to_edit, contact_feature, new_value)
            print(f"Kontakt o nazwie '{contact_name}' zaktualizowany.")
        else:
            print(f"Kontakt o nazwie '{contact_name}' nie istnieje.")

    def delete_contact_from_contact_list(self, contact_name):
        contact_to_delete = None

        for contact in self.contact_list:
            if contact.name == contact_name:
                contact_to_delete = contact
                break
        if contact_to_delete:
            self.contact_list.remove(contact_to_delete)
            print(f"Kontakt o nazwie '{contact_name}' został usunięty")
        else:
            print(f"Nie można usunąć.Kontakt o nazwie'{contact_name}' nie istnieje")

    def load_contact_list_from_hard_disc(self):
        pass

    def save_contact_list_to_hard_disc(self):
        pass

    def get_whole_contact_list(self):
        str_contact_list = f"\nLista kontaktów w Twojej bazie jest następująca:\n"
        for contact in self.contact_list:
            str_contact_list += str(contact)
        str_contact_list += f"------------------------------------------------------------\n"
        return str_contact_list
