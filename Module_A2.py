class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured): #Intializies all the attributes of the class
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured

    def getProductcode(self): #Gets the product_code
        return self.product_code #Returns the product name
    
    def getProductname(self): #Gets the product_name
        return self.product_name #Returns the product name
    
    def getSaleprice(self):#Gets the sale_price
        return self.sale_price #Returns the product name
    
    def getManufacturecost(self):#Gets the manufacture_cost
        return self.manufacture_cost #Returns the product name
    
    def getStocklevel(self):#Gets the stock_level
        return self.stock_level #Returns the product name
    
    def getMonthlyunits(self):#Gets the monthly_units_manufactured)
        return self.monthly_units_manufactured #Returns the product name
