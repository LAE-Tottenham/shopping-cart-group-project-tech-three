import math
import pyfiglet
import time

food_items = {
    'Coke': 2.00,
    'Butter': 3.65,
    'Chocoloate':1.50,
    'Coffee': 3.00,
    'Yoghurt': 1.20,
    'Lays BBQ Ribs Crisp': 2.59,
    'Pasta': 3.00,
    'Indomie': 0.99,
    'Eggs': 2.50,
    'Sprite': 2.00
}



def welcome_msg():
    welcome_msg = pyfiglet.figlet_format("Welcome to your Shopping Cart Experience!", font='small', width=60)                                     
    print (welcome_msg)

def add_to_cart():
    cart = []
    cart_price = 0
    while True:
        add_item = input("Enter name of item you would like to add to the basket (or type 'Checkout' to checkout): ").capitalize()
        
        if add_item == 'Checkout':
            if len(cart) == 0:
                print("Your cart can be empty. Please add an item before checking out: ")
            else:
                print("Proceeding to checkout...")
                break
        elif add_item in food_items:
            cart.append(add_item)
            cart_price += food_items[add_item]
            print("Added" + " "+ add_item + " " + "to your cart. Current total price is: £" + str(cart_price))

            if len(cart) > 10:
                print("You have more than 10 items in your cart. We are removing the last item.")
                removed_item = cart.pop()
                cart_price -= food_items[removed_item]
            elif len(cart) == 10:
                print("You have 10 items in your cart. Proceeding to checkout...")
                break
        else:
            print("Please make sure you input an item only from what we sell.")
    
    return cart, cart_price


def paying(total_cost):
    total = str(total_cost)

    payment_type = input("Please enter if you are using card or cash. Type 'Card' for card or 'Cash' for cash: ").capitalize()
    while True:
        if payment_type == "Cash":
            cash = input("Pay now. Type amount owed: ")
            if float(cash) != total_cost:
                print("Please enter amount due: which is: £" + " " + total +": ")
            else:
                time.sleep(3)
                print("Thank you for payment. You should recieve your order tomorrow! ")
                break
        elif payment_type =="Card":
            card = input("Please enter what type of card you are using. (Visa/Mastercard) : ").capitalize()
            if card.capitalize() not in ["Visa", "Mastercard"]:
                print("Please enter the correct type of card: ")
            else:
                card_money = input("Pay now. Type amount owed: ")
                if float(card_money) != total_cost:
                    print("Please enter amount due: which is £:" + total +": ")
                else:
                    time.sleep(3)
                    print("Thank you for payment. You should recieve your order tomorrow! ")
                    break
        else:
            print("Enter a valid payment option, either Card or Cash: ")

def delivery_cost(postcode):
    distance = {'N17 0BX': 0,
                'N17 0BY': 0.5,
                'N17 0BZ': 0.6}
    return distance.get(postcode, 10)             
        
                  
        
def main():
    welcome_msg()
    print("The items we sell are:")
    for key, value in food_items.items():
        print(f"{key}: £{value:.2f}")
        time.sleep(1)
    print("Select up to 10 items from this list to add to your cart.")
    
    cart, cart_price = add_to_cart()
    
    
    user_postcode = input("Please enter your postcode: ").upper()
    distance_m = delivery_cost(user_postcode)
    delivery_price = distance_m * 0.50
    total_cost = cart_price + delivery_price

    print(f"Delivery distance: {distance_m} metres. Delivery cost: £{delivery_price:.2f}")
    print(f"Total cost including delivery £{total_cost:.2f}")

    paying(total_cost)
    

    
    

main()
   
    




        
