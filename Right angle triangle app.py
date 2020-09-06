
import math
print("Welcome to Right angle triangle app")
print()

a = float(input("What is the first leg of the triangle:"))
b = float(input("What is the second leg of the triangle:"))
print()

hypotenuse = math.sqrt(a **2 + b **2)
area = (a * b) / 2

hypotenuse = round(hypotenuse,3)
area = round(area,1)

print(f"for triangle with legs of {a} and {b} the hypotenuse is {hypotenuse}")
print(f"for triangle with legs of {a} and {b} the area is {area}")
