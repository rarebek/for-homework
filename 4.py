class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class ShoppingCart:
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


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_item(product, quantity)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_item(product)

    def calculate_cart_total(self):
        return self.shopping_cart.calculate_total()


product1 = Product("Product 1", 10)
product2 = Product("Product 2", 20)

customer = Customer("John Doe", "john@example.com")

customer.add_to_cart(product1, 2)
customer.add_to_cart(product2, 1)

cart_total = customer.calculate_cart_total()
print(f"Cart Total: ${cart_total}")