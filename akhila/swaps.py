# y.akhila
# swaps program
a = 10
b = 20
temp = a
a = b
b = temp
print("Using temp:", a, b)
a, b = b, a
print("Using tuple:", a, b)