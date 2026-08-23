# y akhila
# largest num program
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print("Largest number is:", largest)
# Enter first number: 39
# Enter second number: 26
# Enter third number: 18
# Largest number is: 39.0