class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor:
        def pay_debit(self, order, security_code):                
                print("Processing debit payment type")
                print(f"Verifying security code: {security_code}")
                order.status = "paid"
                
        def pay_credit(self, order, security_code):                
                print("Processing credit payment type")
                print(f"Verifying security code: {security_code}")
                order.status = "paid"
                
order = Order()
order.add_item("keyboard",1,50)                
order.add_item("SSD",1,150)                
order.add_item("USB Cable",1,5)                
                
payment_processor = PaymentProcessor()
payment_processor.pay_debit(order,'464646535121')
            