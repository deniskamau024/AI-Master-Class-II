"""Dairy Co-op payment calculator
----------------------------------
Farmers enter their name and litres supplied.
Tool show total owed at current buying price

Usage:
    python dairy_calculator.py

Config:
    Edit current price in the script to update weekly rate.
    Future version: Read from price.txt
"""
import os
def get_current_price():
    """Read current price from 
    price.txt, fall back to default"""
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir,"price.txt")

    try:
        with open(file_path,"r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return  55# Default: Kes 55.0 per litre

def calculate_payment(litres,price_per_litre):
    return litres * price_per_litre

def run():
    print("Kiambu Dairy Co-op payment calculator")
    print("-" * 54)
    print(f"Current buying price: KES {get_current_price():.2f} per litre")
    print()

    name = input ("Farmer name: ").strip()
    if not name:
        print("Name is required.")
        return

    try:
        litres = float(input("Litres supplied today: "))
        if litres <= 0:
            print("Litres must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number of litres.")
        return
    price = get_current_price()
    total = calculate_payment(litres,price)

    print()
    print(f"Farmer : {name}")
    print(f"Litres : {litres}")
    print(f"Price : KES {price:.2f}/litre")
    print(f"Total : KES {total:,.2f}")

run()