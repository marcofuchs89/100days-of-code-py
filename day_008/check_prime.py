# Write your code below this line 👇
def prime_checker(number):
    counter = 0
    for num in range(2, number+1):
        if (number % num) == 0:
            counter += 1
        else:
            pass

    if counter > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
