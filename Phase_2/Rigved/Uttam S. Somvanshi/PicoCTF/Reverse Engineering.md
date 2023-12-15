## Challenge: keygenme-py  
Logged into webshell and downloaded the python script. Then executed it via python3 command to see the calculator interface. b is locked and a requires me to mention a star system. c seems to be where i enter the keyphrase.  
Used nano command to look at the code.  
From the code i noticed the key structure:  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/c02b19f8-b6f4-4072-9aa2-a13c96131972)  
I also got the list of star systems which i will use in the calculator now.  
I used different star names but only got the estimated mana burn not anything that looked like akey.  
I couldnt understand the code completely so i referred 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Reverse%20Engineering/keygenme-py/keygenme-py.md'.  
I understood that the key must be entered in the license area which will unlock b option.  
And also that the key is of the same length as that of the ctf flag given above in the structure.  
Because of the writeup above i was able to understand that the first half of the static key is part of the key, i.e. "picoCTF{1n_7h3_|<3y_of_"  
The remaining unknown values are equal to the number of if statements. If x is replaced in the provided order of 45362718 i complete the key.  
The next step is heavily influenced by the writeup and it took me a while to understand it.  
What has been done is that parts of the code is taken to another python file which includes the required library i.e. hashlib, the given trial username which in my case is "SCHOFIELD" along with the structure of full key template as well as the 8 if statements with the given x values in sequence:  
```
import hashlib  
username_trial = "SCHOFIELD"  
bUsername_trial = b"SCHOFIELD"  

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"  
key_part_dynamic1_trial = "xxxxxxxx"  
key_part_static2_trial = "}"  
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial  

print(hashlib.sha256(bUsername_trial).hexdigest()[4])  
print(hashlib.sha256(bUsername_trial).hexdigest()[5])  
print(hashlib.sha256(bUsername_trial).hexdigest()[3])  
print(hashlib.sha256(bUsername_trial).hexdigest()[6])  
print(hashlib.sha256(bUsername_trial).hexdigest()[2])  
print(hashlib.sha256(bUsername_trial).hexdigest()[7])  
print(hashlib.sha256(bUsername_trial).hexdigest()[1])  
print(hashlib.sha256(bUsername_trial).hexdigest()[8])
```
This gave the result "e584b363"  
So the flag is "picoCTF{1n_7h3_|<3y_of_e584b363}"
## Challenge GDB baby step 1  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/baf187d5-f1fa-426e-9ed9-e440813bb351)  
Using gdb, i look for main function:  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/24a3825a-3d12-49d5-aed5-75614a51269c)  
For convenience i make the syntax format intel and then disassemble:  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/bae4fbc5-560b-49bb-a0f5-87fb626f7001)  
Now i focus on eax register as instructed. It is visible that the hexadecimal value in eax register is '0x86342'.  
Converting that to decimal via 'https://www.binaryhexconverter.com/hex-to-decimal-converter', n = 549698.  
Flag: picoCTF{549698}
(I took help from the commands given in primer.picoctf.org)  
## Challenge: ARMssembly 0  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/47a5b59b-b05b-4301-9629-9783145a2468)  
Here i was not familiar with ARM assembly so i referred 'https://ctftime.org/writeup/26962' to figure out what was happening.  
~~
 2 values are there - '3854998744' i.e. w0 and '915131509' i.e. w1 stored on the stack at offset address 12 and 8 respectively.  
Then we load the value at offset 12 on the stack into w1 and offset 8 into w0.  
And compare by substracting w0 from w1 = '2939867235'  
~~  
I could not understand the functioning so i referred 'https://youtu.be/BMvda3d0dt8?si=AsMBk8z5NFty7an5'  
Following this i converted the largest value to 32 bit hexadecimal and got the flag.  
Flag picoCTF{e5c69cd8}  
-----x---x-----
