import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.15,
    'CAD': 1.80,
    'JPY': 194.46, # Japanese Yen
    'CHS': 1.12 # Swiss Franc
}

def check_currency_exists(currency):
    if currency != "USD" or currency!= "EUR" or currency!= "CAD" or currency!= "JPY" or currency!= "CHS" :
        return("Your currency is not a currency we can convert to.")
    else:
        return("Your currency"+ currency+"can be converted to by our software.")

def currency_convert(original_c, new_c, amount):
    # your code here
    return
