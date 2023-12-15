## ARMssembly0
Looked up solution online since I don't know how Assembly is written. After going through the first function, it looked like the code was just printing the first number `w0`. Converted that into hexadecimal and obtained the flag.

flag: picoCTF{f51e846f}

## GDB Baby Steps 1
Looked online for a GDB tutorial, also learnt basic Linux 64-bit Assembly in Intel Syntax. The given file was found to be an  ELF 64-bit LSB pie executable, which is usually compiled code. Using the command `lay next` in GDB, it was found that the value assigned to eax at the end of the main function is `0x86342`, whose decimal value was the required flag. The default syntax used in gdb is AT&T which was a problem since I had learnt Intel syntax.

![GDB_1_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/e620b614-0356-44f0-88ce-bbf52bcdd270)
![GDB_1_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/06c8d03f-c184-4bac-bab5-de7e01a7c00a)
![GDB_1_B2](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/25919dbe-e92d-4452-a782-6c029dbe948f)
![GDB_1_C](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/b41910e7-3d75-4508-9465-4ce742dfef41)

flag: picoCTF{549698}

##  keygenme-py
The given file contains a function that checks for the validity of the key. Once this fact is known, it is only a matter of using the given code to reverse engineer the key, which is the flag we need.

flag: picoCTF{1n_7h3_|<3y_of_01582419}

![keygenme-py_sol_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/92b65bea-ad5d-4bc9-9e4e-73a3e8ef8ff3)

This part of the `check_key` function reveals the dynamic part of the key, using which the whole key can be reconstructed thus:

![keygenme-py_sol_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/af7b1e07-e2b0-4bc7-ade1-f5c4ab26eb64)
