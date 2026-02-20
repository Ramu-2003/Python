# --- 1. Variable Assignment and Data Types ---

# String: Text data representing the user's name
user_name = "RAMU 2710"

# String: Text data representing the user's role
user_role = "Creator"

# Integer: A whole number representing a count or ID
item_count = 5

# Float: A decimal number (Use 'USD' for currency as per guidelines)
# price_per_unit = USD 19.99
price_per_unit = 19.99

# Boolean: Represents True or False states
is_active = True


# --- 2. Multiple Assignment ---

# You can assign multiple values to multiple variables in a single line
x, y, z = 10, 20, 30  # x is 10, y is 20, z is 30


# --- 3. Dynamic Typing ---

# Python allows a variable to change its data type during execution
status = "Initializing"  # Initially a String
status = 1              # Now an Integer


# --- 4. Collections (Lists) ---

# A list stores multiple items in a single variable
skills = ["Content Creation", "Python", "Automation"]


# --- 5. Mathematical Operations and Logic ---

# Performing calculations using variables
# Logic: If $a = 10$ and $b = 5$, then $total = a + b$
a = 10
b = 5
total_sum = a + b  # total_sum is 15

# Calculating a total price
# Logic: $total\_cost = item\_count \times price\_per\_unit$
total_cost = item_count * price_per_unit


# --- 6. Output using f-strings ---

# f-strings allow you to embed variables directly into strings for display
print(f"Profile: {user_name}")
print(f"Role: {user_role}")
print(f"Status Active: {is_active}")
print(f"Total Items: {item_count}")
print(f"Total Cost: USD {total_cost}")  # Displaying currency as USD
print(f"Primary Skill: {skills[0]}")
