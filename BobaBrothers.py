# Menu System
# File logging with time and order status
# Cancelled, success, etc.

drinks = {'Taro': 4, 'Peach': 4, 'Brown Sugar': 4, 'Coffee': 4, 'Lychee': 4, 'White Tea': 4, 'Black Tea': 4, 'Coconut': 4, 'Guava': 4, 'Almond': 4, 'Caramel': 4}
pearls = {'Brown Sugar': 2, 'Plain': 2, 'Strawbery': 2, 'Mango': 2, 'None': 0}
extras = {'Grass Jelly': 2, 'Coffee Jelly': 2, 'Lychee Jelly': 2, 'Peach Jelly': 2, 'None': 0}
sugar = {'1 Teaspoon': 0, '2 Teaspoons': 0, '3 Teaspoons': 0, '4 Teaspoons': 0}
ice = {'No Ice': 0, 'Moderate Ice': 0, 'Extra Ice': 0}
drink_parts = {'drink': list(drinks.keys()), 'pearls': list(pearls.keys()), 'extras': list(extras.keys()), 'sugar amount':list(sugar.keys()), 'ice amount': list(ice.keys())}

def display_options(options):
    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')

def select_option(options):
    # global loop variable shenanigans later
    display_options(options)
    valid = False
    valid_options = [str(i) for i in range(1, len(options) + 1)]
    while not valid:
        choice = input()
        if choice == 'x':
            return choice
        elif choice not in valid_options:
            print('Invalid option')
        else:
            valid = True
            return int(choice) - 1

def create_drink(parts):
    drink = []
    for part in parts:
        print(f'Select {part}')
        option = select_option(parts[part])
        if option == 'x':
            return False
        else:
            option = parts[part][option]
            print()
            drink.append(option)
    return drink

running = True
while running:
    print('What would you like to do?')
    print('enter x at anytime to go back or exit')
    action = select_option(['create new order'])
    print()
    if action == 'x':
        running = False
    else:
        order = {'drinks': []}
        print('Enter customer name: ')
        order['name'] = input()
        print()
        add_order = True
        while add_order:
            print('What would you like to do?')
            action = select_option(['create new drink', 'finish order'])
            print()
            if action == 0:
                drink = create_drink(drink_parts)
                if drink:
                    order['drinks'].append(drink)
            elif action == 1:
                print(order)
                add_order = False