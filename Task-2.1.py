string=str(input("Enter a string: "))
count=0
for char in string:
    if char in ['A','a','E','e','I','i','O','o','U','u']:
       count+=1
print("Number of vowels: ",count)




