# main.py
from inventory import add_book, remove_book, display_inventory, inventory
from borrow_return import borrow_book, return_book
from datetime import date, timedelta

# 1️⃣ Add books to inventory
add_book("The Great Gatsby", "F. Scott Fitzgerald", 3)
add_book("1984", "George Orwell", 2)
add_book("Python Basics", "John Doe", 4)

display_inventory()

# 2️⃣ Borrow books
borrow_book("1984")
borrow_book("Python Basics")

# 3️⃣ Return a book (late by 4 days)
return_book("1984", days_late=4)

# 4️⃣ Remove a book
remove_book("The Great Gatsby")

display_inventory()

# 5️⃣ Using Lambda — filter overdue books (demo data)
borrowed_books = [
    {"title": "1984", "due_date": date(2025, 9, 30)},
    {"title": "Python Basics", "due_date": date(2025, 10, 10)},
    {"title": "AI for Beginners", "due_date": date(2025, 9, 28)},
]

today = date(2025, 10, 5)
overdue_books = list(filter(lambda b: b["due_date"] < today, borrowed_books))

print("\n⏰ Overdue Books:")
for book in overdue_books:
    print(f"• {book['title']} (Due: {book['due_date']})")

# 6️⃣ List comprehension — report of borrowed books
borrowed_report = [f"{title} ({info['borrowed']} borrowed)" for title, info in inventory.items() if info['borrowed'] > 0]

print("\n📊 Borrowed Books Report:")
for item in borrowed_report:
    print("•", item)
