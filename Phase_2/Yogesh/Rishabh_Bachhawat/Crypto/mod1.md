Wrote python code

```
import string

m = open("message")

l = m.read()
print(l)
l = l.split(" ")
print(l)
l.remove(l[-1])
for i in range(len(l)):
	l[i] = int(l[i])
	l[i] = l[i] % 37
	
print(l)

letters = string.ascii_uppercase

d_alpha = {i: letters[i] for i in range(26)}
d_num = { i+26: i for i in range(10)}

for i in range(len(l)):
	if l[i] == 36:
		l[i] = "_"
	elif l[i]<=25 :
		l[i] = d_alpha[l[i]]
		l[i] = str(l[i])
	else :
		l[i] = d_num[l[i]]
		l[i] = str(l[i])
print(l)
print(''.join(l))
print(''.join(l), file = open('output.txt', "w"))

```
![image](https://github.com/CoderZonora/picoCTF/assets/140229408/7f606790-26ad-4b92-b974-d673bbf15ef0)

Flag: picoCTF{R0UND_N_R0UND_79C18FB3}
