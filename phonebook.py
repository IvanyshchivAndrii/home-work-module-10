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


class Field:
    pass


class Name(Field):
    def __init__(self, name: str):
        self.value = name


class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone


def input_error(func):
    def inner(*args):
        try:
            if 1 < len(args) <= 2 and args[0] != 'phone':
                print('Enter telephone number')
            elif len(args) <= 1 and args[0] == 'phone':
                print('Enter Username')
            elif len(args) <= 1 and args[0] in ['add']:
                print('Enter Username and telephone number')
            elif len(args) <= 1 and args[0] in ['add']:
                print('Enter Username and telephone number')
            else:
                return func(*args)
        except KeyError:
            print('Enter existing or correct username')
        except IndexError as e:
            print(e)

    return inner


def helper(*args):
    print('hello - print "say hello',
          'add - adding Name and Phone. You have to enter Name and Phone through a space',
          'change - changing Phone of user Name. You have to enter user nave and new Phone through a space',
          'phone - showing Phone of user. You have to enter username',
          'show all - showing all contacts', sep='\n')
    return ''


def say_hallo(*args):
    print("How can I help you?")
    return ''


PHONEBOOK = AddressBook()


@input_error
def add_contact(*args):
    name = Name(args[1].title())
    phone = Phone(args[2])
    record = Record(name, phone)
    PHONEBOOK.add_record(record)
    print(f'Contact {args[1].title()} {args[2]} has been added to PHONEBOOK')
    return ''


@input_error
def add_phone_to_contact(*args):
    if args[1].title() in PHONEBOOK:
        phone = Phone(args[2])
        PHONEBOOK[args[1].title()].add_phone(phone)
        print(f'Phone {args[2]} has been added to contact {args[1].title()}')
    else:
        print(f'Contact {args[1]} is not exist!!')
    return ''


@input_error
def change_contact(*args):
    old_phone = Phone(args[2])
    new_phone = Phone(args[3])
    if args[1].title() in PHONEBOOK:
        PHONEBOOK[args[1]].change_phone(old_phone, new_phone)
        print(f'Phone {old_phone.phone} in PHONEBOOK has been changed to {new_phone.phone}')
    else:
        print(f'There is no {args[1]} in PHONEBOOK !')
    return ''


@input_error
def show_phone(*args):
    print(f'The number you have searched: {list(i.phone for i in PHONEBOOK[args[1]].phones)}')
    return ''


def show_all_contacts(*args):
    num, name, tel = '№', 'Name', 'Phone'
    print(f'|{num:^5}|{name:^10}|{tel:^15}|')
    for k, v in enumerate(PHONEBOOK):
        phones_list = '\n'.join(i.phone for i in PHONEBOOK[v].phones)
        print(f'|{k:^5}|{v:^10}|{phones_list:^15}|')
    return ''


OPERATIONS = {
    'hello': say_hallo,
    'new': add_contact,
    'add':add_phone_to_contact,
    'change': change_contact,
    'phone': show_phone,
    'show all': show_all_contacts,
    'help': helper
}


def get_hendler(*args):
    return OPERATIONS[args[0]]


def main():
    flag = True
    print('Hello!! This is your phonebook assistant. Let\'s start!!')
    while flag:
        request = input('Enter request>>>').lower()
        request_list = request.split()

        if request_list[0] in list(OPERATIONS):
            get_hendler(*request.split())(*request.split())
        elif ' '.join(request_list[0:2]) == 'show all':
            show_all_contacts()
        elif request in ['exit', 'close', 'good bye']:
            flag = False
        else:
            print('Please, write one of the command')


if __name__ == '__main__':
    main()
