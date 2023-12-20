# new-caesar

1) There is a Python code linked to the question which contains a new encryption method for strings.
2) After analysing the code, I see that in this decryption technique:
   - first, a character is extracted from the given string in the question
   - then it takes its ASCII value into binary and splits it in half, where the alphabet is only the first 16 letters.
   - It then applies a shifting method with a key which is only one character.
3) I then created a new function for decoding this code.

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/e2994c2b-c57b-4807-b9ed-7c78d1f09cda)

5) It basically takes the given flag goes through all 16 alphabets and then decodes each time.
    - It takes the 4-bit binary code for each character
    - It then adds the 4-bit binary for a pair of characters.
    - It then converts the binary into an ASCII integer and then into a character.
 6) Using this a list of text came after executing the code.

    ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/06c4243b-302f-461a-9bcb-8acb1f828ff7)

7) When the key is 'g', a suitable flag comes up which I then use to complete the challenge.

# miniRSA

1) According to the question there is an RSA key given which I opened up on my notepad application.
2) I analyzed it and saw that each key was a part of the main RSA key which needed to be decoded
3) Using the website https://www.dcode.fr/rsa-cipher I decoded the key and the required flag came.
 
   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/d532fbb9-8dc3-4d2e-b85b-f1d32d45fbe6)

  # Flag

  picoCTF{n33d_a_lArg3r_e_ccaa7776}

# basic-mod1

1) According to the question, there is a list of numbers that are given. We need to apply mod 37 to find the key using given data.
2) I then put the list onto a python code and then used a decryption method to unscramble the data to get the flag
   
   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/eef069a4-68e3-4fee-b3fc-362d17a949b6)

3) the required key then came after running the code

    # Flag

   picoCTF{R0UND_N_R0UND_79C18FB3}

