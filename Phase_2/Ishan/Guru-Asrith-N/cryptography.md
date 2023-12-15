### writeup on crytography

#### new_caesar

opened the challenge     
downloaded the python file `wget https://mercury.picoctf.net/static/2fc43dd1a3718df7debf367b0e092831/new_caesar.py`    
used `python3 new_caesar.py`        
opened the file `nano new_caesar.py`     
read the file       
didn't understand fully. so saw a writeup 'https://ctftime.org/writeup/28927'     
followed what was given in writeup      
did all the process in the original python file in reverse by subtracting and then using python file      
```
# import string
import string

# constants
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# decode function
def b16_decode(cipher):
    dec = ""
    # loop through the cipher 2 characters at a time
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        b = ""
        b += "{0:b}".format(ALPHABET.index(cipher[c])).zfill(4)
        b += "{0:b}".format(ALPHABET.index(cipher[c+1])).zfill(4)
        # turn the binary string to a character and add
        dec += chr(int(b,2))
    
    # return
    return dec

# unshift the text
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

# encrypted flag
enc = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

# loop through all possible keys
for key in ALPHABET:
    # initialize string
    s = ""

    # loop through the encrypted text
    for i,c in enumerate(enc):
        # unshift it based on key
        s += unshift(c, key[i % len(key)])

    # decode
    s = b16_decode(s)

    # print key
    print(s)
```
got the flag 
```
flag : picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}
```


####  mod1

opened the challenge   
used `cat message.txt`     
didn't know what to do referred writeup     
created a python script for given conditions using `nano python.py`      
```
def decode(number):
    r = number % 37
    return r

def main():
    f = open("message.txt", "r", encoding="UTF-8")
    lst = f.read().split()
    # print(lst[0])

    dec_lst = []

    for i in range(len(lst)):
        dec_lst.append(decode(int(lst[i])))

    print(dec_lst)

if __name__ == '__main__':
    main()
```
according to given data "a=0  b=1 ..... z=25 0=26 1=27 ..... 9=35  _=36 "     

got numbers after comparing with given key you will get flag      
```
flag : picoCTF{R0UND_N_R0UND_B6B25531}
```

#### miniRSA

opened the challenge      
downloaded the file using `wget https://jupiter.challenges.picoctf.org/static/ee7e2388b45f521b285334abb5a63771/ciphertext`    
opened the file using `cat ciphertext`     
the formula is given in primer for this ( `m^e mod n = c `)     
although it looks difficult , there is a small chance that `m^e <n`  in which case `m^e = c` . e is also very small which shows that the chance of this occuring is very high       
therefore `m = c^(1/e)`      
directly substituting the values will not give the answer as it will give shortened form     
searched in google about how to write a program for this but didn't get it          
finally read a writeup  'https://github.com/VermillionBird/CTF-Writeups/blob/master/2019/picoCTF/Cryptography/miniRSA/README.md' and got the program from there 'https://github.com/VermillionBird/CTF-Writeups/blob/master/Useful-Scripts/Cryptography/invpow.py'     

```
flag : 
```
