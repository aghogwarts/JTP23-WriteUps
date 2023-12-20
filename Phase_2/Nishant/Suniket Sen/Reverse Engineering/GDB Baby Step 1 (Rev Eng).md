This one was comparatively easy.
First I watched a whole video on GNU and GDB to understand what am I dealing with here.  
I watched a video on how to use GDB to disassemble the file.  
I used Kali Linux CLI to operate further.  
I downloaded the gdb package into my computer using _sudo apt install gdb_ and loaded the file *debugger0_a* into it.  
Then all I did was type _disassemble main_ in the Terminal ans voila a hex eax register number was right on there waiting for me!
I transtaled the hex number into decimal and got the flag as _picoCTF{549698}_

![Screenshot 2023-11-16 155923](https://github.com/SuniCoder9567/Crypt0n1t3/assets/89261516/9b833c5f-edb1-48aa-91cf-e447f97f8959)
