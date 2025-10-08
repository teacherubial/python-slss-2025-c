# Functions
# Author: Ubial
# 8 October

# function to print "hello" to the console
def say_hello():
    print("hello")

# function to print a personalized hello
def say_hello_personal(name: str):
    print(f"hello {name}!")

def normalized_input():
	"""Clean up the user's input"""
	output = input()
	output = output.strip(",.?! ").lower()
	return output

# Ask the user for the weather
print("What's the weather like?")
weather_reply = normalized_input()

if weather_reply == "rainy":
	print("You should bring an umbrella!")
