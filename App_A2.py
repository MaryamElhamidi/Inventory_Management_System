class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured



    def getProductinput(self):
        product_name = input("Enter Product Name: ")
        if product_name.isalpha():
            pass
        else:
            print("Please enter a valid name. Must be a string")
            product_name = input("Enter Product Name: ")


        sale_price = input("Enter Product Sale Price: ")
        if type(sale_price) == float:
            pass
        else:
            print("Please Enter a valid Sale Price. Must be a float.")
            sale_price = input("Enter Product Sale Price: ")        


        manufacture_cost = input("Enter Product Manufacture Cost: ")
        if type(manufacture_cost) == float:
            pass
        else:
            print("Please Enter a Valid Manufacture Cost. Must be a float.")
            manufacture_cost = input("Enter Product Manufacture Cost: ")    


        stock_level = input("Enter Stock Level: ")
        if type(stock_level) == int:
            pass
        else:
            print("Please Enter a valid Stock Level. Must be an integer.")
            stock_level = input("Enter Stock Level: ")    
        
        monthly_units_manufactured = input("Enter Estimated Monthly Units Manufactured: ")
        if type(monthly_units_manufactured) == int:
            pass
        else:
            print("Please Enter a valid Estimate of Monthly Units Manufactured. Must be an integer.")
            monthly_units_manufactured = input("Enter Estimated Monthly Units Manufactured: ")           
        
        product_code = int(input("Enter Product Code (1 to 1000): "))
        if 1 <= product_code <= 1000:
            pass
        else:
            print("Invalid input. Product code must be between 1 and 1000, that is an integer.")
            product_code = int(input("Enter Product Code (1 to 1000): "))
    
        
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
                    print(f"Sale of {units_to_sell} units of {Product.product_name} successful.")
                    return True
                else:
                    choice = input(f"Not enough stock available to sell {units_to_sell} units. Do you want to sell {Product.stock_level} units instead? (y/n): ")
                    if choice.lower() == 'y':
                        Product.stock_level = 0
                        print(f"Sale of {Product.stock_level} units of {Product.product_name} successful.")
                    else:
                        print("Sale declined.")
                        return False
        print("Product not found.")
