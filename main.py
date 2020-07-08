#Today we will be converting temperatures
def func():

    name = input("Please enter your name: ")
    print("Hello " + name.capitalize())
    W = input("what temperature are you converting from: ")
    if W == "celsius":
        b = input("what temperature do you want to convert to: ")
        if b == "fahrenheit":
            C = int(input("Enter the temperature in celsius: "))

            F = 9 / 5 * (C + 32)
            print(round(str(F)) + " (rounded)")
            print(str(F) + " degrees fahrenheit")
        elif b == "kelvin":
            m = int(input("enter the temperature in celsius: "))

            x = m + 273.15
            print(str(round(x, 2)) + " (rounded)")
            print(str(x) + " degrees kelvin")

    elif W == "fahrenheit":
        l = input("what temperature do you want to convert to: ")
        if l == "celsius":
            f = int(input("Please enter the temperature in fahrenheit: "))

            c = 5 / 9 * (f - 32)
            print(str(c) + " degrees celsius")
        elif l == "kelvin":
            z = int(input("enter the temperatture in fahrenheit"))

            r = (z + 459.67) * 5 / 9
            print(str(round(r, 2)) + " (rounded)")
            print(str(r) + " degrees celsius")

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
