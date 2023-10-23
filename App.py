class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured

    def getProduct(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured)
        product = Product.append
        return product

    def getProductinput(self):
        product_name = input("Enter Product Name: ")    
        sale_price = float(input("Enter Product Sale Price: "))
        manufacture_cost = float(input("Enter Product Manufacture Cost: "))
        stock_level = int(input("Enter Stock Level: "))
        monthly_units_manufactured = int(input("Enter Estimated Monthly Units Manufactured: "))
        while True:
            product_code = int(input("Enter Product Code (100 to 1000): "))
            if 100 <= product_code <= 1000:
                break
            else:
                print("Invalid input. Product code must be between 100 and 1000.")
        
        return product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured
    
    
class Bonus:    
    
    def getProductsale(self,product_code,units_to_sell):
        #ensure the stock never goes negative while processing a sale
        product_code = int(input("Enter Product Code to sell: "))
        units_to_sell = int(input("Enter the number of units to sell: "))
        for product in product_code:
            if product == product_code:
                if product >= units_to_sell:
                    product -= units_to_sell
                    return True
                else:
                    print("Not enough stock available to complete the sale.")
                    return False
        print("Product not found.")
        return False