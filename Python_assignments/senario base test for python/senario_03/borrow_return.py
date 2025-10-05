# borrow_return.py
import math
from inventory import inventory

def borrow_book(title):
    """Borrow a book if available."""
    if title in inventory and inventory[title]["copies"] > 0:
        inventory[title]["copies"] -= 1
        inventory[title]["borrowed"] += 1
        print(f"📖 You borrowed '{title}'. Enjoy reading!")
    else:
        print(f"⚠️ '{title}' is not available for borrowing.")

def return_book(title, days_late=0):
    """Return a borrowed book and calculate fine if late."""
    if title in inventory and inventory[title]["borrowed"] > 0:
        inventory[title]["copies"] += 1
        inventory[title]["borrowed"] -= 1
        fine = calculate_fine(days_late)
        print(f"📚 Returned '{title}'. Fine: Rs {fine:.2f}")
    else:
        print(f"⚠️ '{title}' was not borrowed.")

def calculate_fine(days_late):
    """Fine = base_rate * sqrt(days_late)"""
    base_rate = 10  # Rs 10 per day (nonlinear increase)
    if days_late <= 0:
        return 0
    return math.sqrt(days_late) * base_rate
