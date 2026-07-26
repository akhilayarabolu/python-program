# y.akhila
# argv program
import sys
if len(sys.argv) != 3:
    print("Usage: python sum.py num1 num2")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum =", a + b)