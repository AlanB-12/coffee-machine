MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(earning):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Earnings: ${earning:.2f}")

def check(choice):
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        if resources.get(item, 0) < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    print("Your coffee will be ready soon.\n")
    return True

def price(q, d, n, p, choice):
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    cost = MENU[choice]["cost"]
    if total < cost:
        print("Sorry, that’s not enough money. Money refunded.")
        return 0
    change = total - cost
    if change > 0:
        print(f"Here is your ${change:.2f} change.")
    print(f"Here is your {choice}. ☕ Enjoy!\n")
    return cost

def deductions(choice):
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

print("\n--- VIRTUAL COFFEE MACHINE ---\n")
earning = 0
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino) or 'report' or 'off': ").lower()

    if choice == "off":
        print("Coffee machine turned off.")
        machine_on = False

    elif choice == "report":
        report(earning)

    elif choice in MENU:
        if check(choice):
            print("Please insert coins:")
            q = float(input("How many quarters?: "))
            d = float(input("How many dimes?: "))
            n = float(input("How many nickels?: "))
            p = float(input("How many pennies?: "))

            cost = price(q, d, n, p, choice)
            if cost > 0:
                deductions(choice)
                earning += cost
    else:
        print("Invalid choice. Please select again.\n")
