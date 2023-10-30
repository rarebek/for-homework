class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class StockLevel:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Insufficient stock.")


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].get_price() * item["quantity"]
        return total


class InventoryTrackingSystem:
    def __init__(self):
        self.stock_levels = []

    def add_stock_level(self, stock_level):
        self.stock_levels.append(stock_level)

    def remove_stock_level(self, stock_level):
        self.stock_levels.remove(stock_level)

    def restock_product(self, product, quantity):
        for stock_level in self.stock_levels:
            if stock_level.get_product() == product:
                stock_level.increase_quantity(quantity)
                break
        else:
            new_stock_level = StockLevel(product, quantity)
            self.stock_levels.append(new_stock_level)

    def process_order(self, order):
        for item in order.items:
            product = item["product"]
            quantity = item["quantity"]
            for stock_level in self.stock_levels:
                if stock_level.get_product() == product:
                    stock_level.decrease_quantity(quantity)
                    break

    def generate_report(self):
        for stock_level in self.stock_levels:
            product = stock_level.get_product()
            quantity = stock_level.get_quantity()
            print(f"Product: {product.get_name()}, Quantity: {quantity}")


inventory_system = InventoryTrackingSystem()

product1 = Product("Shirt", 20)
product2 = Product("Pants", 30)

stock_level1 = StockLevel(product1, 10)
stock_level2 = StockLevel(product2, 5)

inventory_system.add_stock_level(stock_level1)
inventory_system.add_stock_level(stock_level2)

order = Order()
order.add_item(product1, 2)
order.add_item(product2, 1)

inventory_system.process_order(order)

inventory_system.restock_product(product1, 5)

inventory_system.generate_report()
