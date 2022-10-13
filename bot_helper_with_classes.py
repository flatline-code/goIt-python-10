from classes import AddressBook, Record


def input_error(handler):
    def wrapper(*args):
        try:
            return handler(*args)
        except Exception as e:
            error_string = e.args[0]
            if "show_phone()" in error_string: 
                print('enter name')
            else:
                print('enter name and phone')
    return wrapper

def stop():
    print('Good bye!')

def greeting():
    print('How can I help you?')

@input_error
def add(name, phone):
    if address_book.data.get(name):
        print('Contact already exist')
        return
    
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    print('new contact added')

@input_error
def add_phone(name, phone):
    if address_book.data.get(name):
        record = address_book.data[name]
        record.add_phone(phone)
        print(f'A new phone {phone} has been added to contact {name}')
    else:
        print('Сontact does not exist')

@input_error
def change(name, phone):
    new_phone = input('enter new phone\n')
    record = address_book.data[name]

    if record.change_phone(phone, new_phone) is True:
        print(f'{name} phone number changed to {new_phone}')
    else:
        print('Phone number does not exist')

@input_error
def delete_phone(name, phone):
    record = address_book.data[name]

    if record.delete_phone(phone) is True:
        print(f'Contact: {name} phone {phone} deleted')
    else:
        print('Phone number does not exist')

@input_error
def show_phone(name):
    if name in address_book.data.keys():
        phones_list = []
        for phone in address_book.data[name].phones:
            phones_list.append(phone.value)
        print(phones_list)
    else:
        print('no such name')

def show_all():
    if not address_book.data:
        print('nothing to show')
        return

    for name, record in address_book.items():
        phones_list = []
        for phone in record.phones:
            phones_list.append(phone.value)
        print(f'{name} | phones: {phones_list}')

def main():  
    commands_without_input = {
      'hello': greeting,
      'exit': stop,
      'close': stop,
      'good bye': stop,
      'show all': show_all,
    }

    commands_with_input = {
        'add': add,
        'add_phone': add_phone,
        'change': change,
        'phone': show_phone,
        'delete': delete_phone,
    }
    
    while True:
        user_command = input('...').lower()
        user_command_with_inputs = user_command.split(' ')
        command = user_command_with_inputs[0]
        user_inputs = user_command_with_inputs[1:]

        if user_command in ['exit', 'close', 'good bye']:
            stop()
            break
        
        if commands_without_input.get(user_command):
            commands_without_input[user_command]()
            continue
        elif commands_with_input.get(command):
            commands_with_input[command](*user_inputs)
            continue
        else:
            print('unknown command')
            continue

if __name__ == '__main__':
    address_book = AddressBook()
    main()