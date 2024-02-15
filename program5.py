try:
    x= int(input("Enter a number of repetitions"))
except ValueError:
    print("Please enter a valid number")
    exit()

def dec(var):
    def wrapper():
        for i in range(x):
            var()
    return wrapper

@dec
def hello():
    print ('Hello')

hello()
