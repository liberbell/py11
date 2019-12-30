
pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (free)"
    else:
        return f"{topping.title() ($1 Extra)}"

# format_topping(pizza_toppings)
print(format_topping("cheese") "Cheese (free)")
