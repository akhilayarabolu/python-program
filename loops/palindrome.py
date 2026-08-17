# y akhila
# palindrome program
num = int(input("Enter a number: "))
original = num
reverse = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
    #Enter a number: 34
#Not a palindrome