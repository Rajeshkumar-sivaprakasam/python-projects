

print("Welcome To Letter Counter App")

name = input("Enter your name:\t")
name = name.title()

print(f"Hello {name}")
print()
print("I will count the number of times that a specific letter occurs in a message")
print()

message = input("Please enter a message:")
message = message.lower()
print()

letter = input("Which letter would you like to count the occurrences of:")
letter = letter.lower()

occurrence = message.count(letter)
print()
print(f"{name}, Your Message has {occurrence} {letter}'s in it.")