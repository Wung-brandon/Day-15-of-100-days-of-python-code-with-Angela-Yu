
MENU = {
    "espresso":{ 
        "ingredients":{
        "water":50,
        "coffee":18,
    },
    "cost":1.5,
    },
    "latte":{ 
        "ingredients":{
        "water":200,
        "milk":150,
        "coffee":24,
    },
    "cost":2.5,
    },
    "cappuccino":{ 
        "ingredients":{
        "water":250,
        "milk":100,
        "coffee":24,
    },
    "cost":3.0
    }
    
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_enough(order_ingredients):
    """Returns True when orders can be made, and False when ingredients are insufficient"""
    is_enough = True
    for items in order_ingredients:
        #print(order_ingredients[items])
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry the is not enought {items}")
            is_enough = False
    return is_enough

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please Insert Coins...")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dime?: ")) * 0.1
    total += int(input("How many Nickels?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True when payments is accepted or False when momey is insufficient"""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}") 
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}") 
    
is_on = True
while is_on:
    user_choice = input("What will you like? 'espresso', 'latte' or 'cappuccino': ")
    if user_choice == 'off':
        is_on = False
        print("The machine is turned off")
    elif user_choice == "report":
        print(f'Water:{resources["water"]}ml')
        print(f'Milk:{resources["milk"]}ml')
        print(f'Coffee:{resources["coffee"]}g')
        print(f'Money:${profit}')
    else:
        drink = MENU[user_choice]
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
            