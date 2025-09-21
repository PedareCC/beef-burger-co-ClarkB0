from os import system, name
from datetime import datetime
from pytz import timezone

drinks = {'Taro': 4.49, 'Peach': 4.99, 'Brown Sugar': 2.99, 'Coffee': 3.99, 'Black Tea': 3.49, 'Coconut': 3.99, 'Caramel': 3.99}
pearls = {'Brown Sugar': 1.99, 'Plain': 1.49, 'Strawbery': 2.49, 'Mango': 2.49, 'None': 0}
extras = {'Grass Jelly': 0.99, 'Coffee Jelly': 0.99, 'Lychee Jelly': 1.49, 'Peach Jelly': 1.49, 'None': 0}
sugar = {'1 Teaspoon': 0, '2 Teaspoons': 0, '3 Teaspoons': 0, '4 Teaspoons': 0}
ice = {'No Ice': 0, 'Moderate Ice': 0, 'Extra Ice': 0}
drink_parts_options = {'drink': list(drinks.keys()), 'pearls': list(pearls.keys()), 'extras': list(extras.keys()), 'sugar amount':list(sugar.keys()), 'ice amount': list(ice.keys())}
drink_parts_prices = [drinks, pearls, extras, sugar, ice]

date_format = '%Y-%m-%d %H:%M:%S'
local_timezone = timezone('Australia/Adelaide')

def clear():
    system('cls' if name == 'nt' else 'clear')

def display_options(options):
    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')

def wait():
    print('Press enter to continue.')
    input()
    clear()

def select_option(prompt, options):
    valid = False
    valid_options = [str(i) for i in range(1, len(options) + 1)]
    while not valid:
        print(prompt)
        display_options(options)
        choice = input()
        if choice == 'x':
            return choice
        elif choice not in valid_options:
            print('Invalid option.')
            wait()
        else:
            valid = True
            return int(choice) - 1

def create_drink(parts):
    drink = []
    for part in parts:
        option = select_option(f'Create Drink\n------------\nSelect {part}:', parts[part])
        clear()
        if option == 'x':
            return False
        else:
            option = parts[part][option]
            drink.append(option)
    return drink


clear()
running = True
while running:
    action = select_option('Main Screen\n-----------\nWhat would you like to do?\nEnter x at anytime to cancel or exit.', ['create new order'])
    clear()
    if action == 'x':
        running = False
    else:
        print('Order Screen')
        print('------------')
        print('Enter customer name: ')
        order = {'drinks': []}
        order['name'] = input()
        clear()
        add_order = True
        while add_order:
            action = select_option('Order Screen\n------------\nWhat would you like to do?', ['add new drink', 'finish order'])
            clear()
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
                        print('Create Drink')
                        print('------------')
                        print('Drink Added to Order:')
                        print(f'{', '.join(drink['parts'])}: ${drink['price']:.2f}')
                        wait()
            elif action == 1:
                total = 0
                for drink in order['drinks']:
                    total += drink['price']
                order_print = f'Name: {order['name']}\nDrinks:\n{'\n'.join([f'- {', '.join(drink['parts'])}: ${drink['price']:.2f}' for drink in order['drinks']])}\nTotal: ${total:.2f}'
                action = select_option(f'Order\n-----\n{order_print}\n', ['transaction approved', 'transaction failed/cancelled'])
                if action == 0:
                    local_datetime = datetime.now().astimezone(local_timezone).strftime(date_format)
                    with open('OrderLog.txt', 'a') as file:
                        file.write(f'{local_datetime}\n{order_print}\n\n')
                    print('(placeholder) recepit, log, stuff')
                    wait()
                else:
                    print('(placeholder) order cancelled')
                    wait()
                clear()
                add_order = False