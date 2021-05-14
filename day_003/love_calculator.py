# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Concatenate both names
both_names = name1 + name2
l1 = ["t", "r", "u", "e"]
l2 = ["l", "o", "v", "e"]

# Initialize counter
count_true = 0
count_love = 0

# Loop over the lists and count the occurences of the list items
for i in l1:
    count_true += both_names.lower().count(i)
for i in l2:
    count_love += both_names.lower().count(i)

# Concatenate the scores to a string value
love_score_str = str(count_true) + str(count_love)
# Convert back to int for easy comparison
love_score = int(love_score_str)

# Logic for deciding the printout
if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score_str}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score_str}, you are alright together.")
else:
    print(f"Your score is {love_score_str}.")