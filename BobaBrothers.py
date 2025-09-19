# Menu System
# File logging with time and order status
# Cancelled, success, etc.

drinks = {'Taro': 4.49, 'Peach': 4.99, 'Brown Sugar': 2.99, 'Coffee': 3.99, 'Lychee': 4.49, 'White Tea': 3.49, 'Black Tea': 3.49, 'Coconut': 3.99, 'Guava': 4.99, 'Almond': 3.99, 'Caramel': 3.99}
pearls = {'Brown Sugar': 1.99, 'Plain': 1.49, 'Strawbery': 2.49, 'Mango': 2.49, 'None': 0}
extras = {'Grass Jelly': 0.99, 'Coffee Jelly': 0.99, 'Lychee Jelly': 1.49, 'Peach Jelly': 1.49, 'None': 0}
sugar = {'1 Teaspoon': 0, '2 Teaspoons': 0, '3 Teaspoons': 0, '4 Teaspoons': 0}
ice = {'No Ice': 0, 'Moderate Ice': 0, 'Extra Ice': 0}
drink_parts_options = {'drink': list(drinks.keys()), 'pearls': list(pearls.keys()), 'extras': list(extras.keys()), 'sugar amount':list(sugar.keys()), 'ice amount': list(ice.keys())}
drink_parts_prices = [drinks, pearls, extras, sugar, ice]

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
            print('Invalid option\n')
        else:
            valid = True
            return int(choice) - 1

def create_drink(parts):
    drink = []
    for part in parts:
        print(f'Select {part}')
        option = select_option(parts[part])
        print()
        if option == 'x':
            return False
        else:
            option = parts[part][option]
            drink.append(option)
    return drink

running = True
while running:
    print('Main Screen')
    print('-----------')
    print('What would you like to do?')
    print('Enter x at anytime to cancel or exit.')
    action = select_option(['create new order'])
    print()
    if action == 'x':
        running = False
    else:
        print('Order Screen')
        print('------------')
        order = {'drinks': []}
        print('Enter customer name: ')
        order['name'] = input()
        print()
        add_order = True
        while add_order:
            print('What would you like to do?')
            action = select_option(['create new drink', 'finish order'])
            print()
            if action == 'x':
                add_order = False
            elif action == 0:
                drink = {}
                drink_parts = create_drink(drink_parts_options)
                if drink_parts:
                    drink['parts'] = drink_parts
                    drink_price = 0
                    for i in range(len(drink_parts)):
                        drink_price += drink_parts_prices[i][drink_parts[i]]
                    drink['price'] = drink_price
                    if drink:
                        order['drinks'].append(drink)
            elif action == 1:
                print('Order:')
                print(f'Name: {order['name']}')
                for drink in order['drinks']:
                    print(f'Drink: {', '.join(drink['parts'])}: ${drink['price']:.2f}')
                total = 0
                for drink in order['drinks']:
                    total += drink['price']
                print('\nPress enter to continue.')
                input()
                add_order = False
# do chcekcout stuff money pirce