# inventory.py

# Dictionary to store books
inventory = {}

def add_book(title, author, copies):
    """Add a new book or increase copies if it already exists."""
    if title in inventory:
        inventory[title]["copies"] += copies
    else:
        inventory[title] = {"author": author, "copies": copies, "borrowed": 0}
    print(f"✅ '{title}' added/updated successfully!")

def remove_book(title):
    """Remove a book from inventory."""
    if title in inventory:
        del inventory[title]
        print(f"❌ '{title}' removed from inventory.")
    else:
        print(f"⚠️ Book '{title}' not found.")

def display_inventory():
    """Display all books and their availability."""
    print("\n📚 Current Inventory:")
    if not inventory:
        print("No books available.")
    else:
        for title, info in inventory.items():
            print(f"• {title} by {info['author']} | Copies: {info['copies']} | Borrowed: {info['borrowed']}")
