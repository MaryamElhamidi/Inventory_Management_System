class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured

class Application:
    def __init__(self):
        self.products = []  # List to store product instances

    def create_product(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured)
        self.products.append(product)

    def simulate_production_and_sales(self):
        # Implement simulation logic here

    def generate_stock_statement(self):
        # Implement stock statement generation here

    def run(self):
        # Main application logic