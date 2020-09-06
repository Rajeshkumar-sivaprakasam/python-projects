

print("Welcome to Temprature conversion app")
print()

fahrenheit = float(input("What is the given temperature in degrees Fahrenheit:  "))

celsius = (5/9) * (fahrenheit - 32) 
 
kelvin = celsius + 273.15

#allocating decimal after round
fahrenheit = round(fahrenheit,2) 
celsius = round(celsius,4)
kelvin = round(kelvin,4)

print(f"Degree Fahrenheit:\t {fahrenheit}")
print(f"Degree celsius:\t {celsius}")
print(f"Degree kelvin:\t {kelvin}")