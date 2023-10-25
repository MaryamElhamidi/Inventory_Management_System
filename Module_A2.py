class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured

    def getProductcode(self):
        return self.product_code 
    
    def getProductname(self):
        return self.product_name
    
    def getSaleprice(self):
        return self.sale_price
    
    def getManufacturecost(self):
        return self.manufacture_cost
    
    def getStocklevel(self):
        return self.stock_level
    
    def getMonthlyunits(self):
        return self.monthly_units_manufactured
    
