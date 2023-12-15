## miniRSA

miniRSA

As the value of public key, public key E and the cipher message is given, using any decryption site we can get the value of the flag.

![Uploading Screenshot 2023-11-14 at 2.03.22 AM.png…]()

## mod1

MOD1

First take the mod of each number with 37 to get values between 1 and 36. Replace each digit with its corresponding value to get the flag value.

![Uploading Screenshot 2023-11-10 at 6.34.57 PM.png…]()

## new caeser

Upon understanding the code essentially what is happening is that the key is any 1 character from a-p. When we pass a flag what happens is first it is converted to its binary value. Then this value is split from the middle whose binary is converted into a decimal number. This decimal number is then converted into its corresponding character. The shift function is carrying out some form of a caesar shift.

(I consulted the reverse engineered code to solve this question.)

What we essentially do is convert the split parts of the code and combine them to form the complete binary which we then convert to decimal and decimal to characters.

In the reverse engineered code the key can be brute forced as there are only 16 possibilities from a-p. On running the code key and flag will get printed. When the key is e the flag seems to be in a readable format with no weird characters and it is the key.
<img width="1041" alt="Screenshot 2023-11-14 at 11 58 29 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/3ad0c0f4-379c-4238-b5b4-a4541ff8f36b">
<img width="1041" alt="Screenshot 2023-11-14 at 11 58 41 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/a184c145-d98b-4693-9ed2-e4131565e212">
