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
        else:
            print(f'{phone.phone} already exist!')

    def remove_phone(self, phone):
        phones_dict = {phone.phone: index for index, phone in enumerate(self.phones)}
        if phone.phone in phones_dict.keys():
            del self.phones[phones_dict[phone.phone]]
        else:
            print(f'Sorry, {phone.phone} wasn\'t founded. Try again.')

    def change_phone(self, from_phone, to_phone):
        phones_dict = {phone.phone: index for index, phone in enumerate(self.phones)}
        if from_phone.phone in phones_dict.keys():
            self.phones[phones_dict[from_phone.phone]] = to_phone
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
            if 1 < len(args) <= 2 and args[0] not in ['phone', 'del']:
                print('Enter telephone number')
            elif len(args) <= 1 and args[0] == 'phone':
                print('Enter Username')
            elif len(args) <= 1 and args[0] in ['add']:
                print('Enter Username and telephone number')
            elif len(args) <= 2 and args[0] in ['add', 'change']:
                print('Enter Username and telephone number')
            elif len(args) <= 3 and args[0] in ['change']:
                print('Enter 2nd telephone number')
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
def delete_contact(*args):
    if args[1].title() in PHONEBOOK:
        PHONEBOOK.pop(args[1].title())
        print(f'Contact {args[1].title()} has been deleted from PHONEBOOK')
    else:
        print(f'Contact {args[1].title()} does not exist!!')
    return ''


@input_error
def add_phone_to_contact(*args):
    if args[1].title() in PHONEBOOK:
        phone = Phone(args[2])
        PHONEBOOK[args[1].title()].add_phone(phone)
        print(f'Phone {args[2]} has been added to contact {args[1].title()}')
    else:
        print(f'Contact {args[1].title()} does not exist!!')
    return ''


@input_error
def remove_phone_contact(*args):
    if args[1].title() in PHONEBOOK:
        phone = Phone(args[2])
        PHONEBOOK[args[1].title()].remove_phone(phone)
        print(f'Phone {args[2]} has been removed from contact {args[1].title()}')
    return ''


@input_error
def change_contact(*args):
    old_phone = Phone(args[2])
    new_phone = Phone(args[3])
    if args[1].title() in PHONEBOOK:
        PHONEBOOK[args[1].title()].change_phone(old_phone, new_phone)
        print(f'Phone {old_phone.phone} in PHONEBOOK has been changed to {new_phone.phone}')
    else:
        print(f'There is no {args[1]} in PHONEBOOK !')
    return ''


@input_error
def show_phone(*args):
    print(f'The number you have searched: {list(i.phone for i in PHONEBOOK[args[1].title()].phones)}')
    return ''


def show_all_contacts(*args):
    num, name, tel = '№', 'Name', 'Phones'
    print(f'|{num:^5}|{name:^10}|{tel:^15}|')
    for k, v in enumerate(PHONEBOOK):
        phones_list = ', '.join(i.phone for i in PHONEBOOK[v].phones)
        len_num = len(phones_list) if len(phones_list) > 15 else 15
        print(f'|{k:^5}|{v:^10}|{phones_list:^{len_num}}|')
    return ''


OPERATIONS = {
    'hello': say_hallo,
    'new': add_contact,
    'del': delete_contact,
    'add': add_phone_to_contact,
    'remove': remove_phone_contact,
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
    try:
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
    except IndexError:
        print('Enter command and values')


if __name__ == '__main__':
    main()
