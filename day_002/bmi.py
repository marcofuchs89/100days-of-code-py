# Exercise 2-2 - BMI
print("BMI Calculator")
print("==============")
body_height = float(input("What's your height in meters? (decimal -> 1.75m)\n"))
body_weight = float(input("What's your weight in kilograms?\n"))

body_mass_index = int(body_weight / body_height**2)

print(f"Your Body Mass Index is: {body_mass_index}\n")