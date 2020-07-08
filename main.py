#Today we will be converting temperatures
name = input("Please enter your name: ")
print("Hello " + name.capitalize())
W = input("what temperature are you converting from: ")
if W == "celsius":
    C = int(input("Enter the temperature in celsius: "))

    F = 9 / 5 * (C + 32)
    print(str(F) + " degrees fahrenheit")
elif W == "fahrenheit":
    f = int(input("Please enter the temperature in fahrenheit: "))

    c = 5 / 9 * (f - 32)
    print(str(c) + " degrees celsius")
elif W == "kelvin":