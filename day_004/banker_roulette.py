import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
people_max_index = len(names) - 1
print(f"{names[random.randint(0, people_max_index)]} is going to buy the meal today!")
