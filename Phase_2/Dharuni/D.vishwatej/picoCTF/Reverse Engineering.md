# ARMssembly 0
## GOAL
What integer does this program print with arguments 182476535 and 3742084308? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

# HOW ARM ASSEMBLY WORKS

I referred to these sites to know about ARM assembly

(https://azeria-labs.com/arm-instruction-set-part-3/)

(https://developer.arm.com/documentation/ddi0487/latest)

# WRITE UP

The file is written in ARM assembly language. To read this code we need a compiler.

> RESOURCE USED:- https://github.com/joebobmiles/ARMv8ViaLinuxCommandline

1.we now install a Cross Compiler
 `$ sudo apt install binutils-aarch64-linux-gnu`

2. Now Compiling ARMv8
 
 `aarch64-linux-gnu-as -o chall.o chall.S`
 
 `aarch64-linux-gnu-gcc -static -o chall chall.o`

we need to install a version of QEMU that runs statically in the background with the following command `sudo apt install qemu-user-static`. Now we can run ARM binaries without any issue.

Now running the program with given arguments, `./chall 182476535 3742084308`

>Result: 3742084308

convert this into hexadecimal using [decode.fr](https://www.dcode.fr/hexadecimal-system)

>Result: df0bacd4

**Given Flag format**: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits

So,
FLAG :- **picoCTF{df0bacd4}**

____

# GDB baby step 1
## GOAL
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Disassemble this.

## HINTS
1.gdb is a very good debugger to use for this problem and many others!
2.main is actually a recognized symbol that can be used with gdb commands

## WRITE UP

I downloaded the file and ran the ` $ file debugger0_a` command on the downloaded file.
It said it was
![image](https://github.com/vishwatejD/picoCTF/assets/141154035/53ca3e3a-7eed-43d4-ae6a-7958be0c5d20)

~~ first i ran the file on ghidra hoping to find any clues, but i didnt find any~~

Using the hint given i used the following command

`$ gdb debugger0_a`

Our ultimate goal is to reach the main function.

 Thus , i used `$ info functions`
 
>NOTE:- info functions prints the names and data types of all defined functions

Now I used `disassemble main`

As we see, we have 0x86342 beside eax register.

We convert this into decimal --------> according to the question.

> RESOURCE USED:- https://stackoverflow.com/questions/10680670/ask-gdb-to-list-all-functions-in-a-program

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/8b1b37e6-7843-41de-9acb-fb7c3aea75bb)

format for flag:- picoCTF{decimal}

FLAG:- **picoctf{549698}**


____

# keygenme-py
## GOAL

[keygenme-trial.py](./keygenme.py)
## WRITE UP

In the code it is given that 

```c
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
```
it is half of the flag , we need to find the next part of the flag that is `key_part_dynamic1_trial = "xxxxxxxx"` using the code.

After analysing the code we understand that each of the digits of xxxxxxx are hashed as follows

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/23d3abe4-3f37-41e0-8a69-a74f590ec0e9)

The no of if commands matches with the number of characters needed for the key.

> Note:- the i here is being rewritten and added with 1 to replace the next place.

To retrieve the key i typed the following code.

```c
import hashlib

username_trial = "GOUGH"



print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[4])

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[5])

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[3])

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[6])

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[2])

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[7]) 

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[1])

print(hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[8])

```
we get the output as `f911a486` 

Thus the flag is ,

FLAG:- **picoCTF{1n_7h3_|<3y_of_f911a486}**



