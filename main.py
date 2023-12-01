MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
profit = 0


def check_resources(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}.")
           return False
    else:
      return True

def check_coins(order_cost):
    global profit
    coins = int(input("Please insert coins in rupees: "))
    if coins < order_cost:
        print("Sorry not enough money.You are refunded.")
        return False
    elif coins > order_cost:
        print("Successful!")
        bal = coins - order_cost
        print(f"Balance of {round(bal, 2)} is given.")
        profit += order_cost
        return True

    else:
        print("Successful!")
        profit += order_cost
        return True

def deduct_resources(order_ingredients):
     for item in order_ingredients:
         resources[item] = resources[item] - order_ingredients[item]





is_on = True


while is_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt.lower() == "off":
        is_on = False

    elif prompt.lower() == "report":
        for key in resources:
            print(key, ":", resources[key])

        print("Profit: ",profit)

    else:
        if check_resources(MENU[prompt]["ingredients"]):
               if check_coins(MENU[prompt]["cost"]):
                   deduct_resources(MENU[prompt]["ingredients"])
                   print(f"Here is your {prompt}. Enjoy it!!")






