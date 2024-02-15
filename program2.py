nums = []

for i in range(10):
    
    try:
        num = float(input(f"Enter number {i+1}:\n"))
    
    except ValueError:
        print("Please enter a valid number")
        exit()

    nums.append(num)

max = nums[0]

for num in range(1,10):
    if num > max:
        max = num

print(f"The Largest number is: {max}")