from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)
        print(f'{phone.get_phone()} was added to {self.name.get_name()}\'s list of phones')

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            print(f'{phone.get_phone()} was removed from list of phones')
        else:
            print(f'Sorry, {phone.get_phone()} wasn\'t founded. Try again.')

    def change_phone(self, from_phone, to_phone):
        if from_phone in self.phones:
            self.phones[self.phones.index(from_phone)] = to_phone
            print(f'{from_phone.get_phone()} was changed to {to_phone.get_phone()} in list of phones')
        else:
            print(f'Sorry, {from_phone} wasn\'t founded. Try again.')

    def show_phones(self):
        if self.phones:
            phones_list = [i.get_phone() for i in self.phones]
            print(f'{self.name.get_name()}: {phones_list}')

    def get_phones(self):
        if self.phones:
            return [i.get_phone() for i in self.phones]
        else:
            print('There are no phones')


class Field:
    pass


class Name(Field):
    def __init__(self, name: str):
        self.value = name

    def get_name(self):
        return self.value

    def set_name(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone




