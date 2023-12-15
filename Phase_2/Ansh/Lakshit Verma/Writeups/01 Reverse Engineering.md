# keygenme-py

**Flag:** `picoCTF{1n_7h3_|<3y_of_ac73dc29}`

For this, we're given a file `keygenme-trial.py`. In its source code block, we're given the following variable declarations

```py
username_trial = "FRASER"
bUsername_trial = b"FRASER"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

It seems that the flag we want is in the template of `key_full_template_trial`.

There's also a function `check_key` that presumably we need to test with to check whether the flag/key we enter is also a valid activation key or not. It performs the following checks

```py
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False
```

So it seems it checks whether the dynamic part of the given key is equal to the combination of elements of the variable `hashlib.sha256(username_trial).hexdigest()` with the indices **4**, **5**, **3**, **6**, **2**, **7**, **1**, and **8**.

The value of `hashlib.sha256(username_trial).hexdigest()` is controlled by the value of `username_trial`, which in this case is `FRASER`. Using this, we can get its value

```py
~ $ python3
Python 3.11.5 (main, Sep  2 2023, 18:29:07) [GCC 13.2.1 20230801] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hashlib
>>> username_trial = b"FRASER"
>>> hex = hashlib.sha256(username_trial).hexdigest()
'92d7ac3c9a0cf9d527a5906540d6c59c80bf8d7ad5bb1885f5f79b5b24a6d387'
```

Looping through the required indices on the hashed value, we get

```py
>>> for i in [4, 5, 3, 6, 2, 7, 1, 8]:
...     print(hex[i], end = '')
...
ac73dc29
```

Therefore the value of the dynamic key turns out to be `ac73dc29`, leading to the full key being `picoCTF{1n_7h3_|<3y_of_ac73dc29}`.

Using it on `keygenme-trial.py`, we get a successful activation

```
~/Downloads $ python3 keygenme-trial.py

===============================================
Welcome to the Arcane Calculator, FRASER!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy.
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, FRASER (a/b/c/d)? c

Enter your license key: picoCTF{1n_7h3_|<3y_of_ac73dc29}

Full version written to 'keygenme.py'.

Exiting trial version...

===================================================

Welcome to the Arcane Calculator, tron!
```

# GDB baby step 0

**Flag:** `picoCTF{549698}`

We're given a binary `debugger0_a` and our task is to figure out the value of the register `eax` at the end. We can use the program `objdump` with the `-D` flag for this

```
~/Downloads $ objdump -D debugger0_a | less
```

Searching for the main function `main:`, we get

```nasm
0000000000001129 <main>:
    1129:       f3 0f 1e fa             endbr64
    112d:       55                      push   %rbp
    112e:       48 89 e5                mov    %rsp,%rbp
    1131:       89 7d fc                mov    %edi,-0x4(%rbp)
    1134:       48 89 75 f0             mov    %rsi,-0x10(%rbp)
    1138:       b8 42 63 08 00          mov    $0x86342,%eax
    113d:       5d                      pop    %rbp
    113e:       c3                      ret
    113f:       90                      nop
```

Here, the instruction `mov $0x86342,%eax` is of interest to us here. In simple terms, it means the hexadecimal number `0x86342` is being set (`mov`) as the value for the register `eax`.

The value finally in `eax` is therefore 0x86342 in hexadecimal, or `549698` in decimal.

# ARMssembly 0

**Flag:** `picoCTF{5EE79C2B}`

We're given an ARM assembly source file `chall.s`. It's structured as follows

```nasm
main:
    stp x29, x30, [sp, -48]!
    add x29, sp, 0
    str x19, [sp, 16]
    str w0, [x29, 44]
    str x1, [x29, 32]
    ldr x0, [x29, 32]
    add x0, x0, 8
    ldr x0, [x0]
    bl  atoi
    mov w19, w0
    ldr x0, [x29, 32]
    add x0, x0, 16
    ldr x0, [x0]
    bl  atoi
    mov w1, w0
    mov w0, w19
    bl  func1
```

Here, the two arguments provided to the file `266134863` and `1592237099` are converted to integers via the `atoi` function and stored in the registers `w0` and `w1` respectively.
It then branches to the `func1` code block, which has the following code

```nasm
func1:
    sub sp, sp, #16
    str w0, [sp, 12]
    str w1, [sp, 8]
    ldr w1, [sp, 12]
    ldr w0, [sp, 8]
    cmp w1, w0
    bls .L2
    ldr w0, [sp, 12]
    b  .L3
```

In this, `w0` and `w1` are compared. If `w1` is lesser than or equal to `w0`, it branches to `.L2`. If not, it loads the value stored at the address 12 bytes offset (essentially the integer value of `w0`) from the stack pointer into `w0`, and then branches to `.L3`.

Since `w1` (1592237099) is greater than `w0` (266134863), the code branches to `.L3`

```nasm
.LC3:
    add sp, sp, 16
    ret
```

This just adds 16 to the stack pointer.

After this, the `.main` function continues

```nasm
    mov  w1, w0
    adrp x0, .LC0
    add  x0, x0, :lo12:.LC0
    bl   printf
.
.
.
```

This copies the value in `w0` to `w1`. It then prints using `printf` the value at `w0`.

So, the result of this code will be `Result: 1592237099`.

Converting the numerical value to hexadecimal, we get `5EE79C2B`

```
~ $ printf "%X\n" 1592237099
5EE79C2B
```

