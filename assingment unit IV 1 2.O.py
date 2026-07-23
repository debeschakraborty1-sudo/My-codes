# Smart Inventory System using Classes, Inheritance, and Polymorphism

from datetime import datetime

# Base Class
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    # Method to update stock
    def update_stock(self, quantity):
        self.stock += quantity
        print(f"Updated stock for {self.name}: {self.stock}")

    # Method to apply discount
    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
        print(f"New price of {self.name} after {percent}% discount: ₹{self.price:.2f}")

    # Method to display details
    def display(self):
        print("\nProduct Details")
        print("----------------------")
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ₹{self.price:.2f}")
        print(f"Stock      : {self.stock}")


# Subclass using Inheritance
class PerishableProduct(Product):
    def __init__(self, product_id, name, price, stock, expiry_date):
        super().__init__(product_id, name, price, stock)
        self.expiry_date = expiry_date

    # Overriding method (Polymorphism)
    def apply_discount(self, percent):
        today = datetime.today().date()
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()

        # Extra discount if product is near expiry
        days_left = (expiry - today).days

        if days_left <= 5:
            percent += 10
            print(f"{self.name} is near expiry! Extra 10% discount applied.")

        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

        print(f"New price of {self.name}: ₹{self.price:.2f}")

    
    def display(self):
        super().display()
        print(f"Expiry Date: {self.expiry_date}")



p1 = Product(101, "Laptop", 50000, 10)
p2 = Product(102, "Keyboard", 1500, 25)
p3 = PerishableProduct(201, "Milk", 60, 40, "2026-05-15")



p1.display()
p2.display()
p3.display()



print("\n--- Real-Time Inventory Updates ---")


p1.update_stock(-2)   
p2.update_stock(10)   
p3.update_stock(-5)   


p1.apply_discount(5)
p2.apply_discount(10)
p3.apply_discount(15)   



print("\n--- Final Inventory Status ---")
p1.display()
p2.display()
p3.display()
