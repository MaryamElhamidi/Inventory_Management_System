class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured

    def create_product(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured)
        self.products.append(product)

    def getProductinput():
        product_name = input("Enter Product Name: ")    
        while True:
            product_code = int(input("Enter Product Code (100 to 1000): "))
            if 100 <= product_code <= 1000:
                break
            else:
                print("Invalid input. Product code must be between 100 and 1000.")
        return product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured
