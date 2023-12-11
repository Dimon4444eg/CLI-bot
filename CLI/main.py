contacts = {}

def input_error(funk):
    def wrapper(*args, **kwargs):
        try:
            result = funk(*args, **kwargs)
            return result
        except KeyError as e:
            return f"KeyError: {e}"
        except ValueError as e:
            return f"ValueError: {e}"
        except IndexError as e:
            return f"IndexError: {e}"
        except Exception as e:
            return f"Exception: {e}"
    return wrapper


@input_error
def hello_handler(args):
    return "How can I help you?"


@input_error
def add_handler(args):
    if len(args) == 0:
        return "There are no arguments"

    name, phone = args.split()
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} added successfully."


@input_error
def change_handler(args):
    if len(args) == 0:
        return "There are no arguments"

    name, phone = args.split()
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact {name} changed to {phone}."
    else:
        return "Contact not found."


@input_error
def phone_handler(args):
    if len(args) == 0:
        return "There are no arguments"

    if args in contacts:
        return f"The phone number for {args} is {contacts[args]}."
    else:
        return "Contact not found."

@input_error
def show_all_handler(args):
    if len(args) == 0:
        return "There are no arguments"

    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts available."


@input_error
def exit_handler(args):
    return "Good bye!"


def main():
    table = {
        "add": add_handler,
        "change": change_handler,
        "hello": hello_handler,
        "phone": phone_handler,
        "show": show_all_handler,
        "exit": exit_handler,
        "close": exit_handler,
        "good bye": exit_handler
    }
    while True:
        user_input = input(">>> ").lower()
        first_name = user_input.find(" ")
        handler_name = user_input[:first_name]
        args = user_input[first_name:].strip()

        if handler_name in table:
            result = table[handler_name](args)
            if result is not None:
                if handler_name in ["good bye", "close", "exit"]:
                    print(result)
                    break
                else:
                    print(result)



if __name__ == "__main__":
    main()