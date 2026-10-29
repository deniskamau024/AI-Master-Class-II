Markdown

# Kiambu Dairy Co-op payment calculator
A simple python script that takes in a farmers name and litres and returns the money owed as per current price

# Features
- Reads the updated price of milk directly from text
- Uses fall back price if the current price is missing
- cleans and formats total payout to two decimal places

## project structure
- 'python_dairy_calculator.py' (The main script)
- 'price.txt' ( File containing the current price)

## Setup & Running
- Make sure python 3 is installed in your computer
- put 'python_dairy_calculator.py' and 'price.txt' in the same folder
- run

# Example Output

'''text
Kiambu Dairy Co-op payment calculator
---------------------------------------
current buying price: KES 70.00 per litre

Farmer: Denis
litres : 1.0
Price: KES 70.00/litre
Total: KES 70.00
'''