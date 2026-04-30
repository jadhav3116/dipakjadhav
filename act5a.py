# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:52:46 2026

@author: dipak
"""
# Create dictionary
library = {
    "Python Basics": 250,
    "Data Science Handbook": 500,
    "Machine Learning": 750
}

# Update price of a book
book_name = "Python Basics"
new_price = 300

if book_name in library:
    library[book_name] = new_price
    print(f"Updated price of '{book_name}' is {library[book_name]}")
else:
    print("Book not found")

# Print full dictionary
print(library)
