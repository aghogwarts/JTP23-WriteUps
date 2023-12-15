### Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme.

Download the message [here](./message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

### Approach

Open the file: `cat message.txt`

>`165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138`

We need split those numbers and `mod` each of them with `37` and store in a list. After that decrypt the list according to the rules.To do that, write a [python script](./modulus.py) in terminal using nano:`nano modulus.py`

```python
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

```

Run the python script: `python3 modulus.py`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/9bd32031-7a28-4871-b9e5-d954956ba59c)

**Flag:** `picoCTF{R0UND_N_R0UND_B6B25531}`
