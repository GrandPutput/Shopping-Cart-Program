class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0.0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, new_item):
        self.cart_items.append(new_item)

    def remove_item(self, item_name):
        removed = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                removed = True
                break
        if not removed:
            print("Item not found in cart. Nothing removed.")       

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total = 0
        for i in self.cart_items:
            total += i.item_quantity
        return total

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost = total_cost + (i.item_price * i.item_quantity)
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
    print('a - Add item to cart')#done
    print('r - Remove item from cart')#done
    print('c - Change item quantity')#done
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
                    print('ADD ITEM TO CART')
                    item_name = input('Enter the item name: ')
                    item_quantity = int(input('Enter the item quantity: '))
                    item_price = float(input('Enter the item price: '))
                    item_desc = input('Enter the item description: ')
                    item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
                    shopping_cart.add_item(item)
                elif choice == 'r':
                    print('REMOVE ITEM FROM CART')
                    item_removal = input('Enter name of item to remove:')
                    shopping_cart.remove_item(item_removal)
                elif choice == 'c':
                    print('CHANGE ITEM QUANTITY')
                    item_name = input('Enter the item name: ')
                    new_item_quantity = int(input('Enter the new item quantity: '))
                    new_item = ItemToPurchase(item_name, 0, new_item_quantity)
                    shopping_cart.modify_item(new_item)
                elif choice == 'i': 
                    print('OUTPUT ITEMS DESCRIPTIONS')
                    shopping_cart.print_descriptions()
                elif choice == 'o': 
                    print('OUTPUT SHOPPING CART')
                    shopping_cart.print_total()
            else:
                print('Please choose one of the options! \n')
