### Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) _ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih_

[new_caesar.py](./new_caesar.py)


### Approaach

 First we need to Understand the given code

```python
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] #a,b,c,...,p

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1
```

The assert statements indicate that the key must be a single character and should be a letter from 'a' to 'p'. To obtain the output of "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih", it is essential to modify the values of both the flag and the key.

```python

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

```

When the code "binary = "{0:08b}".format(ord(c))" is tested, it generates the binary representation of the ASCII value of 'c' (values within the flag). The subsequent two lines divide the binary number into two halves (e.g., 01101110 becomes 0110 for the first half and 1110 for the second half). The integer value derived from each half serves as an index for a letter in the ALPHABET list.

```python
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
```

The final process of encrypting the flag is above. Usine enumerate loops through the values of b16, assigning i to the index at a particular point and c the value. The values for the function include the values of b16 and the key (len(key) = 1, i%1 = 0).

```python

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]
```
The function shift returns a value in ALPHABET at the index ascii value of the c minus 97 plus the ascii value of the key minus 97 mod 16.


**Solving**

I decided to write code from different resources and other writeups to make the program run in reverse [new_caesar_reverse_code](./ceaser1.py)

```python
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
cipher_flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
    count = 1
    hexaDeciNum = ['0'] * 100
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
        if count % 4 == 0:
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
    if count == 1:
        i = i-1
    hex_string = ''
    while i >= 0:
        hex_string += hexaDeciNum[i]
        i = i-1
    if hex_string == '':
        hex_string = '00'
    return hex_string

tmp = ""
guess_strings = ""
for i in range(1, 16):
    for e in cipher_flag:
        tmp += "{0:04b}".format((ord(e) - LOWERCASE_OFFSET + i) % len(ALPHABET))
        if len(tmp) % 8 == 0:
            guess_strings += chr(int(binToHexa(tmp), 16))
            tmp = ""
    tmp = ""
    print(guess_strings)
    guess_strings = ""
```
Run the script: `python3 ceaser1.py`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/808c5950-79ab-446b-8f6d-b4bc45e7a632)

**Flag:** `picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}`
