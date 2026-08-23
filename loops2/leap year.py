# y akhila
# leap year program
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
 print("Leap year")
else:
 print("Not a leap year")
 #Enter a year: 2035
# Not a leap year