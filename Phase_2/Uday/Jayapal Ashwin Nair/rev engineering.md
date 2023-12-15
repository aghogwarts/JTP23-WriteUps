### Keygenme.py

in the python code the static part of flag is already given which is : `picoCTF{1n_7h3_|<3y_of_` and later on dynamic part `xxxxxxxx`. In the code it first checks if the key we enter in progwwwram has the same length as the flag. Then it checks if the static part is same. For checking the dynamic parts 8 if statements are written:

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/ffff4489-e3a3-4234-87cf-45d8094700a9)

by executing this:

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/4eab9c7d-eb1f-499b-92f9-40f5b9a92de4)

we get the dynamic portion as _01582419


flag: picoCTF{1n_7h3_|<3y_of_01582419}

---

### GDB baby step 1

opening the file in gdb using : `gdb debugger0_a`

we can then see functions defined by `info functions` ,now onto seeing main `disassemble main`

we can see 0x86342 being moved to eax registry, after converting the hex valuue i get the flag.

flag: picoCTF{549698}

---

###  ARMASSEMBLY 0

on compiling the arm assembly code with given values the value is given, it's then converted to hex and used in flag

flag:picoCTF{F51E846F}
