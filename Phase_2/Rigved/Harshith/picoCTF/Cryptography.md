# mod1

So the challenge description is pretty self explanatory. We get a message that has a set of numbers. What we do now is `%37` with each number in the message and we have to map the remainder to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrote the following code to solve the problem and got the flag.![Screenshot (2)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/efda7191-4599-425d-bc5a-18188c679e39)

The flag- `picoCTF{R0UND_N_R0UND_ADD17EC2}`

# miniRSA

Looks like we get a cipher text with bunch of random numbers which is encrypted using **RSA** algorithm and some instructions. The message could be decoded by writing a python solution script, but I choose to use an online decoder and specified Public Key Value as 3. The image below shows the result.![Screenshot (1)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/ff93fa6e-f7f7-469a-9d75-23308a30138f)

The flag- `picoCTF{n33d_a_lArg3r_e_d0cd6eae}`

# Mod 36

The cipher is encrypted using ROT13. Pasted the `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}` cipher text in CyberChef ROT13 decrypter to get the flag.

The flag- `picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}`

# The Numbers

 At a glance, we can know that the numbers in the text `16 9 3 15 3 20 6 {20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}` are related to alphabets. The number 1-26 correspond to alphabets A-Z. With this, we can get the flag for the challenge.

 The flag- `PICOCTF{THENUMBERSMASON}`

 # 13

 Easy one. The cipher text is ROT13 encrypted so used CyberChef ROT13 decrypter to decrypt `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}` to get the flag.
![Screenshot (42)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/f170879b-87f3-4bb6-a342-054d29cd185c)

The flag- `picoCTF{not_too_bad_of_a_problem}`

# Easy1

So it's a basic Vignere cipher text with the `UFJKXQZQUNB` as the cipher text and `SOLVECRYPTO` as the key. Used the Vignere decoder from CyberChef to get the flag.
![Screenshot (44)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/55bc75c1-4696-4827-bb6d-ea8899a74eaa)

The flag- `picoCTF{CRYPTOISFUN}`

# caeser

We get a cipher text ` picoCTF{gvswwmrkxlivyfmgsrhnrisegl}` and it seems that the flag part has been encrypted. Going by the challenge name, It's probably using caeser cipher. But I didn't get anything useful when I ran the cipher text on CyberChef caeser decrypter. So I tried a online multi decoder tool called [CacheSleuth](https://www.cachesleuth.com/multidecoder/) which gave out something useful as shown below.
![Screenshot (45)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/0a568fe2-ac2d-424c-b43a-702228c3ac81)

The flag- `picoCTF{crossingtherubicondjneoach}`

# Vignere

Pasted the Vignere cipher text `rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}` on CyberChef Vignere decoder to get the flag.

The flag- `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}`

# rail-fence

As the instructions say, the cipher `Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6` is encrypted using rail-fence with 4 rails. Pasted the cipher text on CyberChef rail-fence cipher decoder and set Key as 4 to get the flag.
![Screenshot (46)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/66facae0-9612-4467-8fc6-1eaea4dab385)

The flag- `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_83F6D8D7}`

# morse-code

We get a audio file `morse_chal.wav` which had morse audio. So used an online audio morse decoder tool and got this output for the audio file.
![Screenshot (47)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/06688feb-063b-41cd-8741-f7bc8dfebbdb)
After replacing the spaces with '_' , we get the flag.

The flag- `picoCTF{WH47_H47H_90D_W20U9H7}`

# credstuff

We get two files, a `usernames.txt` and `passwords.txt` file. As the instruction says that the first username corresponds to the first password, we need to find the serial number of the user `cultiris` to get his password. I opened both the text files on Notepad++ which shows the line numbers, I searched for `cultiris` and found the username in line number `378`. Then went to line number `378` on the `passwords.txt` file annd got this password ` cvpbPGS{P7e1S_54I35_71Z3}`. It's highly probable that the password is ROT13 encrypted so decoded it on CyberChef and got the flag.
![Screenshot (48)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/4abb0439-8e66-44e4-9ef1-2d3a6f6a89aa)

The flag- `picoCTF{C7r1F_54V35_71M3}`

# substitution0

So looking at the txt file, it looks jumbled at first and it's not smart to try any decoder on such a long text. Looking closely at `DECKFMYIQJRWTZPXGNABUSOLVH` and keeping mind the challenge name, It seems that the characters in `DECKFMYIQJRWTZPXGNABUSOLVH` corresponds to characters of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. So looked for an online character substitution tool and luckily, found one on CyberChef. I tried replacing `DECKFMYIQJRWTZPXGNABUSOLVH` with 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and the output started to look like it has something useful to offer. Since the text file had lower case characters too, I tried replacing `DECKFMYIQJRWTZPXGNABUSOLVHdeckfmyiqjrwtzpxgnabusolvh` with 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz' and got the flag.
![Screenshot (49)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/66d88a0b-bedb-44d3-a146-cd759cf07cd1)

The flag- `picoCTF{5UB5717U710N_3V0LU710N_59533A2E}`

# substitution2

This text file was difficult to understand and there was no clues on how to replace the  characters with other ones. The only thing visible was the curly braces at the end of the text file that suggested that the flag was somewhere around there. So while I was looking for some automatic character substitution solving tools, I came across one automatic mono alphabet substitution tool on [DCODE](https://www.dcode.fr/monoalphabetic-substitution). I decided to try it out and thankfully, it gave out the flag where I expected it to.\
![Screenshot (51)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/eee1eee0-1158-4799-b7c4-410cc0c5eb9f)


The flag- `PICOCTF{N6R4M_4N41Y515_15_73D10U5_42EA1770}`


 # New Caeser

 This one was a bit difficult for me to undestand at first but I did understand the first half of the python code given. To understand the rest half of the `b16_encode` function, I referred to this writeup by [vivian dai](https://vivian-dai.github.io/PicoCTF2021-Writeup/Cryptography/New%20Caesar/New%20Caesar.html).
 Wrote the code below with some help from the writeup.

 **import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

cipher_text = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

def b16_decode(solve):
    dec = ""
    for idx in range(0, len(solve), 2):
    
        c1 = solve[idx]
        c2 = solve[idx + 1]
        
        c1 = ALPHABET.index(c1)
        c2 = ALPHABET.index(c2)
        
        binary1 = "{0:04b}".format(c1)
        binary2 = "{0:04b}".format(c2)
        
        binary = int(binary1 + binary2, 2)

        dec += chr(binary)
    return dec

def unshift(c, k):
   
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def is_ascii(s):
    return len(s) == len(s.encode())
for letter in ALPHABET:
    
    dec = ""
    
    for i, c in enumerate(cipher_text):
        dec += unshift(c, letter)
    
    dec = b16_decode(dec)

    if is_ascii(dec) and " " not in dec:
        print("Flag: picoCTF{%s}" % dec)**

       

 The flag- `picoCTF{et_tu?_1ac5f3d7920a85610afeb2572831daa8}`
