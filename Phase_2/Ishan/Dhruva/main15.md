# picoCTF
.
## 1. tunn3l v1s10n
This is a CTF based on forensics.
A picture is given in the first file. Upon using
`exiftool tunn3l_v1s10n`
where exiftool is used for reading, writing and changing image and audio data.
A file that can be read, written and executed is returned, its filetype being bitmap(.bmp)
As the file's name is just `tunn3l_v1s10n`, we change it to 
`mv tunn3l_v1s10n tunn3l_v1s10n.bmp`
Any bitmap file is an uncompressed file which can store high quality images which uses raster graphics.
Proceeding forward, we can open the file using an online app like [Photopea](https://www.photopea.com/). Upon doing so the file shows a picture showing text that reads
_'notaflag{sorry}'_ 

![image](https://github.com/kua23/picoCTF/assets/61975172/a3f965e3-ead5-4ea6-9d59-101992ea265d)

Opening the file in an hexeditor like [HexEd.it](https://hexed.it/), we can observe that the height of the .bmp file is very small. Thus, once the hexdump (data converted from any other form to hexadecimal) is obtained, we can edit it in order to obtain the full image by increasing the height of the file.
The width of the file starts at offset 12 and goes on for a length of 4 bits, while the height starts at offset 16 and goes on for 4 bits too. On changing the height of the .bmp file to its width, by replacing _32 01_ with _32 04_ , thus increasing the height of the image and opening the file again with the text editor, we get the entire picture which contains the flag.
![image](https://github.com/kua23/picoCTF/assets/61975172/7a1fbc82-7370-41e0-8e44-3398d7ffdcc7)

Thus, we can conclude that the height of the file was extremely small compared to the original height of the file which contained the flag. 

![image](https://github.com/kua23/picoCTF/assets/61975172/749562e2-bbab-4c1b-bcea-5a2ae6c8f39d)

### Flag
`picoCTF{qu1t3_a_v13w_2020}`

## 2. Trivial FTP
First, a directory called _**tftp.pcanpng**_ is downloaded, which hosts a Trivil File Transfer Protocol which is used to store or extract a file from a remote host. Upon opening the directory using [Wireshark](https://www.wireshark.org/), and navigating to _File>Export Objects>TFTP_, all the files in the directory can be saved. Wireshark is a tool used to analyze network traffic, and perform actions like tracing connections and viewing contents of network transactions and protocols.

![image](https://github.com/kua23/picoCTF/assets/61975172/c0a5cd7a-35b1-4686-9975-48bb12d22bbb)

There exists a file called _**instructions.txt**_ which can be opened using
`cat instructions.txt`
from which we get a cipher:
_GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA_


This did look like a caesar cipher, and upon bruteforcing it using [this tool](https://www.dcode.fr/caesar-cipher), it was encoded as a _rot13_ file. Upon decoding the key, it returned
`TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
`

_'I will check back for the plan'_ must actually mean deciphering the plan file which upon doing so using [rot13](https://www.dcode.fr/caesar-cipher) gave 
`IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
`

Upon using the command 
`steghide info`
to check if there is any hidden message in the three photos, the first two files, _'picture1.bmp' and 'picture2.bmp'_did not return anything but the third file _'picture3.bmp_ returned an embedded _'flag.txt'_ when the passphrase `DUEDILIGENCE` is used to decode the hidden message in the pictures.

![image](https://github.com/kua23/picoCTF/assets/61975172/dd292599-43e1-4254-8519-b4f731a7733f)


Using the command `steghide extract -sf picture3.bmp`, where sf stands for stegofile we get the flag using `cat flag.txt`.

### Flag
`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`

## 3. MacroHard WeakEdge
This picoCTF is based on binwalk. Upon downloading the file _'Forensics is fun'_ , we can use binwalk on that file. This command is used for identifying and extracting embedded files and code that is executable. In simpler words, it is used to extract the content of binary files. 


Upon using `binwalk 'Forensics is fun.pptm'`, we get a list of unzipped files

Running `binwalk -e ‘Forensics is fun.pptm’`, we can use it to extract the unzipped files in the .pptm.
We get a new file called 'Forensics is fun.pptm.extracted' in our directory and upon navigating to it using 
``cd '_Forensics is fun.pptm.extracted'``
and using 
``ls -la ``
we get a list of files in the directory.
```
total 136
drwxr-xr-x  6 kali kali   4096 Nov  9 17:52  .
drwxr-xr-x 11 kali kali   4096 Nov 20 22:24  ..
-rw-r--r--  1 kali kali 100093 Nov  9 17:48  0.zip
drwxr-xr-x  5 kali kali   4096 Nov  9 17:52  _0.zip.extracted
-rw-r--r--  1 kali kali  10660 Jan  1  1980 '[Content_Types].xml'
drwxr-xr-x  2 kali kali   4096 Nov  9 17:48  docProps
drwxr-xr-x  7 kali kali   4096 Nov  9 17:48  ppt
drwxr-xr-x  2 kali kali   4096 Nov  9 17:48  _rels

```
Then using,
``strings ppt/vbaProject.bin``
wew get a line saying
`sorry_this_isn 't_it`
Upon changing the directory using,
`cd slideMasters`
and using
`strings hidden`, we get a string
`Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q` and upon removing all the spaces and using base64 we can decode it. 

### Flag
`picoCTF{D1d_u_kn0w_ppts_r_z1p5}`

## 4. caas
Cowsay as a service is a program in which a cow tells a message which the user inputs.
The server used here is node.js which is a cross platform, open source runtime environment. This ctf was an example of a command injection which is basically when a program which takes in a user input is manipulated in such a way that the user who inputs the command can extract information from the program host's system.
Thus, our first task is to see if the cowsay works as it is intended to work. Hence, we first use (https://caas.mars.picoctf.net/cowsay/hi) which returns the cowsay as intended.
![image](https://github.com/kua23/picoCTF/assets/61975172/9a989363-15f4-425e-82e6-494a180e76f8)

In order to use a command injection, we can use the same url and use
(https://caas.mars.picoctf.net/cowsay/hi;ls)
where the ; is used to end the first command and start a new command. This lists the files in the directory where the cowsay program is stored. This returns certain folders and files under which there is one .txt file and upon using (https://caas.mars.picoctf.net/cowsay/hi;ls;cat%20falg.txt), the flag is received.

![image](https://github.com/kua23/picoCTF/assets/61975172/9a0cc60b-0ecd-4b4d-93f6-99cf35925faa)

This command injection can be prevented by ensuring that users can only execute the program, but not obtain permissions to write and read it. 


### Flag
`picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`

## 5. Forbidden Paths
Upon entering the website, (http://saturn.picoctf.net:64403/), there is a list of _.txt_ files and a '..' file.
The problem statement gives that there are four directories into which we need to navigate in order to get the _flag.txt_ file. On first trying to navigate through the directories by just pasting the path,
`/usr/share/nginx/html/ ` it did not work. 

Hence, instead of that I just used
`../../../../flag.txt` 
where each `../` is used to climb the directory once, thuse `../` climbs to the usr directory, and then climbs to share, then nginx and finally html,
where it navigated into four directories and the flag file is provided. 

![image](https://github.com/kua23/picoCTF/assets/61975172/b73f163c-08a6-4ce8-9efd-8b55b650cf0a)

### Flag
picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}

## 6. Local Authority
The website which the user is directed to shows a username and a password which can be filled to get the flag, presumably... As there are no other elements present in the website, we can right click the page and go to the _**Inspect Source**_ option which shows an _index_ and a _style.css _ file.
![image](https://github.com/kua23/picoCTF/assets/61975172/3691a078-f351-46a5-a0ff-25049de9f040)

Upon entering any gibberish name and password, there pops a new file called _login.php_ which contains the code

![image](https://github.com/kua23/picoCTF/assets/61975172/2c864f95-ba47-4cc0-b71a-1e7da37de8e7)

```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )

```
Upon logging in using these credentials,. we can get the flag.

### Flag
`picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}` 

## 7. buffer overflow 0
First, we connect to the server 
`nc saturn.picoctf.net 55984`
This CTF is based on buffer overflow. Buffers are temporary memory storage regions that hold data temporarily while it is moved from one location to another.	+ Buffer overflow occurs when the amount of data in a website exceeds it storage capacity. Thus, the program attempting to store or write the excess data overwrites the adjacent memory locations. Upon seeing the code, we can deduce that if we find a fault in the segmentation, we get the flag. Segmentation fault occurs when a piece of code tries to read and write when it can only read a certain piece of code. It shows that the memory is corrupted. There are two types of buffer overflows: Stack-based and heap-based. 
In order to prevent buffer overflows, certain methods can be used:
Address Space Randomization - This moves around the address locations of data. However, buffer overflow attacks need to know the memory locations which makes it difficult for it to be carried out.
Data Execution Prevention - which prevents the code from being executed in non-executable regions.
```
void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
```
The flag is with `sigsegv_handler`, thus we need to trigger a segmentation fault.
```
void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
}

gets(buf1); 
vuln(buf1);
```
The `gets()` is called and reads the user input onto the stack, where the stack is the collection of different data types. However, there is a fault in the function as it write's the input without caring about the length. Thus we can take this to our advantage and overflow the length, pushing the input into the `vuln()` function that triggers a segmentation fault. Thus, by just printing a load of gibberish that has a long length, we get the flag.

Thus, buffer overflows can be used to corrupt a web application's execution stack, execute malware code and take over a machine

### Flag
`picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}`

## 8. Stonks
In this, the user has money from which a random share is picked after which the program asks the API token to the user.
```On first entering the first option when the program starts, we can type gibberish when the program asks us:
What is your API token?
jkggkiliugliugluifyuftckj
Buying stonks with token:
jkggkiliugliugluifyuftckj
Portfolio as of Mon Nov 13 09:24:44 UTC 2023


1 shares of QHJ
2 shares of FHR
7 shares of YA
1 shares of O
13 shares of PCTQ
5 shares of IIDQ
269 shares of LHC
185 shares of XP
13 shares of JPSF
66 shares of Y
523 shares of AO
629 shares of X
Goodbye!
```
This just provides shares as per the user's input in a random order
```
What would you like to do?
1) Buy some stonks!
2) View my portfolio
2

Portfolio as of Mon Nov 13 09:24:57 UTC 2023


You don't own any stonks!
Goodbye!

```
This shows that no stonks are owned.
On going through the source code `vuln.c`
```
char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);
```
In the given block of code, the input to printf is the data we can use to manipulate the code. 
If we provide format strings in the user input we can exploit it towards our advantage.
In the beginning of the buy_stonks function, the flag file is loaded and the code is copied to a buffer on the stack:
```
char api_buf[FLAG_BUFFER];
FILE *f = fopen("api","r");
if (!f) {
    printf("Flag file not found. Contact an admin.\n");
    exit(1);
}
fgets(api_buf, FLAG_BUFFER, f);
```
The `printf()` will pull information from the stack to match each format specifier. So if we overload it using `%p` format specifier which stands for a pointer address, we can exploit it.
```
What is your API token?
%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p
Buying stonks with token:
0x8ae83900x804b0000x80489c30xf7f67d800xffffffff0x10x8ae61600xf7f751100xf7f67dc7(nil)0x8ae71800x10x8ae83700x8ae83900x6f6369700x7b4654430x306c5f490x345f74350x6d5f6c6c0x306d5f790x5f79336e0x326663310x306131300xff8d007d

```
The underscores are used to separate the output,so it becomes easier to read. 
Also the 'nil' must be a padding operator, thus we conside only the hexadecimal digits after that.
Upon inputting the hexademical code to a [hexadecimal editor](https://www.rapidtables.com/convert/number/hex-to-ascii.html), and removing the unwanted parts, the value returned was 
`ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿ`
This can then be inputted into [this program](https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',4,true)From_Hex('Auto')&input=Cgk) to swap endianness.

![image](https://github.com/kua23/picoCTF/assets/61975172/8d2f0025-524f-4800-9462-8739db9ce053)

This reverses the strings every fourth letter and we get the flag. This was an example of big endian which is swapped to little endian, which is a way to store multibyte data types. The last byte of the multibyte data is stored first in little endian. This is then reversed to get the flag.

### Flag
picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}


## 9. GDB Baby Step 0
GDB, which stands for the GNU Project Debugger, allows us to debug a program step by step when it executes. You can disassemble your code and provide breakpoints in them and figure out the mistake using GDB.
The file given is an ELF(Executable and Linkable Format).
After downloading the file and opening the file using 
`gdb debugger0_a`, we can use `info functions` to understand which functions do what. The command returns:
```
Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
```

The problem statement asks what is in the _eax function_ in the _main_ register. According to a source, the RAX registor is an accumulator register that is used for arithmetic and data manipulation generally. The GDB provides a function called _'disassemble'_ which can be used to, as the name suggests, disassemble a function. Hence, we use:
`disassemble main` that returns:
```
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   %rbp
   0x000000000000112e <+5>:     mov    %rsp,%rbp
   0x0000000000001131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:    mov    $0x86342,%eax
   0x000000000000113d <+20>:    pop    %rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
```
Thus, we get the value next to the eax register, but it is in hexadecimal. Upon converting the hexadecimal value to decimal, we get the value as 549698, which is the flag.

### Flag
`picoCTF{549698}`

## ARMssembly 0
What is an ARM first? It is a family of CPUs based on reduced instruction set computer(RISC) architecture. They have two main states where they can operate: Instructions state and Thumb state. According to a writeup which I followed, this ctf could have been used by either reading the assembly code or by cross compiling it.  This ctf is based on cross compiling ARM assembly on x86, where x86 is a family of complex instruction set computer(CISC). Thus for cross compiling it, we need to install a cross compiler using 
``sudo apt install binutils-aarch64-linux-gnu`` and then from there, in order to cross compile it, we use:
```
aarch64-linux-gnu-as -o chall.o chall.S
aarch64-linux-gnu-gcc -static -o chall chall.o
```
Upon then using
`file chall.o`
we find that it is compiled for ARM aarch64, which is a 64-bit extension of the ARM family. But this code cannot be run by a x86_64 cpu. In order to emulate it we use QEMU, which emulates using dynamic binary translation. We can install it using,
`sudo apt install qemu-user-static` and run it using 
`./chall 3854998744 915131509  ` where we get the answer as 
`Result: 3854998744`

WE CAN ALSO USE,
Upon using `cat chall.S`
we get a block of assembly code.
For func1,
```
func1:
        sub     sp, sp, #16
        str     w0, [sp, 12]
        str     w1, [sp, 8]
        ldr     w1, [sp, 12]
        ldr     w0, [sp, 8]
        cmp     w1, w0
        bls     .L2
        ldr     w0, [sp, 12]
        b       .L3
```
the sub command is for three components, where `#16` which denotes a constant, has to be subtracted from `sp` and be stored in `sp`.
`sp` stands for stack pointer which is a place to store the memory address of the last element added to the stack.
In 
```
str     w0, [sp, 12]
str     w1, [sp, 8]
```
`str` which stands for store, stores the value of `w0` and `w1` which are user inputted in sp. 
The number is used to denote the offset, where for 
`str     w0, [sp, 12]`
The number is stored in w0 on the stack at offset 12
```
ldr     w1, [sp, 12]
ldr     w0, [sp, 8]
```
Here, `ldr` stands for load register, which is used to load the offset value of 12 into the variable w1 in the stack point.
`cmp     w1, w0` is used to compare the values of w1 and w0.
`bls     .L2`
bls stands for branch if less, which says that if w0 is smaller than w1, branch to .L2.
```
ldr w0, [sp, 12] 
    b   .L3
```
This loads a value into w0 and branches to L3

L2:
`ldr     w0, [sp, 8]` - loads a value from stack at offset 8 and loads it into w0

L3:
`add     sp, sp, 16` - The stack is filled by adding 16 to sp

Thus, the flag will be the smaller number, that is: 3854998744 in 32 bit hex string.

### Flag
`picoctf{e5c69cd8}`

## 11.babygame01

This is a game in which you, as a player move your character to try and reach the finish line. Upon reaching the finish line, which is just the 'X' it just says you "You Win" but doesn't return back any string. Some other points to be noted were that:
On moving to extreme right, your character would move to the level below and on the very left. Upon going to the extreme left, the character moves to a level above and the very right.
Thus, it could be inferred, that by going to the top left corner the game, you could find a segmentation fault. 
![image](https://github.com/kua23/picoCTF/assets/61975172/4484c504-af96-4f74-9a1b-c28c7cfec196)


Thus by going to the top left corner, we can observe that the 
`Player has flag:64` value becomes 64. Upon moving there four times, and on typing 'p' it changes to `Player has flag:46` and the flag is printed.

![image](https://github.com/kua23/picoCTF/assets/61975172/882e38dd-2bd2-4770-89e7-716f8cd2676a)


### Flag
picoCTF{gamer_m0d3_enabled_8985ce0e} 

## 12. Keygenme-py

Upon observing the source code, 
```
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

```

```
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n").
```
If this block of code returns true, then we might be able to get the flag

This shows the beginning part of the flag that is fixed and the part of the flag which depends on the username_trial and hashing which we encounter later on in the program. 

```
if len(key) != len(key_full_template_trial):
    return False
```
This shows that the length of the key is the same as `picoCTF{1n_7h3_|<3y_of_xxxxxxxx}`.

```
if key[i] != hashlib.sha256(username_trial).hexdigest()[x]:
    return False
else:
    i += 1

```
This part of the code, basically encrypts the value based on the `username_trial` using the Secure Hashing Algorithm in the order 45362718.

```
import hashlib
import base64


key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = b"SCHOFIELD"

potential_dynamic_key = ""

# where our input begins:
offset = 23

# positions in username_trial
positions = [4,5,3,6,2,7,1,8]

for p in positions:
    potential_dynamic_key += hashlib.sha256(username_trial).hexdigest()[p]

key = key_part_static1_trial + potential_dynamic_key + key_part_static2_trial
print(key)
print(len(key))
```
Upon using this code, we can get the flag for the last 8 positions.

### Flag
picoCTF{1n_7h3_|<3y_of_e584b363}

## 13. basic-mod 1
Ok, I'm proud of this as I did it on my own, but I would've been ashamed if I was not able to solve this. The problem statement states that we need to decipher a cipher which is based on mod 37. The ctf has provided a list of numbers and a set of instruction to perform this task.
```
l1 = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
l2 = []
for x in l1:
    rem = x % 37
    if rem >= 0 and rem <= 25:
        l2 += (chr(rem+65))
    elif rem >= 26 and rem <= 35:
        l2 += str(rem-26)
    elif rem == 36:
        l2 += '_'
print(''.join(l2))
```
This was the code written by me to get the flag. So let's break this down into smaller chunks.
```
l1 = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
l2 = []
```
Here, I've provided the list of numbers in the problem statement to the list l1. I have also initialized an empty list to l2

```
for x in l1:
    rem = x % 37
```
This statement starts a for loop. It basically states, for every element in the list l1, take the element and take its modulo with 37 and store it in the variable rem.

```
if rem >= 0 and rem <= 25:
        l2 += (chr(rem+65))
```
Here, the code states that if the rem variable is greater than or equal to 0 and lesser than 26, convert the number to an ASCII letter and add it to l2. the chr() function converts numbers into ASCII letters. I have added 65 to rem as the ASCII letters begin with the number 65.

```
elif rem >= 26 and rem <= 35:
        l2 += str(rem-26)
```
Now in this elif branch, I have asked the code to check if the number is greater than 25 and lesser than 36. If it is, the rem value is converted into a decimal number and added to the list l2. Here, we subtract 26 from the rem variable, as we want values ranging only from 0 to 9. We also convert this value into a string as it becomes easier to parse in a list.

```
elif rem == 36:
        l2 += '_'
```
In the last elif branch, if the rem variable is equal to 36, we add an underscore to the list 2. I have used '==' as this compares the values while a single'=' is an assignment operator.
`print(''.join(l2))`
This prints the flag, by printing the list and joining all the elements of the list wihtout any spaces.

### Flag
picoctf{R0UND_N_R0UND_B6B25531}


## New Caesar
```
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
```
Here, there is a lowercase offset of the order a, whcih is equal to 97. An offeset is babsically an integer which shows the distance between the beginning of an object and a given element. The alphabet string contains 16 letters starting from 'a' till 'p'.

```
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c)) #01100001 = 97
		enc += ALPHABET[int(binary[:4], 2)] #[0110] = [6] = 'g'
		enc += ALPHABET[int(binary[4:], 2)] #[0001] = [1] = 'b'
	return enc
```
This function first converts the letter into binary and then takes the first half and converts it into a letter. Then it takes the second half of the binary and converts it into another letter. This can be done as the binary has 8 digits.

```
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
```
The two encoded letters get shifted by a key where the values of these shifts are stored as t1 and t2. This function performs the caesar shift.

```
assert all([k in ALPHABET for k in key])
assert len(key) == 1
```
The key is only 1 character long. The key can be any one of the 16 possible letters.


Thus, we can write a program to bruteforce and loop over the 16 letters and add 16 possible shifts. Then take the binary, convert it into a number and get the character which we can use to decode the cipher.

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
We are creating a loop, and skipping every two characters. This is because every two characters in the cipher text actually represents a single character of the encryption based on the encode function in the main program. We need to get the half binaries and concatenate them together to get the full binary again. Each letter of the encryption is an index of the alphabet. So, by getting index we can convert it into the binary. We can convert that binary character into the corresponding ASCII character.

```
enc = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'
for key in ALPHABET:
  flag = ""
  print("Key:", key)
  for c in enc:
    flag += shift(c,key)
  print("Flag: ", b16_decode(flag))
```
We get the flag from this, by bruteforcing through every letter of the first 16 letters of the alphabet.


### Flag
picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}


## basic mod-2

So, in this program, we will need to find the inverse modulus of the given values with respect to 41 and then print the output to get the flag. The program I used to write this is:
```
import string

values = string.ascii_lowercase + "0123456789_"
l1 = [268, 413, 438, 313, 426, 337, 272, 188, 392, 338, 77, 332, 139, 113, 92, 239, 247, 120, 419, 72, 295, 190, 131]
flag = ''
```
Here, we first import the library called 'string'. We add the alphabets, numbers and the '_' to a variable called values, and we assign the list of numbers given to get the flag to a list called l1. We also initialize an empty flag variable.

```
for x in l1:
    ind = pow(x, -1, 41)
    flag += values[ind-1]
print(flag)
```
In this for loop, we iterate through every element in the list l1, The ind variable is equal to the inverse modulo of the number with the 41, where the pow() function is defined with the attributes (x^-1 % 41). This value is taken as the index with respect to values from which the flag is extracted.

### Flag
picoCTF{1nv3r53ly_h4rd_8a05d939}


## miniRSA
So, what is an RSA?
It is basically a type of encryption which uses two keys, a public key and a private key, for the encrypting process. The public key is used to encrypt the message while the private key is only provided to the user and is used to decrypt the message. It is a faster encryption, and one in which the data cannot be easily modified in the host.

It works on the principle of assymetric encryption and digital signatures.

First, two large prime numbers p and q are taken. Consider,
z = (p-1)(q-1)
n = p*q
Choose a number e between 1 and z.
d = (k*z + 1)/e is the formula for encrypting the minirsa. 
The private key pair is given by (n,d) while the public key pair is given by (n,e).
m is the plaintext and c is the cipher text.
Thus to encrypt the data, we use c = (texttobeencypted)^e mod n
And then to decrypt the data, we use (c^d) mod n.


E is a small number, where ideally it has to be a large prime number, so we could conceivably compute the cube root.
Thus, [this website](https://www.dcode.fr/rsa-cipher) could be used to find out the flag
![image](https://github.com/kua23/picoCTF/assets/61975172/c0aa58cb-927a-4091-a95a-e72d7f340549)


### Flag
picoCTF{n33d_a_lArg3r_e_606ce004}





