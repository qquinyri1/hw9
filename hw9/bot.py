import json

PHONEBOOK_FILE = 'phonebook.json'

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

def load_phonebook():
    try:
        with open(PHONEBOOK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, 'w') as file:
        json.dump(phonebook, file)

@input_error
def hello_command():
    return "How can I help you?"

@input_error
def add_command(name, phone):
    phonebook = load_phonebook()
    phonebook[name] = phone
    save_phonebook(phonebook)
    return "Contact added successfully."

@input_error
def change_command(name, phone):
    phonebook = load_phonebook()
    if name not in phonebook:
        raise KeyError
    phonebook[name] = phone
    save_phonebook(phonebook)
    return "Phone number changed successfully."

@input_error
def phone_command(name):
    phonebook = load_phonebook()
    if name not in phonebook:
        raise KeyError
    return f"The phone number for {name} is {phonebook[name]}."

@input_error
def show_all_command():
    phonebook = load_phonebook()
    if not phonebook:
        return "The phonebook is empty."
    result = "Phonebook entries:\n"
    for name, phone in phonebook.items():
        result += f"{name}: {phone}\n"
    return result

def main():
    while True:
        command = input("Enter a command: ").lower()
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print(hello_command())
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_command(name, phone))
            except ValueError:
                print("Invalid command format")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change_command(name, phone))
            except ValueError:
                print("Invalid command format")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(phone_command(name))
            except ValueError:
                print("Invalid command format")
        elif command == "show all":
            print(show_all_command())
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()