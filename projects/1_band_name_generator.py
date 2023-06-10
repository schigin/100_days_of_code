#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Welcome to the Band Name Generator.")
print("What's the name of the city you grew up in?")
city_name = input()
print("What's your pet's name?")
pet_name = input()
band_name = city_name + " " + pet_name
print("Your band name could be " + band_name)
