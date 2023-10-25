from Module_A2 import Product
import random
class Application(Product):
    def __init__(self, product_code = 0, product_name = None, sale_price = 0, manufacture_cost = 0, stock_level = 0, monthly_units_manufactured = 0):
        # Created Application class that takes the attributes from the 'Product' Class, and empty base variables for the Application class to use in future methods.
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured    
    
    '''
    This method is to set the product information. It uses the details entered by the end user to create a product instance.
    It allows validation and repeated inputs for all class attributes to ensure the user inputs are approperiate and within a correct value/range.
    It additionally provides the user the monthly production and monthly sale and stock information
    Lastly, it provides a predicted stock statement as well as a net profit statement.
    '''
    def setProductinfo():
        print("♥ Welcome to Maryam's Sample Product Inventory ♥")
        product_name = input("Enter Product Name: ") #Prompts the user to enter product name.
        
        sale_price = float(input("Enter Product Sale Price: ")) # Prompts the user to enter the product sale price.
        if sale_price > 0: #Validates that the user input is a greater than zero
            pass
        else: #If the number is not greater than 0, it prompts the user to enter again, with instructions.
            print("Invalid input. Sale Price must be greater than 0.")
            sale_price = float(input("Enter Product Sale Price: "))

        manufacture_cost = float(input("Enter Product Manufacture Cost: ")) #Prompts the user to enter manufacturing costs.
        if manufacture_cost > 0: #Validates that the user input is a greater than zero
            pass
        else: #If the number is not greater than 0, it prompts the user to enter again, with instructions.
            print("Invalid input. Manufacturing Cost must be greater than 0.")
            manufacture_cost = float(input("Enter Product Manufacture Cost: "))
        

        stock_level = int(input("Enter Stock Level: ")) #Prompts the user to enter the stock level.
        if stock_level > 0: #Validates that the user input is a greater than zero
            pass
        else: #If the number is not greater than 0 and not an integer, it prompts the user to enter again, with instructions stating that it must be an integer.
            print("Invalid input. Manufacturing Cost must be greater than 0, while being an integer.")
            stock_level = int(input("Enter Stock Level: "))
        
        
        monthly_units_manufactured = int(input("Enter Estimated Monthly Units Manufactured: ")) #Prompts the user to enter Monthly Units Manufactured.
        if monthly_units_manufactured >= 0: #Ensure that the monthly units manufactured is greater than or equal to 0.
            pass
        else: #Ensures that the if parameters are true, if not, it provides a user a prompt to enter it again.
            print("Please Enter a valid Estimate of Monthly Units Manufactured. Must be an integer greater than or equal to 0.")
            monthly_units_manufactured = int(input("Enter Estimated Monthly Units Manufactured: "))           


        product_code = int(input("Enter Product Code (100 to 1000): ")) #Prompts the user to enter a Product code.
        if 100 <= product_code <= 1000: #Ensures the product code is a valid number between 100-1000
            pass
        else: #If not validated, provides user prompt to re-enter.
            print("Invalid input. Product code must be between 100 and 1000.")
            product_code = int(input("Enter Product Code (100 to 1000): "))

        sampleproduct = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured) #Created an instannce of the method setProductinfo(), that uses the Class 'Product', and provides it it's respected attributes in order to utilize the methods in the class 'Product' in future functions.
        print("♥ Maryam's Sample Stock Statement ♥ ") 
        # The following print statements use dot notation to use methods from 'Product' Class
        print("Product Code: ", sampleproduct.getProductcode()) #Displays the product code
        print("Product Name: ", sampleproduct.getProductname()) #Displays the product name
        print("Sale Price: ", sampleproduct.getSaleprice())#Displays the sale price
        print("Manufacture Cost: ", sampleproduct.getManufacturecost())#Displays the manufacturing cost
        print("Stock Level:" , sampleproduct.getStocklevel())#Displays the stock level
        print("Estimated Monthly Units Manufactured:" , sampleproduct.getMonthlyunits())#Displays the monthly units manufactured
        
        unfilled_sales = []  # Create a list to store details of sales that could not be fulfilled


        for month in range(1,13): #For loop for the months, ensuring to simultaneously print every month's production
            stock_value = monthly_units_manufactured + stock_level #Adds monthly units manufactured to the actual stock value
            lower_bound = max(1, monthly_units_manufactured - 10) #Creates a max and min for the sale units object
            upper_bound = min(monthly_units_manufactured + 10, monthly_units_manufactured)
            sale_units = random.randint(lower_bound, upper_bound) #Estimates the units sold
            
            
            
            stock_calculated = stock_value - sale_units #Shows the updated and calculated stock level
            


            print(f"Month {month} :" ) #Displays Months
            print("Manufactured: ",monthly_units_manufactured, "units") # Displays manufactured units
            print("Sold:", sale_units, "units")  #Displays sold units
            print("Stock: ", stock_calculated, "units") # Displays stock units
            stock_calculated = stock_value - sale_units #Updates the stock for the following months
        
            yearly_manufature_profits =+ monthly_units_manufactured #Adds and updates the units manufactured
            yearly_sale_profits =+ sale_units #Adds and updates the units sold
        net_profit = (yearly_sale_profits * sale_price) - (yearly_manufature_profits * manufacture_cost) #Calculates net profit
        rounded = round(net_profit, 2) #Rounds the net profit to 2 decimal places.
        print("Net Profit: $", rounded, "CAD") #Displays net profit


product_execution = Application.setProductinfo() #Object of the class
print(product_execution) #Prints the object, allowing for user interaction.