class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0.0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

class ShoppingCart(ItemToPurchase):
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        ItemToPurchase.__init__(self)
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, new_item):
        self.cart_items.append(new_item)

    def remove_item(self):
        #module 8
        '''Removes item from cart_items list. 
        Has a string (an item's name) parameter. 
        Does not return anything.
        If item name cannot be found, output this message: 
            Item not found in cart. Nothing removed.'''

    def modify_item(self):
        #module 8
        '''Modifies an item's description, price, and/or quantity. 
        Has parameter ItemToPurchase. Does not return anything.
        If item can be found (by name) in cart, 
            check if parameter has default values for description, 
            price, and quantity. 
        If not, modify item in cart.
        If item cannot be found (by name) in cart, output this message: 
            Item not found in cart. Nothing modified.'''

    def get_num_items_in_cart(self):
        total = 0
        for i in self.cart_items:
            self.item_quantity = int(i.item_quantity)
            total += self.item_quantity
        return total

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            self.item_price = i.item_price
            self.item_quantity = i.item_quantity
            total_cost = total_cost + (self.item_price * self.item_quantity)
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY\n')
        else:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}\n')
            for item in self.cart_items:
                print(f'{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}')
            print(f'Total: ${self.get_cost_of_cart()}')

    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print("Item Descriptions")
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')

def print_menu():
    print('Menu')
    print('a - Add item to cart')#to be done in module 8
    print('r - Remove item from cart')#to be done in module 8
    print('c - Change item quantity')#to be done in module 8
    print('i - Output items descriptions')#done
    print('o - Output shopping cart')#do
    print('q - Quit')#done
if __name__ == '__main__':
    print('Test output to see if program is running')
    choice = ('')
    choices = ["a", "r", "c", "i", "o", "q"]
    customer_name = input('Enter Name: ')
    current_date = input('Enter Date: ')
    print('')

    shopping_cart = ShoppingCart(customer_name, current_date)
    print(f'{shopping_cart.customer_name} - {shopping_cart.current_date}')

    print_menu()
    print('')

    while True:
        choice = input('Choose an option: \n')
        if choice == 'q':
            print('Good Bye!')
            break
        else:
            if choice in choices:
                if choice == 'a':
                    print("ADD ITEM TO CART")
                    item_name = input("Enter the item name:\n")
                    item_quantity = input("Enter the item quantity:\n")
                    item_price = input("Enter the item price:\n")
                    item_desc = input("Enter the item description:\n")
                    item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
                    shopping_cart.add_item(item)
                elif choice == 'r':
                    break
                elif choice == 'c':
                    break
                elif choice == 'i': 
                    print('OUTPUT ITEMS DESCRIPTIONS')
                    shopping_cart.print_descriptions()
                elif choice == 'o': 
                    print('OUTPUT SHOPPING CART')
                    shopping_cart.print_total()
            else:
                print('Please choose one of the options! \n')





