class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price
    
    def remove_item(self, item_name):
        del self.items[item_name]

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Item '{item_name}' not found in the store.")
    
    def get_item_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in the store.")
            return None
    
    def show_items(self):
        print(f'\nItems in {self.name} ({self.address}):')
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

# Создание объектов магазинов  
store_1 = Store("Apple Store", "123 Main St")
store_1.add_item("iPhone", 10.99)
store_1.add_item("MacBook Pro", 999.99)
store_1.add_item("iWatch", 399.99)

store_2 = Store("Amazon", "456 Pennsylvania St")
store_2.add_item("Echo Dot", 49.99)
store_2.add_item("Fire TV Stick", 249.99)
store_2.add_item("Fire TV", 299.99)

store_3 = Store("Grocery Store", "78 Denver St")
store_3.add_item("Milk", 3.99)
store_3.add_item("Eggs", 2.99)
store_3.add_item("Bread", 1.99)

# Использование методов магазинов
store_3.add_item("Butter", 5.99)
store_3.update_item_price("Eggs", 3.99)
store_3.remove_item("Bread")

store_1.show_items()
store_2.show_items()
store_3.show_items()