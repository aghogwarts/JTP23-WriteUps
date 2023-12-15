
# new caesar

## problem
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil
 we are also given the code for the encryption 
 ## hints
 How does the cipher work if the alphabet isn't 26 letters?
 Even though the letters are split up, the same paradigms still apply.

 ## solution 
after going through the code for the encryption i could figure out hoe the encryption works 
* first the code takes the string and converts it into binary which require 8bits per character then splits into groups of 4 bits and concerts them into characters
![Screenshot from 2023-11-15 10-41-36](https://github.com/adwait3/pico/assets/148553626/4c990af8-cb35-4ec4-805e-2533a8352eb0)
* then the shift function takes a character c and our key character k and shifts c by k places and we know that our key character is one of the alphabets which gives us 16 possible keys , since 16 is not a large number we can easily bruteforce this.

to get the decryption we can try and reverse the encryption code .
first we make a code for reversing the b_16 encryption.
![Screenshot from 2023-11-15 11-22-09](https://github.com/adwait3/pico/assets/148553626/95821df1-33aa-4b56-b900-4fc8153f49d6)
* in this we iterate over the encoded string in steps of 2 as each char is 4 bits and 2 characters would make a byte.
* then we convert our chunk of two characters(1 byte) to thier binary representation.
 in this expression {0:04b}{1:04b}".format(ALPHABET.index(chunk[0]), ALPHABET.index(chunk[1])):
* o and 1 are the place holders and 04b specifies the format (4 digit binary format)
* the next part gives the index of the first and second character in our chunk.
* after this we convert the binary string to characters and add it to plain.
now we make a reverse for the shifting
![Screenshot from 2023-11-15 11-32-32](https://github.com/adwait3/pico/assets/148553626/fe3cfa1b-70a5-4c3a-b565-699f5910653a)

this takes a cgaracter c and the key character k and gives the decrypted character by shifting c bacnk by k places inthe alphabets.

next we print all possible decryptions (bruteforce) for every character in the alphabet since we dont know which one is actually the key
![Screenshot from 2023-11-15 11-36-32](https://github.com/adwait3/pico/assets/148553626/47517619-10e9-4232-8e4a-4f6d433f85bc)
this loop iterates in all the alphabets and calls various functions to give the decrypted output for each of them
## final code with output
![Screenshot from 2023-11-15 11-39-00](https://github.com/adwait3/pico/assets/148553626/4250d036-fb67-4aee-9f88-2ac837492e1e)
this gives us the answers and after trial and erroe we get the final key f and decrypted answer et_tu?_431db62c5618cd75f1d0b83832b67b46

## flag
picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}


# miniRSA
## problem
Let's decrypt this: ciphertext? Something seems a bit small.
hints
* RSA tutorial
* How could having too small an e affect the security of this 2048 bit key?
* Make sure you don't lose precision, the numbers are pretty big (besides the e value)

## solution

## flag
picoCTF{n33d_a_lArg3r_e_d0cd6eae}

# basic-mod1
## problem
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
hints
* Do you know what mod 37 means?
* mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## solution
first after opening the message it seemed pretty straightforward 
![Screenshot from 2023-11-15 22-35-25](https://github.com/adwait3/pico/assets/148553626/7270ec23-161b-45f4-9c26-1ed5ea4b2b0b)
looking at the hints i calculated the mod of each of the numbers giving me
![Screenshot from 2023-11-15 22-39-00](https://github.com/adwait3/pico/assets/148553626/dd750ff4-8c16-4d4a-ad6c-18b203def99b)
![Screenshot from 2023-11-15 22-39-09](https://github.com/adwait3/pico/assets/148553626/a70c3b5d-ee5f-4d86-be71-8af49906a8c1)

then i mapped these according to the given parameters which gaave me 
R0UND_N_R0UND_ADD17EC2

## flag
picoCTF{R0UND_N_R0UND_ADD17EC2}


# basic-mod2
## problem
A new modular challenge!
Download the message here.
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
hints
* Do you know what the modular inverse is?
* The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
* It's recommended to use a tool to find the modular inverses

## solution
first things first i read the file 
![Screenshot from 2023-11-16 11-50-45](https://github.com/adwait3/pico/assets/148553626/ef4a1695-0cc6-4408-996a-d88dd6750a13)
then like in mod 1 i calculated mod41 for all the digits
![Screenshot from 2023-11-16 12-02-02](https://github.com/adwait3/pico/assets/148553626/fb7f066f-7370-4167-a09d-2e66a5623eb9)
![Screenshot from 2023-11-16 12-02-11](https://github.com/adwait3/pico/assets/148553626/4612cbfd-3b42-4ab4-92c6-e3ca51d204fa)

22 3 28 26 16 9 26 24 23 10 36 4 16 31 10 31 1 31 1 1 14 1 1  

after this using the hints i calculated inverse modulo for each number manualy which gave me 
28 14 22 30 18 32 30 12 25 37 8 31 18 4 37 4 1 4 1 1 3 1 1
now i mapped these according to the question which gave me 

1NV3r53LY_H4RD_DADAACAA

## flag
picoCTF{1NV3r53LY_H4RD_DADAACAA}


