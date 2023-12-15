import string
characters = string.ascii_uppercase
characters += "0123456789_"

def modu(num):
	r = num % 37
	return r

deci_list = []

def main():
	mess = open("message.txt", "r")
	list = mess.read().split()
	print(list)


	for i in range(len(list)):
		deci_list.append(modu(int(list[i])))

	print(deci_list)

main()

flag = ""

for i in deci_list:
	flag += characters[i]

print('picoCTF{%s}' % flag)
