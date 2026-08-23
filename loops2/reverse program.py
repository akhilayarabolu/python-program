# akhila
# reverse program
num = int(input("Enter an integer: "))
temp = abs(num)
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num < 0:
    reverse = -reverse
print("Reversed number:", reverse)
#Enter an integer: 2
#Reversed number: 2