# miniRSA  
I found this one a bit challenging, I looked out through the hints, even read the wikipedia page on RSA and noted down some formulas from it but I was too much focused on extracting the values of the prime number associated with the modulus.  
So I ended up asking my mentro what to do about it, and luckily he suggested me to go through a writeup regarding this challenge. So I opened up a writeup _"https://ctf.samsongama.com/ctf/crypto/picoctf19-minirsa.html"_ to understand how to proceed further.  
From there, I came to know about using the formula _c = m^e % n_ where c is the ciphertext, m is the plain message, e is the public exponent and n is the modulus.  
For this I tried to find out the cube root of the given ciphertext, and converted it into Base16 as the displayed set of numbers were not giving anything when I tried to convert it into ASCII format. I extracted the hex conversion, converted it into ASCII format and got the flag.  
THe flag is _picoCTF{n33d_a_lArg3r_e_d0cd6eae}_  
![Screenshot 2023-11-09 125932](https://github.com/SuniCoder9567/Crypt0n1t3/assets/89261516/73a0549a-a2ca-4a72-afae-afcf1d9089b6)
