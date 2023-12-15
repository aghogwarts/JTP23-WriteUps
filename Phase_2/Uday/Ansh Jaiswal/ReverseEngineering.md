# Keygenme-Py Rewritten

**Flag:** `picoCTF{1n_7h3_|<3y_of_ac73dc29}`

Let's begin by examining a file named `keygenme-trial.py` that we have been provided with. This file contains a block of source code that defines several variables:

```python
username_trial = "FRASER"
bUsername_trial = b"FRASER"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

It appears that the flag we're aiming to find is embedded within the template of `key_full_template_trial`.

The file also contains a function called `check_key`, which we can assume verifies if the flag/key we input is also a valid activation key. The function performs the following checks:

```python
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        # Similar checks for indices 5, 3, 6, 2, 7, 1, 8
```

The function checks if the dynamic part of the provided key matches a specific combination of elements from the hash of `username_trial`. The indices for these elements are **4**, **5**, **3**, **6**, **2**, **7**, **1**, and **8**.

The value of `hashlib.sha256(username_trial).hexdigest()` is determined by `username_trial`, which in this case is `FRASER`. Using this, we can find its value:

```python
>>> import hashlib
>>> username_trial = b"FRASER"
>>> hex = hashlib.sha256(username_trial).hexdigest()
'92d7ac3c9a0cf9d527a5906540d6c59c80bf8d7ad5bb1885f5f79b5b24a6d387'
```

If we loop through the required indices on the hashed value, we get:

```python
>>> for i in [4, 5, 3, 6, 2, 7, 1, 8]:
...     print(hex[i], end = '')
...
ac73dc29
```

Thus, the value of the dynamic key is `ac73dc29`, resulting in the full key `picoCTF{1n_7h3_|<3y_of_ac73dc29}`. When this key is used with `keygenme-trial.py`, we achieve a successful activation.

# GDB baby step 0

**Flag:** `picoCTF{549698}`

Here, we're given a binary `debugger0_a`, and our goal is to determine the value of the register `eax` at the end. We can use the `objdump` program with the `-D` flag for this:

```bash
~/Downloads $ objdump -D debugger0_a | less
```

Looking for the `main:` function, we find:

```assembly
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

The instruction `mov $0x86342,%eax` is of interest here. It sets the hexadecimal number `0x86342` as the value for the register `eax`. Therefore, the final value in `eax` is `0x86342` in hexadecimal or `549698` in decimal.

# ARMssembly 0

**Flag:** `picoCTF{5EE79C2B}`

We are provided with an ARM assembly source file named `chall.s`. The structure of the file is as follows:

```assembly
main:
    stp x29, x30, [[sp, -48]!
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

The two arguments provided to the file `266134863` and `1592237099` are converted to integers using the `atoi` function and are then stored in the registers `w0` and `w1` respectively. The function then branches out to the `func1` code block:

```assembly
func1:
    sub	sp, sp, #16
    str	w0, [sp, 12]
    str	w1, [sp, 8]
    ldr	w1, [sp, 12]
    ldr w0, [sp, 8]
    cmp w1, w0
    bls .L2
    ldr w0, [sp, 12]
    b  .L3
```

In this block, the values of `w0` and `w1` are compared. If `w1` is less than or equal to `w0`, the code branches to `.L2`. If not, it loads the value at the address 12 bytes offset from the stack pointer (essentially the integer value of `w0`) into `w0`, and then branches to `.L3`.

Since `w1` (1592237099) is greater than `w0` (266134863), the code branches to `.L3`:

```assembly
.LC3:
    add sp, sp, 16
    ret
```

This code block simply increments the stack pointer by 16.

Following this, the `.main` function resumes:

```assembly
    mov  w1, w0
    adrp x0, .LC0
    add  x0, x0, :lo12:.LC0
    bl   printf
.
.
.
```

The value in `w0` is copied to `w1`, and then the `printf` function is called to print the value at `w0`.

So, the result of running this code will be `Result: 1592237099`.

Converting this numerical value to hexadecimal, we get `5EE79C2B`:

```bash
~ $ printf "%X\n" 1592237099
5EE79C2B
```
