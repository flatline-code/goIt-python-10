from classes import AddressBook, Record


def input_error(handler):
    def wrapper(*args):
        try:
            return handler(*args)
        except Exception as e:
            error_string = e.args[0]
            if "show_phone()" in error_string: 
                return 'enter name' 
            else:
                return 'enter name and phone' 
    return wrapper

def stop():
    return 'Good bye!'

def greeting():
    return 'How can I help you?' 

@input_error
def add(name, phone):
    if address_book.data.get(name):
        return 'Contact already exist' 
    
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return 'new contact added'

@input_error
def add_phone(name, phone):
    if address_book.data.get(name):
        record = address_book.data[name]
        record.add_phone(phone)
        return f'A new phone {phone} has been added to contact {name}' 
    else:
        return 'Сontact does not exist' 

@input_error
def change(name, phone):
    new_phone = input('enter new phone\n')
    record = address_book.data[name]

    if record.change_phone(phone, new_phone) is True:
        return f'{name} phone number changed to {new_phone}' 
    else:
        return 'Phone number does not exist' 

@input_error
def delete_phone(name, phone):
    record = address_book.data[name]

    if record.delete_phone(phone) is True:
        return f'Contact: {name} phone {phone} deleted' 
    else:
        return 'Phone number does not exist' 

@input_error
def show_phone(name):
    if name in address_book.data.keys():
        phones_list = []
        for phone in address_book.data[name].phones:
            phones_list.append(phone.value)
        return phones_list 
    else:
        return 'no such name' 

def show_all():
    if not address_book.data:
        return 'nothing to show'

    all_contacts = ''
    for name, record in address_book.items():
        phones_list = []
        for phone in record.phones:
            phones_list.append(phone.value)
        all_contacts += f'{name} | phones: {phones_list}\n'
    return all_contacts

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
            print(stop())
            break
        
        if commands_without_input.get(user_command):
            result = commands_without_input[user_command]()
            print(result)
            continue
        elif commands_with_input.get(command):
            result = commands_with_input[command](*user_inputs)
            print(result)
            continue
        else:
            print('unknown command')
            continue

if __name__ == '__main__':
    address_book = AddressBook()
    main()