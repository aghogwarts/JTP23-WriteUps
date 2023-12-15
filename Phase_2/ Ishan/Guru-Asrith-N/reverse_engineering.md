### writeup on reverse engineering

#### GDB baby step 1

opened the challenge    
downloaded the the file `wget https://artifacts.picoctf.net/c/512/debugger0_a`     
used `gdb debugger0_a`     
got stuck            
referred to writeups      
enetered functions . Didn't work     
entered info functions . worked      
made the syntax format as intel since it is the most widely used processor    
used `set disassembly-flavor intel`     
used `disassemble main`     
found eax and next to it the register number in hexadecimal format     
converted the hexadecimal format to decimal since it was asked in question     
got the decimal as '549698'     
got the flag     
```
flag : picoCTF{549698}
```


#### ARMassembly 0

opened the challenge     
downloaded the file `wget https://mercury.picoctf.net/static/b3b17204c7ce77f184a397c4fae4a35b/chall.S`   
used `file chall.S` . It is assembly source and ASCII text   
used `cat chall.S`    
didn't know what to do after this so referred writeups 'https://ctftime.org/writeup/26962'    
from writeup w0 =3854998744  and w1 = 915131509     
subtract w1 from w2 (smaller from larger)     
didn't understand so referred this 'https://www.youtube.com/watch?v=BMvda3d0dt8'    
converted largest value to 32 bit hexadecimal      
```
flag : picoCTF{e5c69cd8}
```


#### keygenme-py

opened challenge    
downloaded the file `wget https://mercury.picoctf.net/static/9cc50abd5b012891d5a1132e05f15a07/keygenme-trial.py`    
used `nano keygenme-trial.py`    
read through the code      
intial part of the flag is given and we have to the next part of the flag    
i didn't understand what to do after this so i referred to this writeup 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Reverse%20Engineering/keygenme-py/keygenme-py.md'    
the key length should be same as the flag length     
the numbers given in hashlib are the same number as the number of letters missing in the flag      
the number order given is 45362718 in hashlib      
used the following code although i didn't understand completely      
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
got the missing digits 'e584b363'    
got the flag 
```
flag : picoCTF{1n_7h3_|<3y_of_e584b363}
```
