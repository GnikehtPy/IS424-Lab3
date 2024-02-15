try:
    number = int(input("please enter a number:\n"))
except ValueError:
    print("Please enter a valid number")
    exit()
for i in range(10):
    print(f"{number} * {i+1} = {number*(i+1)}")