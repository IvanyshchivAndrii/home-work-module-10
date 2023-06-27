from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        if isinstance(phone, Phone):
            self.phones = [phone]
        else:
            self.phones = []

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
            print(f'{phone.phone} was added to {self.name.value}\'s list of phones')
        else:
            print(f'{phone.phone} already exist!')

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            print(f'{phone.phone} was removed from list of phones')
        else:
            print(f'Sorry, {phone.phone} wasn\'t founded. Try again.')

    def change_phone(self, from_phone, to_phone):
        if from_phone in self.phones:
            self.phones[self.phones.index(from_phone)] = to_phone
            print(f'{from_phone.phone} was changed to {to_phone.phone} in list of phones')
        else:
            print(f'Sorry, {from_phone.phone} wasn\'t founded. Try again.')

    def show_phones(self):
        if self.phones:
            phones_list = [i.phone for i in self.phones]
            print(f'{self.name.value}: {phones_list}')

    def get_phones(self):
        if self.phones:
            return [i.phone for i in self.phones]
        else:
            print('There are no phones')


class Field:
    pass


class Name(Field):
    def __init__(self, name: str):
        self.value = name

    # def get_name(self):
    #     return self.value
    #
    # def set_name(self, name):
    #     self.value = name


class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone

    # def get_phone(self):
    #     return self.phone
    #
    # def set_phone(self, phone):
    #     self.phone = phone


# def main():
#     flag = True
#     print('Hello!! This is your phonebook assistant. Let\'s start!!')
#     while flag:
#         request = input('Enter request>>>').lower()
#         request_list = request.split()
#         if request_list[0] in list(OPERATIONS):
#             get_hendler(*request.split())(*request.split())
#         elif ' '.join(request_list[0:2]) == 'show all':
#             show_all_contacts()
#         elif request in ['exit', 'close', 'good bye']:
#             flag = False
#         else:
#             print('Please, write one of the command')
#     set_contacts(PHONEB00K)

name = Name('Andrey')
phone = Phone('+380978546398')
phone1 = Phone('+380951368745')
phone2 = Phone('+380978546398')


record = Record(name, phone)

record.show_phones()
record.add_phone(phone)
record.show_phones()
