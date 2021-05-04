# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

body_mass_index = round(weight / height**2)

if body_mass_index <= 18.5:
    print(f"Your BMI is {body_mass_index}, you are underweight.")
elif 18.5 < body_mass_index <= 25:
    print(f"Your BMI is {body_mass_index}, you have a normal weight.")
elif 25 < body_mass_index <= 30:
    print(f"Your BMI is {body_mass_index}, you are slightly overweight.")
elif 30 < body_mass_index <= 35:
    print(f"Your BMI is {body_mass_index}, you are obese.")
elif body_mass_index > 35:
    print(f"Your BMI is {body_mass_index}, you are clinically obese.")
else:
    print(f"Your BMI is {body_mass_index}, and not on the scale.")