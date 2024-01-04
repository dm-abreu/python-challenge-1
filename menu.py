# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
orders = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1


    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Please enter menu number you wish to order:")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]['Item name']

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many items '{item_name}' would you like to order? (Default is 1 if input is invalid): ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        print("Invalid input. Defaulting to 1")
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                orders.append({
                    "Item name": selected_item['Item name'],
                    "Price": selected_item['Price'],
                    "Quantity": quantity
                    })

                    # Tell the customer that their input isn't valid
            else:
                print("Input is invalid.")

                    # Tell the customer they didn't select a menu option
        else:
            print(f"{menu_category} was not a menu option.")

                    # Tell the customer they didn't select a number
    else:
            print("Number not selected.")



# Ask the customer if they would like to order anything else
while True:
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()

    match keep_ordering:
        case 'y':
            # If the customer wants to keep ordering, break out of this loop to continue ordering
            break
        case 'n':
            # If the customer decides to stop ordering, thank them and break out of the main loop
            print("Thank you for your order!")
            place_order = False  # Assuming 'place_order' is your main loop control variable
            break
        case _:
            # For any other input, ask the customer to try again
            print("Invalid Input. Please try again.")



while place_order:
    # Display menu categories
    # Adding cancel option

    # Add a cancel option
    print(f"{i}: Cancel Order")
    menu_items[i] = "Cancel"

    # Get the customer's category choice
    category_choice = input("Please enter the number corresponding to your menu choice, or type 'Cancel' to cancel the order: ")
    if category_choice.lower() == 'cancel':
        break

    # Check if the category choice is valid and proceed with item selection


    # Display items in the chosen category and add a cancel option
    # ... [existing code to display items] ...
    print(f"{i}: Cancel Order")
    menu_items[i] = "Cancel"

    # Get the customer's item choice
    item_choice = input("Please enter the number of the item you wish to order, or type 'Cancel' to cancel the order: ")
    if item_choice.lower() == 'cancel':
        break


# Finalize the order or end the program if cancelled
if orders:
# The order summary will be printed next
    print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
    print(orders)  # 'orders' is the list holding the order details

    print("Your order summary:")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|---------")

    total_cost = 0
    for order_item in orders:
        name = order_item["Item name"]
        price = order_item["Price"]
        quantity = order_item["Quantity"]
        total_cost += price * quantity
        print(f"{name:25} | ${price:<6} | {quantity}")

    print(f"\nTotal Cost: ${total_cost:.2f}")
else:
    print("Order cancelled.")

# 6. Loop through the items in the customer's order
for order_item in orders:
    # 7. Store the dictionary items as variables
    item_name = order_item['Item name']
    price = order_item['Price']
    quantity = order_item['Quantity']

    # 8. Calculate the number of spaces for formatted printing
    name_spaces = max(1, 26 - len(item_name))

    # 9. Create space strings
    price_str = f"${price:.2f}"
    price_spaces = max(1, 8 - len(price_str))

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_spaces}|{price_str}{price_spaces}| {quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

costs = [item['Price'] * item['Quantity'] for item in orders]
total_cost = sum(costs)

print(f"\nThe total cost will be: ${total_cost:.2f}")
