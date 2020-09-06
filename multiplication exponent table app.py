

print("Welcome to the Multiplication/Exponent Table App")
print()

name = input("What is your name:").title().strip()
number = float(input("What number would you like to work with:"))
message = "math is cool"
print()

print(f"Multiplication Table for {number}" )

for i in range(1,10,1):
	print(f"{i} * {number} = ", i*number)

print()
print(f"Exponent Table for {number}" )

for i in range(1,10,1):
	print(f"{i} ** {number} = ", i ** number)

print(message)
print(f"\t ",message.lower())
print(f"\t \t",message.title())
print(f"\t \t \t",message.upper())