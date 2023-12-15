### Approach used
After downloading the file, we will check its file type by 'file' command.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/26275905-a9cd-41ce-b772-5309143d3308)

It's an It’s an ELF (Executable and Linkable Format) file so we can use 'gdb' to allow us to see what is going on inside another program while it executes. Then we will type `info functions` to basically list all the functions in the program.
Then we can use `disassemble main` to enter this function and there we will find eax value so we will just convert it because it's in hexadecimal and we want it in decimal form so we will use [hexadecimal to decimal converter](https://www.rapidtables.com/convert/number/hex-to-decimal.html) and then use it in the general picoctf manner.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/1b0203af-3791-4a40-865c-59a885c93574)

* ![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/40061129-332b-4d45-a2ec-6953b7101ea3)

### Flag
> picoCTF{549698}

### Resources used
man page of GDB, [Use of GDB](https://www.geeksforgeeks.org/gdb-command-in-linux-with-examples/), [Info functions](https://stackoverflow.com/questions/10680670/ask-gdb-to-list-all-functions-in-a-program)
