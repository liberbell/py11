pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping} (Free)"
    else:
        return f"{topping.title()} ($1 Extra)"

# format_topping(pizza_toppings)
print(format_topping("cheese") == "Cheese (Free)")
print(format_topping("pepperoni") == "Pepperoni ($1 Extra)")

def print_menu(toppings):
    print("Welcome to Jolie's Pizzelia.")
    print("Our available toppings are: ")
