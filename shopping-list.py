shopping_list = []
def show_help():
    print('\nWhat do you want to pick up?')
    print("""
        Enter 'Done' to stop adding items.
        Enter 'Show' to see your list of items.
        """)
def show_list():
    print('Here is what a;; you have in your shopping list')

    for item in shopping_list:
        print(item)

def add_food_to_list(new_item):
    shopping_list.append(new_item)
    print('Added {}. Your shopping list now has {} item(s).'.format(new_item, len(shopping_list)))







show_help()

while True:
    new_item = input(' > ')
    if new_item == 'Done':
        show_list()
        break
    elif new_item == 'Show':
        show_list()
        continue
    add_food_to_list(new_item)