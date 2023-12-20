<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - GDB baby step 1 Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup explains the process of solving the "Baby Steps 1" challenge in PicoCTF, which is part of the GDB (GNU Debugger) category. The challenge requires analyzing a given binary using GDB to find the hidden flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 09, 2023

<b>Tools Used:</b><br>
- Terminal
- GDB (GNU Debugger)

<b>Challenge Description:</b><br>
In the "Baby Steps 1" challenge, we are provided with a binary executable file. The goal is to use GDB to analyze and run the binary, ultimately discovering the hidden flag.

<b>Exploitation:</b><br>
1. Open your terminal and navigate to the directory containing the "debugger0_a" file.

<p align = 'center'>

![](<Pictures/GDB - Download.png>)

</p><br>

2. Check the file type. This shows us its an Executable and Linkable Format file. It also shows that its a 64-bit executable and that its not stripped.

<p align = 'center'>

![](<Pictures/GDB - File_Type.png>)

</p><br>

- ELF File:<br> An ELF file is a common file format used for executables, object code, shared libraries, and even core dumps on Unix and Unix-like systems, including Linux. ELF is a binary format that defines the structure and organization of executable files and their associated data, such as symbols and sections.

- 64-bit Executable:<br> The file is designed to run on a 64-bit CPU architecture. This indicates that it's compiled and optimized for 64-bit systems, which can take advantage of 64-bit registers and memory addressing, allowing for better performance and handling of larger data sets.

- Not Stripped:<br> When a binary is not stripped, it means that the debugging symbols and other debugging information have not been removed from the binary during the compilation process. This is important for debugging and analysis because it allows tools like GDB (GNU Debugger) to associate machine code with source code, making it easier to debug and trace issues in the program.<br><br>

3. Start GDB by running the following command.<br>

<p align = 'center'>gdb debugger0_a</p><br>

4. Then, since we need to locate the main function, lets list all the functions.<br>

<p align = 'center'>info functions</p><br>

<p align = 'center'>

![](<Pictures/GDB - GDB_Start.png>)

</p><br>

4. The syntax for GDB is set to AT&T by default. To use Intel syntax, type the following command.<br>
<p align = 'center'>set disassembly-flavor intel</p><br>

5. To disassemble the assembly code of the main function in this file, we use the following command.<br><p align = 'center'>disassemble main</p><br>

We need to search for the contents of the "eax" register. The contents are in hexadecimal ("0x86342").<br>

<p align = 'center'>

![](<Pictures/GDB - Disassemble.png>)

</p><br>

5. Using python, we can easily convert the hexadecimal number to decimals.<br> <p align = 'center'>print(int(0x84342))</p><br>
We get the number 549698 as decimal. Hence, the pico flag is picoCTF{549698}.

<b>Conclusion:</b><br>
The "Baby Steps 1" challenge in the GDB category of PicoCTF introduced us to basic binary analysis using GDB. We viewed functions, disassembled them, and inspected variables to uncover the hidden flag.

</font>