### Description

What integer does this program print with arguments 3854998744 and 915131509? File: [chall.S](./chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

### Apporach

S files are source code files written in assembly. Either we have to manually read the code or we have to compile and run the code.If you understand ARM assembly, reading it is probably easier than compiling and running it. But I don't have any knowledge about ARM assembly.

To learn how to cross compile ARM assembly on x86, which is what we will be doing, the following resources are helpful:

* [Running Arm Binaries on x86 with QEMU-User](https://azeria-labs.com/arm-on-x86-qemu-user/)
* [Running ARMv8 via Linux Command Line](https://github.com/joebobmiles/ARMv8ViaLinuxCommandline)

To cross-compile ARMv8 code on a non-ARMv8 machine, a cross compiler is required. Fortunately, the GNU project provides a set of cross compiler tools suitable for ARMv8 development. To install these tools on Ubuntu or other Debian-based systems, execute the following command:

`sudo apt install binutils-aarch64-linux-gnu`

utilize the following commands to perform cross-compilation for the ARM assembly code challenge.

```bash
aarch64-linux-gnu-as -o chall.o chall.S
aarch64-linux-gnu-gcc -static -o chall chall.o
```
With the binary in hand, we can employ the [chall](./chall) command to confirm its compilation for ARM aarch64 architecture. Nonetheless, as x86_64 systems are incompatible with this code, emulation becomes necessary. To facilitate this, we can install a QEMU version configured to run statically in the background:

`sudo apt install qemu-user-static`

This allows us to execute ARM binaries seamlessly on the x86_64 system as if they were regular programs.

Finally, we can run the challenge binary with the two provided arguments: `./chall 3854998744 915131509` to get the answer: Result: `3854998744`

Convert the result into hex:
```python
>>> print("picoCTF{"+str(hex(3854998744)[2:])+"}")
picoCTF{e5c69cd8}
>>> 
```
**Flag:** `picoCTF{e5c69cd8}`

[Resource](https://picoctf2021.haydenhousen.com/reverse-engineering/armssembly-0)
