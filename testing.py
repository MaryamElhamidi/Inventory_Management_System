from Module_A2 import Product

def getProductinput():

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

    product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured)
    print("Product Code: ", product.getProductcode())
    print("Product Name: ", product.getProductname())
    print("Sale Price: ", product.getSaleprice())
    print("Manufacture Cost: ", product.getManufacturecost())
    print("Stock Level:" , product.getStocklevel())
    print("Estimated Monthly Units Manufactured:" , Product.getMonthlyunits())


print(getProductinput())