class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients


class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def remove_item(self, item):
        self.menu_items.remove(item)

    def get_items(self):
        return self.menu_items


class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total


class Table:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def vacate(self):
        self.is_occupied = False


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def take_order(self, table, order):
        if table.is_occupied:
            print("Table is already occupied.")
        else:
            table.occupy()
            print(f"Order taken by {self.name} for Table {table.number}.")

    def serve_order(self, table, order):
        if not table.is_occupied:
            print("Table is not occupied.")
        else:
            table.vacate()
            print(f"Order served by {self.name} for Table {table.number}.")


menu = Menu()

item1 = MenuItem("Burger", 10, ["Bun", "Beef Patty", "Lettuce", "Tomato"])
item2 = MenuItem("Pizza", 15, ["Dough", "Tomato Sauce", "Cheese", "Pepperoni"])
item3 = MenuItem("Salad", 8, ["Lettuce", "Tomato", "Cucumber", "Dressing"])

menu.add_item(item1)
menu.add_item(item2)
menu.add_item(item3)

table1 = Table(1, 4)
table2 = Table(2, 6)

staff1 = Staff("John", "Waiter")
staff2 = Staff("Emily", "Waitress")

order1 = Order(table1.number)
order1.add_item(item1)
order1.add_item(item3)

staff1.take_order(table1, order1)
staff2.serve_order(table1, order1)

print(f"Total bill for Table {table1.number}: ${order1.calculate_total()}")


