string=input("Enter a word: ")
dict = {}
for i in string:
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1

print(str(dict))
