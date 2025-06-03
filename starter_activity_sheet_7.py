# starter program week 7

# pizza

def pizza():
    print("What toppings would you like on your pizza? All pizzas have cheese. ")
    print("Enter X when you have finished adding toppings. ")
    toppings = ""
    next_topping = ""
    while next_topping != "X":
        print("So far you have a pizza with cheese " + toppings)
        next_topping =  input("Enter topping ... ")     
        toppings = toppings + " and " + next_topping
        print("Add your next topping (X when finished)")
    print("Your pizza will have cheese " + toppings + ". Enjoy! ")

pizza()