# Menu System
# File logging with time and order status
# Cancelled, success, etc.

drinks = {'Taro': 4, 'Peach': 4, 'Brown Sugar': 4, 'Coffee': 4, 'Lychee': 4, 'White Tea': 4, 'Black Tea': 4, 'Coconut': 4, 'Guava': 4, 'Almond': 4, 'Caramel': 4}
pearls = {'Brown Sugar': 2, 'Plain': 2, 'Strawbery': 2, 'Mango': 2}
extras = {'Grass Jelly': 2, 'Coffee Jelly': 2, 'Lychee Jelly': 2, 'Peach Jelly': 2}
sugar = {'1 Teaspoon': 0, '2 Teaspoons': 0, '3 Teaspoons': 0, '4 Teaspoons': 0}
ice = {'No Ice': 0, 'Moderate Ice': 0, 'Extra Ice': 0}
drink_parts = [list(drinks.keys()), list(pearls.keys()), list(extras.keys()), list(sugar.keys()), list(ice.keys())]
drink_part_names = ['drink', 'pearls', 'extras', 'sugar amount', 'ice amount']

def display_options(options):
    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')

def exit(user_input):
    if user_input == 'x':
        quit()

print('Order System')

"${:,.2f}".format(2.5)

# Add back button

'''print('What would you like to do?')
display_options(['Create new order'])
running = True
while running:
    action = input()
    print()
    running = action != 'x'
    making_order = True
    if running and action == '1':
        print('What would you like to do? ')
        display_options(['Create new drink', 'Choose drink preset'])
        action = input()
        print()
        running = action != 'x'
        if action == '1':
            drink_order = []
            for i in range(len(drink_parts)):
                if making_order:
                    part = drink_parts[i]
                    print(f'Select {drink_part_names[i]}')
                    display_options(part)
                    valid = False
                    while not valid:
                        try:
                            choice = input()
                            valid = choice == 'x'
                            running = choice != 'x'
                            print()
                            print(len(part))
                            if choice not in range(1, len(part)):
                                print('Invalid input')
                            else:
                                valid = True
                        except:
                            print('Invalid input')'''


def select_option(options):
    # global loop variable shenanigans later
    display_options(options)
    valid = False
    valid_options = [str(i) for i in range(1, len(options) + 1)]
    while not valid:
        choice = input()
        if choice not in valid_options:
            print('Invalid option')
        else:
            valid = True
            return int(choice) - 1


def create_drink(parts):
    for part in parts:
        select_option(part)