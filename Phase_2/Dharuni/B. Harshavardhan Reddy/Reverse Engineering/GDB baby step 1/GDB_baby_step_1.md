### Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`. Disassemble [this](./debugger0_a).

### Hints

**[1]**(gdb is a very good debugger to use for this problem and many others!)

**[2]**(`main` is actually a recognized symbol that can be used with gdb commands.)

### Approach

Lets know what and how to use `gdb` which is given hint: `gdb --help`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/8ea753aa-3f8f-4fec-8eee-583a19985ded)

open the [file](./debugger0_a) using gdb: 
```
gdb debuuger0_a
```

and to get entry point 
```
info files
```

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/196cee66-e836-4d50-823f-09af9bbb9e6c)

Entry Point: 0x1040

But we need to information of functions: 
```
info functions
```

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/fbcf3125-d315-4c5e-ac74-da2318b92c85)

Our prime target here is the ‘main‘ function (address 0x1129)

 we’re now set to uncover the assembly code by entering 

```
 disassemble main
```
The disassembly process unveils the following:

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/aa5aabd3-91f5-4a17-9a58-f1484f086413)

'eax' register (address `0x86342`)

To get the flag we have change the hex to decimal number

Open python3 in terminal and convert hex: `int(0x86342)`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/96421fff-7e63-461a-b803-3652eb03e616)

we get `549698`

**Flag:** picoCTF{549698}
