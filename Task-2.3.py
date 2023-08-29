n=input("Enter a set of values with spaces between them: ")
values=n.split()
list=[]
for char_num in values:
    x=int(char_num)
    if x%2==0:
        list.append(x)
print("List of even numbers: ",list)


