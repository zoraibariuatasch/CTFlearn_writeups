---Simply write this code with latest version of python---

file = open("TheMessage.txt", "r").read()
result = ""
for char in file:
	if ord(char) == 32:
		result += "0"
	else:
		result += "1"
print(result)
