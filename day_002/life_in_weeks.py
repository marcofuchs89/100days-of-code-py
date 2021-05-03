# Exercise 2-3 - Life in Weeks
# Example Output:
# You have 12410 days, 1768 weeks, and 408 months left.
# Input: Current age
# CONSTANT: 90 years

LIFE_EXPECTANCE = 90
current_age = int(input("How old are you? (in Years)\n"))

life_span = LIFE_EXPECTANCE - current_age

print(f"You have {life_span * 365} days, {life_span * 52} weeks, and {life_span * 12} months left.")