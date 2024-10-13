import math
conversion_rates = {
        'USD': 1.13, 
        'EUR': 1.15,
        'CAD': 1.80,
        'JPY': 194.46,
        'CHS': 1.12
        }
    
def check_currency_exists(currency):
    while True:
        if currency not in conversion_rates:
            return "Your currency is not a currency we can convert to. Please use either USD, EUR, CAD JPY or CHS. "
        else:
            return f"Your currency {currency} can be converted to by our software. "
            
def currency_converter(amount,new_c):
    og_c = 1.00
    if new_c not in conversion_rates:
        return "Invalid currency provided"
    converted_amount = amount * (conversion_rates[new_c] / og_c)
    return converted_amount
            
current = input("Enter a currency you would like to convert yout money to: ").upper()
print(check_currency_exists(current))

amount = 100
new_currency = input("Please re-enter this currency: ").upper()
result = currency_converter(amount,new_currency)
print(f"{amount} in GBP is equal to {result:.2f} {new_currency}. ")
    
    

    
    






    


    

    

    




 




   
   
