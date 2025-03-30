def calculate_discount(price,discount_percentage):
    if discount_percentage > 20  :
        discount = price * (discount_percentage/100)
        return price - discount
    else:
            return price
    
print(calculate_discount(100, 57))  
