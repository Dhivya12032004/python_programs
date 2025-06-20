class Product:
    def __init__(self, prod_id, prod_name, prod_price):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.prod_price = prod_price

    def show_details(self):
        return f"Product ID: {self.prod_id}, Name: {self.prod_name}, Price: ₹{self.prod_price}"

class TransactionLogger:
    def __init__(self):
        self.transactions = []

    def log_transaction(self, product, units_sold):
        sale_amount = product.prod_price * units_sold
        self.transactions.append({
            "product": product,
            "units": units_sold,
            "amount": sale_amount
        })
        print(f"Transaction: {product.prod_name} × {units_sold} = ₹{sale_amount}")

    def total_earnings(self):
        return sum(txn["amount"] for txn in self.transactions)

    def print_report(self):
        report = "Transaction Report:\n"
        for txn in self.transactions:
            report += f"{txn['product'].prod_name}: {txn['units']} units sold - ₹{txn['amount']}\n"
        return report

# Usage
if __name__ == "__main__":
    prod1 = Product(101, "Tablet", 25000)
    prod2 = Product(102, "Smartwatch", 10000)

    sales_logger = TransactionLogger()
    sales_logger.log_transaction(prod1, 4)
    sales_logger.log_transaction(prod2, 6)

    print("\n" + sales_logger.print_report())
    print(f"Total Earnings: ₹{sales_logger.total_earnings()}")
