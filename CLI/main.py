contacts = {}

def input_error(funk):
    def wrapper(*args, **kwargs):
        try:
            result = funk(*args, **kwargs)
            return result
        except KeyError as e:
            print(f"KeyError: {e}")
        except ValueError as e:
            print(f"ValueError: {e}")
        except IndexError as e:
            print(f"IndexError: {e}")
        except Exception as e:
            print(f"Exception: {e}")
    return wrapper


@input_error
def hello_handler(args):
    if len(args) == 0:
        print("There are no arguments")
        return
    print("How can I help you?")


@input_error
def add_handler(args):
    if len(args) == 0:
        print("There are no arguments")
        return
    name, phone = args.split()
    contacts[name] = phone
    print(f"Contact {name} with phone number {phone} added successfully.")


@input_error
def change_handler(args):
    if len(args) == 0:
        print("There are no arguments")
        return
    name, phone = args.split()
    if name in contacts:
        contacts[name] = phone
        print(f"Phone number for contact {name} changed to {phone}.")
    else:
        print("Contact not found.")


@input_error
def phone_handler(args):
    if len(args) == 0:
        print("There are no arguments")
        return
    if args in contacts:
        print(f"The phone number for {args} is {contacts[args]}.")
    else:
        print("Contact not found.")

@input_error
def show_all_handler(args):
    if len(args) == 0:
        print("There are no arguments")
        return
    if contacts:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")


@input_error
def exit_handler(args):
    print("Good bye!")
    quit()

def main():
    table = {
        "add": add_handler,
        "change": change_handler,
        "hello": hello_handler,
        "phone": phone_handler,
        "show": show_all_handler,
        "exit": exit_handler
    }
    while True:
        user_input = input(">>> ")
        first_name = user_input.find(" ")
        handler_name = user_input[:first_name]
        args = user_input[first_name:].strip()

        if table.get(handler_name) is not None:
            table[handler_name](args)


if "__name__" == "__main__":
    main()