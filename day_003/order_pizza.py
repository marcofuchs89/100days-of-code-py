# Code prepared by Instructor
print("Welcome to Python Pizza Deliveries!")
size: str = input("What size pizza do you want? S, M or L: ")
add_pepperoni: str = input("Do you want pepperoni? Y or N: ")
extra_cheese: str = input("Do you want extra cheese? Y or N: ")

# Own code below this line
# Error Checking
# if size.upper() not in ("S", "M", "L"):
#     print(f"Sorry, the size you entered ist not available. You've chosen: {size.upper}")
#     size: str = input("Please choose a correct size: S - M - L: ")


# Initialize the total_bill
total_bill: int = 0

while True:
    if size.upper() == "L":
        total_bill += 25
        if add_pepperoni.upper() == "Y":
            total_bill += 3
    elif size.upper() == "M":
        total_bill += 20
        if add_pepperoni.upper() == "Y":
            total_bill += 3
    elif size.upper() == "S":
        total_bill += 15
        if add_pepperoni.upper() == "Y":
            total_bill += 2
    else:
        print(f"Sorry, the size you entered ist not available.")
        break

    if extra_cheese.upper() == "Y":
        total_bill +=1

    print(f'Your final bill is: ${total_bill}')
    break
