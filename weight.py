wt = float(input("Enter your weight: "))
unit = input("L(bs) or K(g): ")
if unit.upper() == "L":
    print(f"Your weight in kg is {(wt/2.20462):.2f}")
elif unit.upper() == "K":
    print(f"Your weight in pound is {(wt*2.20462):.2f}")
else:
    print("Invalid input ")
