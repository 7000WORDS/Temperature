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
    p = input("what temperature do you want to convert to: ")
    if p == "celsius":
        v = int(input("Enter the temperature in kelvin: "))

        k = v - 273.15
        print(str(round(k, 2)) + " (rounded)")
        print(str(k) + " degrees kelvin")
    elif p == "fahrenheit":
        o = int(input("enter the temperature in kelvin: "))

        n = (o * 9 / 5) - 459.67
        print(round(n, 2) + " (rounded)")
        print(str(n) + " degrees fahrenheit")
    else:
      print("you cannot convert to any other temperature")
