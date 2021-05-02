# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line, see the example at:
# https://band-name-generator-end.appbrewery.repl.run/

print(
    """Welcome to the Band Name Generator.
===================================

We will create a totally awesome name for your band to start rockin
with just a few easy steps: so let's get started ;)
"""
)
city_name = input("What's the name of the city you grew up in?\n")
print("")
pet_name = input(
    "How was your last pet called / What name would you call your future pet?\n"
)
print("")
print("===================================")
print(
    f"""Your new awesome band-name:
{city_name} {pet_name}
"""
)
