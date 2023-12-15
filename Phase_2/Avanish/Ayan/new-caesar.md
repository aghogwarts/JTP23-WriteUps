# new caesar
In this challenge we need to understand the given python code and write a code to do opposite of what the code does.

So here,

```
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc
```

This code converts the given text to binary, splits it into 2 parts and the converts it to alphabet.

The code i used to solve this is,

```
# new ceasar solved
import string

ALPHABET = string.ascii_lowercase[:16]

cryptedtext = 'mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj'

shiftval = 0
while shiftval < 16:
    msg = ''
    i = 0
    while i < len(cryptedtext):
        d1 = (ALPHABET.index(cryptedtext[i])+ shiftval)%len(ALPHABET)
        d2 = (ALPHABET.index(cryptedtext[i+1])+ shiftval)%len(ALPHABET)

        b16 = (d1 << 4) + d2 
        msg += f"{chr(b16)}"
        i += 2

    print(f"shiftval: {shiftval} => {msg}") 
    shiftval +=1
```

What this is code does is
It takes the first 2 charcaters, takes their value from the ALPHABET and then shifts their values so they line up, it then checks what charcter it represents in b16, then it moves to the next 2 characters.

We see a lot of values that mean nothing except this,

Flag : picoCTF{et_tu?_5723f4e71a0736d3b1d19dde4279ac03}



