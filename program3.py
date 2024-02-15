try:
    temperature = float(input("Please enter a temperature in celsius:\n"))
except ValueError:
    print("Please enter a valid number")
    exit()

print("the temperature in fehrenheit is:")
print((9/5)*temperature+32)