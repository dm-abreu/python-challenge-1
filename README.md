## python-challenge-1 aka Interactive Food Truck Ordering System

This README file provides an overview of the food truck ordering system using Python.

## Background
Design an interactive ordering system for a food truck menu, leveraging Python programming skills. This system will enable customers to place orders, view itemized receipts, and calculate the total cost, including the interest earned.

## Files
- Module 2 Challenge files.
  
### What is it?

This interactive program simulates a food truck ordering experience, allowing customers to browse menus, select number items, and place orders and receipts.

### Features:

<ul>
    <li>Menu browsing: Customers can choose from various food categories like Snacks, Meals, Drinks, and Desserts.</li>
    <li>Item selection: Customers can specify their desired item by entering the corresponding number.</li>
    <li>Quantity selection: Customers can choose the quantity of each item they want.</li>
    <li>Order list: The system tracks the customer's order in a list, displaying the item name, price, and quantity.</li>
    <li>Receipt generation: After placing the order, the system generates a receipt with the order details and total price.</li>
</ul>

### Technologies used:

<ul>
    <li>Python programming language</li>
    <li>Markdown formatting</li>
</ul>

### Running the program:

<ul>
    <li>Clone or download the project repository.</li>
    <li>Open a terminal in the project directory.</li>
    <li>Install any necessary dependencies (if any).</li>
    <li>Run the main Python script to launch the program.</li>
</ul>

From the menu directory, run the menu file

```bash
python menu.py
```
Follow the screen prompts to place your order.


### Sample Output
---
Welcome to the variety food truck.
From which menu would you like to order? 
1: Snacks
2: Meals
[...]

Item name                 | Price  | Quantity
--------------------------|--------|----------
Cookie                    | $0.99  | 2
Burrito                   | $4.49  | 1
[...]

Total Cost: $6.47



## Setup
- Repository: `python-challenge-1`
- Clone and push changes to GitHub or GitLab.

## Challenge Instructions

### Order System
- Initialize an empty list to store customer orders.
- Prompt customers for menu selections and validate inputs.
- Append orders to the list in a structured dictionary format.
- Implement a match-case statement for order continuation or completion.

### Order Receipt
- Iterate through the order list to print itemized receipts.
- Calculate and display the total price using list comprehension.

## Hints and Considerations
- Utilize variables, lists, dictionaries, and loops.
- Break down tasks into mini-objectives and use pseudocode.
- Commit work regularly and maintain a detailed README.md file.



### Order System
- Initialize and populate the order list.
- Prompt and validate user menu selections.
- Convert menu selections to integers.
- Check if selections are within menu items.
- Extract item names from the menu dictionary.
- Prompt for item quantities with default fallback.
- Append item details to the order list.
- Implement match-case for order processing.

### Order Receipt
- Loop through the order list to process items.
- Save key values as individual variables.
- Calculate formatting spaces for receipt display.
- Create space strings with string multiplication.
- Print itemized orders with calculated spaces.
- Compute and print the total order price.

## Submission
Submit your GitHub repository URL containing the challenge work for evaluation.


### Contributing:

Fork the repository and submit pull requests for any improvements or bug fixes. Please ensure your contributions follow the project coding style and adhere to good coding practices.

### Testing:

The project includes unit tests to ensure the functionality works as intended. You can run the tests to verify the system's behavior.

### Future improvements:

<ul>
    <li>Implement payment processing options.</li>
    <li>Integrate with a database for storing order history.</li>
    <li>Add user authentication features for personalized experiences.</li>
    <li>Develop a graphical user interface for a more interactive experience.</li>
</ul>

### Contact:

Feel free to reach out with any questions, feedback, or suggestions. You can find contact information in the project repository or code comments.


### Acknowledgements
<ul>
<li>[Columbia University AI Bootcamp](https://bootcamp.cvn.columbia.edu/micro/artificial-intelligence/landing/)</li>
<li>[Python Documentation](https://docs.python.org/3/)</li>
</ul>
