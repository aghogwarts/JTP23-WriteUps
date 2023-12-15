### Approach Used

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/c366ddbf-d891-4595-a9f8-5842452270a7)

From this we can see that it contains 16 lowercase letters starting from 'a' to 'p'.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/2bf17dd3-e603-4b69-888f-c058bf8fb794)

This function basically converts the letter into binary and then takes first half and converts it to letter. Then it takes the second half of the binary and converts it into another letter.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/f3e314fb-222f-4ccf-9044-052455fed332)

The two letters we got, get shifted by a key where the values of these shifts are stored as t1 and t2. This function performs the caesar shift.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/b4248f74-f336-4a01-96bd-31298d6dad0d)

Here we can see that the length of the key is only 1 character.
So now we can reverse engineer the code to bruteforce and loop over the 16 letters and add 16 possible shifts. After that convert the binary to a number and get the character needed to decode the cipher.

```
def b16_decode(cipher):
    dec = ""
    # loop through the cipher 2 characters at a time
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        binary = "{0:04b}".format(ALPHABET.index(cipher[c])) + "    
                  {0:04b}".format(ALPHABET.index(cipher[c+1]))
       
        # turn the binary string to a character and add
        dec += chr(int(b, 2))
        return dec
```
Every two characters in the cipher text actually represents a single character of the encryption based on the encode function in the main program.

```
enc = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'
for key in ALPHABET:
  flag = ""
  print("Key:", key)
  for c in enc:
    flag += shift(c,key)
  print("Flag: ", b16_decode(flag))
```
### Flag
> picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}

### Resources used
I don't know python so I had to see how to reverse engineer it and understood from [here](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Cryptography/New%20Caesar/New%20Caesar.md)
