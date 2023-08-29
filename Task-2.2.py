string=str(input("Enter a string: "))
reversedstring=string[-1::-1]
print("Reversed String: ",reversedstring)
if string==reversedstring:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

