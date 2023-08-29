number=int(input())
if number<=1:
        print("Number is prime")
for i in range(2,number-1):
    if number%i==0:
        print("Number is not prime")
        break
else:
     print("Number is prime")

