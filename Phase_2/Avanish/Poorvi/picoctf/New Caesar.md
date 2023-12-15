Program breakdown:

		assert all([k in ALPHABET for k in key])
            assert len(key) == 1

This ensures that the key is in the first 16 lowercase alphabets and is only one character long

The b16_encode function : 

The function takes a plain text (plain) as input and returns its Base16-encoded representation (enc). The encoding is performed by converting each character in the plain text to its 8-bit binary representation and then mapping the first 4 bits and the last 4 bits separately to the characters in the ALPHABET
"{0:08b}".format(ord(c)): Converts the ASCII value of the character c to its 8-bit binary representation.

binary[:4] and binary[4:]: Slices the binary string into the first 4 bits and the last 4 bits, respectively.

int(..., 2): Converts the binary string to an integer using base 2.

ALPHABET[...]: Maps the integer value to a character in the ALPHABET.

The final result is obtained by concatenating the characters obtained from both the first and last 4 bits for each character in the input plain text.



Shift function:

ord(c) - LOWERCASE_OFFSET: Converts the character c to its numeric value by subtracting the offset of lowercase letters. This assumes that c is a lowercase letter.

ord(k) - LOWERCASE_OFFSET: Converts the key k to its numeric value using the same offset assumption.

(t1 + t2) % len(ALPHABET): Adds the numeric values of the character and the key, takes the modulus with the length of the ALPHABET to ensure the result stays withinthe valid range.

ALPHABET[...]: Uses the result as an index to obtain the encrypted character from the ALPHABET.

for i, c in enumerate(b16): This iterates through each character (c) in the Base16-encoded string b16, and i represents the index of the current character.

key[i % len(key)]: Uses modular arithmetic to cycle through the characters of the key. i % len(key) ensures that the key is repeated if it's shorter than the length of b16.

shift(c, key[i % len(key)]): Calls the shift function with the current character c from b16 and the corresponding character from the key.

enc += ...: Appends the result of the shift operation to the enc string.

Writing the python script after reversing all the above operations:

![nc1](https://github.com/poorvi1910/Cryptonite/assets/146640913/1f4ff4c1-8d61-4ae3-ac16-7086bb426c04)

OUTPUT:

qQqRY[YSVUT[UYWWWYUYTS

v`@`AHJHwBEDvCurJuuDvHFFFuHDHCvvBssv

et_tu?_0797f143e2da9dd3e7555d7372ee1bbe

TcNcd.N/&(&U #"T!SP(SS"T&$$$S&"&!TT QQT

CR=RS=DCBOBBCBCC@@C

2A,AB,

3

!001ûüóõó"ýðÿ!þ -õ  ÿ!óñññ óÿóþ!!ý..!

/

/ ê
ëâäâìïîíäîâàààâîâíì
ùÙùÚÑÓÑ

Only one output looks like the flag. So The flag is picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}
