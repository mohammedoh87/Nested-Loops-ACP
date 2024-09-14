number = int(input("Enter a number: "))
result = ''
while number != 0:
    remainder = number % 2  # gives the exact remainder
    number = number // 2
    result = str(remainder) + result
print("The binary format is: ", result)    

