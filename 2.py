class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary method")


class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Developer(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Salesperson(Employee):
    def __init__(self, name, employee_id, base_salary, commission_rate, sales_amount):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount

    def calculate_salary(self):
        return self.base_salary + (self.commission_rate * self.sales_amount)


manager = Manager("John Doe", 123, 5000)
developer = Developer("Jane Smith", 456, 50, 160)
salesperson = Salesperson("Mike Johnson", 789, 2000, 0.1, 100000)

employees = [manager, developer, salesperson]

for employee in employees:
    print(f"{employee.name}: {employee.calculate_salary()}")