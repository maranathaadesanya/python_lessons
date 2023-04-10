MENU = ['abula', 'gbegiri', 'ewedu', 'pounded yam', 'egusi soup', 'ikokore',
        'ekuru', 'dambu nama', 'masa', 'tuwo', 'abacha', 'oha soup', 'ofe nsala', 'isi ewu',
        'kunu', 'zobo', 'fruit', 'juice', 'soda', 'palm wine', 'tea', 'acha', 'tuwo masara', 'edikaikong', 'moimoi']

print("Good day and welcome to XYZ restaurant! We serve:")

# Python program to print the data
d = {'abula': ["dambu nama", 'isi ewu', 'soda'], 'pounded yam': ["masa", 'abacha', 'zobo'],
     'egusi soup': ["tuwo", 'ofe nsala', 'kunu'], 'ikokore': ["kilishi", 'oha soup', 'fruit juice'],
     'ekuru': ["tuwo masara", 'edikaikong', 'tea'], 'moimoi': ["acha", 'ofe onugu', 'palm wine']
     }

print("{:<20} {:<20} {:<20} {:<20}".format('Yoruba dishes', 'Hausa dishes', 'Igbo dishes', 'Drinks'))
for k, v in d.items():
    lang, perc, change = v
    print("{:<20} {:<20} {:<20} {:<20}".format(k, lang, perc, change))


def get_order():
    current_order = []
    while True:
        print("What can I get for you?")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("I'm sorry, we don't serve that.")
            continue
        if is_order_complete():
            return current_order


def is_order_complete():
    print("Anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


def output_order(order_list):
    print("Please confirm your order")
    for order in order_list:
        print(order)


def main():
    while True:
        order = get_order()
        output_order(order)
        print('Is this your order? yes/no')
        choice = input()
        if choice == 'no':
            print("Do you want to place another order? yes/no")
            choice = input()
            if choice != 'yes':
                # code to execute if answer is 'no'
                print("Continuing...")
            else:
                continue
        elif choice == 'yes':
            print('Please be patient, your order is on its way ...')
            break


if __name__ == "__main__":
    main()
