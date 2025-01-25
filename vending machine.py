import time
import random

# Initial cash balance and stock levels for new items
cash_balance = 0
product_stock = {
    'A1': 10, 'A2': 8, 'A3': 5, 'A4': 12, 'A5': 7,
    'B1': 6, 'B2': 10, 'B3': 4, 'B4': 8, 'B5': 15,
    'C1': 9, 'C2': 10, 'C3': 6, 'C4': 7, 'C5': 10,
    'D1': 11, 'D2': 8, 'D3': 5, 'D4': 6, 'D5': 9,
    'E1': 14, 'E2': 9, 'E3': 7, 'E4': 5, 'E5': 12,
}

# New product catalog with different items and prices
product_catalog = { 
    'A1': {'Category': 'Sweets', 'Name': 'Smickers', 'Price': 3.0},
    'A2': {'Category': 'Sweets', 'Name': 'Mars', 'Price': 2.0},
    'A3': {'Category': 'Sweets', 'Name': 'Reeses', 'Price': 1.75},
    'A4': {'Category': 'Sweets', 'Name': 'Galaxy', 'Price': 3.50},
    'A5': {'Category': 'Sweets', 'Name': 'Milky Way', 'Price': 1.25},

    'B1': {'Category': 'Hot Drinks', 'Name': 'Cappucino', 'Price': 1.50},
    'B2': {'Category': 'Hot Drinks', 'Name': 'Americano', 'Price': 2.50},
    'B3': {'Category': 'Hot Drinks', 'Name': 'Milk Coffee', 'Price': 3.50},
    'B4': {'Category': 'Hot Drinks', 'Name': 'Hot Chocolate', 'Price': 2.75},
    'B5': {'Category': 'Hot Drinks', 'Name': 'Chai', 'Price': 1.50},

    'C1': {'Category': 'Soda', 'Name': 'Cola', 'Price': 2.50},
    'C2': {'Category': 'Soda', 'Name': '7up', 'Price': 2.25},
    'C3': {'Category': 'Soda', 'Name': 'Mirinda', 'Price': 4.75},
    'C4': {'Category': 'Soda', 'Name': 'Pepsi', 'Price': 4.75},
    'C5': {'Category': 'Soda', 'Name': 'Mountain Dew', 'Price': 3.50},

    'D1': {'Category': 'Snacks', 'Name': 'Oman Chips', 'Price': 2.50},
    'D2': {'Category': 'Snacks', 'Name': 'Sohar Chips', 'Price': 2.0},
    'D3': {'Category': 'Snacks', 'Name': 'Chocolate Brownie', 'Price': 1.0},
    'D4': {'Category': 'Snacks', 'Name': 'Salad Chips', 'Price': 3.25},
    'D5': {'Category': 'Snacks', 'Name': 'Popcorn', 'Price': 1.5},

    'E1': {'Category': 'healthy snacks', 'name': 'banana cake', 'Price': 3.0},
    'E2': {'Category': 'Healthy Snacks', 'Name': 'Rice Cakes', 'Price': 5.5},
    'E3': {'Category': 'Healthy Snacks', 'Name': 'Almonds', 'Price': 3.25},
    'E4': {'Category': 'Healthy Snacks', 'Name': 'Mixed Fruit', 'Price': 4.0},
    'E5': {'Category': 'Healthy Snacks', 'Name': 'Veggie Chips', 'Price': 5.75},
}

# Display available products grouped by category
def show_product_list():
    categories = ['Sweets', 'hot drink', 'Soda', 'Snacks', 'Healthy Snacks']
    for category in categories:
        print(f"\n{'-' * 80}")
        print(f"\n{category}")
        for code, info in sorted(product_catalog.items()):
            if info['Category'] == category:
                print(f"Code: {code} | Name: {info['Name']} | Price: ${info['Price']} | Stock: {product_stock[code]}")

# Validate if the entered product code is valid
def is_valid_selection(selection):
    return selection in product_catalog

# Handle purchase and stock updates
def handle_purchase(selection):
    global cash_balance
    global product_stock

    if product_stock[selection] > 0 and cash_balance >= product_catalog[selection]['Price']:
        recommended_item = suggest_item(selection)
        print(f"\nDispensing: {product_catalog[selection]['Name']}")
        print(f"Enjoy your {product_catalog[selection]['Name']} along with {product_catalog[recommended_item]['Name']}!")
        cash_balance -= product_catalog[selection]['Price']
        product_stock[selection] -= 1
        print(f"{product_stock[selection]} {product_catalog[selection]['Name']} left in stock.")
    elif product_stock[selection] <= 0:
        print("\nSorry, this item is out of stock.")
    elif cash_balance < product_catalog[selection]['Price']:
        print("\nInsufficient funds.")
        add_more = input("Would you like to add more money? (yes/no): ")
        if add_more.lower() == 'yes':
            add_money = float(input("Insert more coins or banknotes: $"))
            cash_balance += add_money
    else:
        print("\nInvalid item code.")

# Suggest a random item from the same category for pairing
def suggest_item(selection):
    category = product_catalog[selection]['Category']
    alternative_items = [code for code, info in product_catalog.items() if info['Category'] == category and code != selection]
    return random.choice(alternative_items)

# Main vending machine interaction loop
def vending_machine():
    global cash_balance

    print("\nWelcome to the Vending Machine!")

    show_product_list()

    print(f"\n{'-' * 80}")
    time.sleep(1)
    inserted_money = float(input("Insert coins or banknotes: $"))
    cash_balance += inserted_money

    continue_shopping = True
    while continue_shopping:
        print(f"\nCurrent balance: ${cash_balance}")
        selected_item = input("Enter the product code to purchase: ")

        if is_valid_selection(selected_item):
            handle_purchase(selected_item)
        else:
            print("Invalid selection.")

        continue_response = input("\nWould you like to make another purchase? (yes/no): ")
        if continue_response.lower() == 'no':
            continue_shopping = False
            print(f"\nYour remaining balance: ${cash_balance}")
            print("Thank you for using the Vending Machine!")

# Start the vending machine process
vending_machine()
