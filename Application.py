from Module_A2 import Product
import random
class Application(Product):
    def __init__(self, product_code = 0, product_name = None, sale_price = 0, manufacture_cost = 0, stock_level = 0, monthly_units_manufactured = 0):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured    
    def setProductinfo():
        print("♥ Welcome to Maryam's Sample Product Inventory ♥")
        product_name = input("Enter Product Name: ")

        sale_price = float(input("Enter Product Sale Price: "))
        if sale_price > 0:
            pass
        else:
            print("Invalid input. Sale Price must be greater than 0, while being an integer.")
            sale_price = float(input("Enter Product Sale Price: "))

        manufacture_cost = float(input("Enter Product Manufacture Cost: "))
        if manufacture_cost > 0:
            pass
        else:
            print("Invalid input. Manufacturing Cost must be greater than 0, while being an integer.")
            manufacture_cost = float(input("Enter Product Manufacture Cost: "))
        

        stock_level = int(input("Enter Stock Level: "))
        if stock_level > 0:
            pass
        else:
            print("Invalid input. Manufacturing Cost must be greater than 0, while being an integer.")
            stock_level = int(input("Enter Stock Level: "))
        
        
        monthly_units_manufactured = int(input("Enter Estimated Monthly Units Manufactured: "))
        if monthly_units_manufactured >= 0:
            pass
        else:
            print("Please Enter a valid Estimate of Monthly Units Manufactured. Must be an integer greater than or equal to 0.")
            monthly_units_manufactured = int(input("Enter Estimated Monthly Units Manufactured: "))           


        product_code = int(input("Enter Product Code (100 to 1000): "))
        if 100 <= product_code <= 1000:
            pass
        else:
            print("Invalid input. Product code must be between 100 and 1000.")
            product_code = int(input("Enter Product Code (100 to 1000): "))

        sampleproduct = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured)
        print("♥ Maryam's Sample Stock Statement ♥ ")

        print("Product Code: ", sampleproduct.getProductcode())
        print("Product Name: ", sampleproduct.getProductname())
        print("Sale Price: ", sampleproduct.getSaleprice())
        print("Manufacture Cost: ", sampleproduct.getManufacturecost())
        print("Stock Level:" , sampleproduct.getStocklevel())
        print("Estimated Monthly Units Manufactured:" , sampleproduct.getMonthlyunits())
        
        
        
        for month in range(1,13):
            stock_value = monthly_units_manufactured + stock_level
            lower_bound = max(1, monthly_units_manufactured - 10)
            upper_bound = min(monthly_units_manufactured + 10, monthly_units_manufactured)
            sale_units = random.randint(lower_bound, upper_bound)
            stock_calculated = stock_value - sale_units

            print(f"Month {month} :" )
            print("Manufactured: ",monthly_units_manufactured, "units") 
            print("Sold:", sale_units, "units")  
            print("Stock: ", stock_calculated, "units")
            stock_calculated = stock_value - sale_units
        
            yearly_manufature_profits =+ monthly_units_manufactured
            yearly_sale_profits =+ sale_units
        net_profit = (yearly_sale_profits * sale_price) - (yearly_manufature_profits * manufacture_cost)
        rounded = round(net_profit, 2)
        print("Net Profit: $", rounded, "CAD")


product_execution = Application.setProductinfo()
print(product_execution)
