class ItemToPurchase:
	
    def __init__(self, item_name = 'none', item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def item_total(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price*self.item_quantity}'

item_1 = ItemToPurchase(input('Enter Item Name: '), float(input('Please Enter Price: ')), int(input('Please Enter Amount: ')))
print('')
item_2 = ItemToPurchase(input('Enter Item Name: '), float(input('Please Enter Price: ')), int(input('Please Enter Amount: ')))
print('')

print('TOTAL COST\n')
print(item_1.item_total(), '\n')
print(item_2.item_total(), '\n')
print('Total: ${}'.format((item_1.item_price * item_1.item_quantity) + (item_2.item_price * item_2.item_quantity)))


