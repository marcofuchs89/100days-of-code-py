# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

total_bill = float(input("How much was the bill total?\n$ "))
total_persons = int(input("Between how many people should the bill be splitted?\n"))
tip_value = int(input("How much tip would you like to apply?\n% "))

payment_per_person = format((total_bill / total_persons) * (1 + (tip_value/100)), '.2f')
print(f"Each person should pay {payment_per_person}$")