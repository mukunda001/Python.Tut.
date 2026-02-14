cost = 49.99

# You can perform if...else statements inside the placeholders:
# You can also perform aritimetic operations and function calls inside the placeholders:

txt = f"The cost of this item is {cost} dollars, which is kind of {'expensive' if cost > 50 else 'affordable'}."
print(txt)