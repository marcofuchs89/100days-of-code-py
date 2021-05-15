# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Remark: len() and sum() are forbidden to use!

average_height: int = 0
item_count: int = 0

# Sum up the heights and counting the iterations
for height in student_heights:
    average_height += height
    item_count += 1

average_height: int = round(average_height / item_count)
print(average_height)
