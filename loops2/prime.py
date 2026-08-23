# y Akhila
# prime number program
num=int(input("enter the number"))
if num<2:
    print("not a prime ")
else:
 prime= True
 for i in range(2,num):
   if num%i==0:
    prime=False
    break
if prime:
    print("prime number")
else:
    print("not a prime")
    # enter the number 4
#not a prime

