GDB lets you see what’s happening inside your program while it’s running and you can explore your code in depth.With GDB, you can disassemble code. This means breaking a program down into smaller parts, a handy feature when working with low-level languages or inspecting compiled programs.It also lets you inspect registers – high-speed storage areas in a CPU


The EAX register is one of the general-purpose registers in the x86 and x86-64 architecture, which are commonly used in Intel and AMD processors. The name "EAX" stands for "Extended AX," where "AX" originally referred to the accumulator register in the older x86 architecture.The question is asking us to find what is in the eax register which is present in the main function.

So first we run the file with gdb using the command:

gdb debugger0_a

Now to see all the functions, we can put the command 'info functions' into the gdb prompt and we see the function 'main' along with many others. To uncover more about this function, we can run the code:

dissassemble main

When we do this, we see a number next to the eax register: 0x86342.
Hence we have our answer, however the number is in hexadecimal format, and we need to convert it to a decimal format:

The flag is picoCTF{549698}
