
pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (free)"
    else:
        return f"{topping.title() ($1.00)}"

format_topping(pizza_toppings)
