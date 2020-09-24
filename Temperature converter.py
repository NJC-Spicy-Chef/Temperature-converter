# Page 46
# 1) Celsius to Fahrenheit
        # Fahrenheit = (9/5) * Celcius + 32
# 2) Fahrenheit to Celsius
        # Celcius = (Fahrenheit - 32) / (9/5)

Celsius_list = (0, 10, 15, 20, 30, 40)
Fahrenheit_list = (32, 50, 59, 68, 86, 104)

for Celsius in Celsius_list:
    Fahrenheit = (9/5) * Celsius + 32
    print(Celsius, " degrees Celsius equals", Fahrenheit, "degrees Fahrenheit.")

print("\n")

for Fahrenheit in Fahrenheit_list:
    Celsius = (Fahrenheit - 32) / (9/5)
    print(Fahrenheit, " degrees Fahrenheit equals", Celsius, "degrees Celsius.")

# Celsius = input("Input temperature in Celsius? ")
# print("The temperature in degrees Fahrenheit is ", (9/5) * int(Celsius) + 32)

# Fahrenheit = input("Input temperature in Fahrenheit? ")
# print("The temperature in degrees Celsius is ", (int(Fahrenheit) - 32) / (9/5))

print("\n")

temperature = input("Input temperature in degrees C or degrees F (e.g., 20C or 70F): ")
try:
    degree = float(temperature[:-1]) # take the temp. but minus the F or C so -1 come back one from the back
    unit = temperature[-1]

    if unit == 'F':
        Celsius = (degree - 32) / (9/5)
        print(temperature, " equals ", Celsius, "C.")
    elif unit == 'C':
        Fahrenheit = (9 / 5) * degree + 32
        print(temperature, " equals ", Fahrenheit, "F.")
    else:
        print("Please enter a valid temperature.")
except ValueError:
    print("Please enter a valid temperature.")