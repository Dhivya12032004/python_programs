class StockInventory:
    def __init__(self):
        self.stock_items = {}

    def add_item(self, item_id, item_name, item_quantity, item_price):
        if item_id in self.stock_items:
            self.stock_items[item_id]["quantity"] += item_quantity
            print(f"Updated {item_name}: New quantity is {self.stock_items[item_id]['quantity']}")
        else:
            self.stock_items[item_id] = {"name": item_name, "quantity": item_quantity, "price": item_price}
            print(f"Added item: {item_name}")

    def get_item(self, item_id):
        return self.stock_items.get(item_id, "Item not found")

    def get_low_stock_items(self, min_threshold):
        return {item_id: details for item_id, details in self.stock_items.items() if details["quantity"] < min_threshold}

# Usage
inventory = StockInventory()
inventory.add_item(101, "Lap", 15, 45670)
inventory.add_item(102, "Mouse", 25, 1000)
inventory.add_item(103, "Keyboard",10, 2000)

print(inventory.get_item(102))
print(inventory.get_low_stock_items(10))
