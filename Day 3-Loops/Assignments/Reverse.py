def reverse(s):
	str = ""
	for i in s:
		
		str = i + str
		print(str)
	return str

s = "Hello World"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
