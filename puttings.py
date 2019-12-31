pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (Free)"
    else:
        return f"{topping.title()} ($1 Extra)"

# format_topping(pizza_toppings)
# print(format_topping("cheese") == "Cheese (Free)")
# print("a" == "a")
# print(format_topping("pepperoni") == "Pepperoni ($1 Extra)")

def print_menu(toppings):
    print("Welcome to Jolie's Pizzelia.")
    print("Our available toppings are: ")
    for topping in toppings:
        print(format_topping(topping))

print_menu()
