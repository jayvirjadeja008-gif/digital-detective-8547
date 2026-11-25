decimal_number = int(input("Enter a positive decimal number: "))

if decimal_number < 0:
    print("Please enter a positive decimal number.")
else:
    print("Binary:", bin(decimal_number))
    print("Hexadecimal:", hex(decimal_number))
