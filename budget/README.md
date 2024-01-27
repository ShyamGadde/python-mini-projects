# Budget

This is a simple Python package for managing budgets across different categories. It allows you to create categories, make deposits and withdrawals, transfer amounts between categories, and visualize your spending with a chart.

## Features

- Create new budget categories
- Make deposits into and withdrawals from each category
- Transfer amounts between categories
- Visualize spending with a chart

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/ShyamGadde/python-mini-projects.git
```

Navigate to the project directory:

```bash
cd python-mini-projects/budget
```

## Usage/Example

```python
>>> import budget
>>>
>>> # Create a new category for food and make an initial deposit
>>> food = budget.Category("Food")
>>> food.deposit(1000, "initial deposit")
>>> # Make a withdrawal for groceries
>>> food.withdraw(10.15, "groceries")
True
>>> food.withdraw(15.89, "restaurant and more food for dessert")
True
>>> # Print the food category
>>> print(food)
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Total: 973.96
>>>
>>> clothing = budget.Category("Clothing")
>>> food.transfer(50, clothing)
True
>>> clothing.withdraw(25.55)
True
>>> clothing.withdraw(100)
False
>>> print(clothing)
***********Clothing***********
Transfer from Food       50.00
                        -25.55
Total: 24.45
>>>
>>> auto = budget.Category("Auto")
>>> auto.deposit(1000, "initial deposit")
>>> auto.withdraw(15)
True
>>> print(auto)
*************Auto*************
initial deposit        1000.00
                        -15.00
Total: 985
>>>
>>> # Visualize spendings
>>> print(create_spend_chart([food, clothing, auto]))
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
```
