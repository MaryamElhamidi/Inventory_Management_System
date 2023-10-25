from Module_A2 import Product

def getProductinput():

    product_name = input("Enter Product Name: ")
    print("Product Name: ", Product.getProductname())


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
        print("Product code: ", product_code.getProductcode())
        pass
    else:
        print("Invalid input. Product code must be between 1 and 1000, that is an integer.")
        product_code = int(input("Enter Product Code (1 to 1000): "))
#return product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured
print(getProductinput())