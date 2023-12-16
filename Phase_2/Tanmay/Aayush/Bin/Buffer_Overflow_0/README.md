# PicoCTF Buffer Overflow Writeup

## Challenge Description

The challenge involved exploiting a buffer overflow vulnerability in a C program that used the `scanf` function to read user input. The program had a predefined buffer size of 100 characters, but it was possible to overflow the buffer by entering more than 100 characters.

## Exploiting the Vulnerability

The vulnerable code snippet was as follows:

```c
#include <stdio.h>

int main() {
    char user_buf[101];  // Vulnerable buffer with a size of 100 characters

    printf("Enter a string (up to 100 characters): ");
    scanf("%100s", user_buf);

    // ... (rest of the code)

    return 0;
}
```

By entering more than 100 characters when prompted for input, it was possible to overflow the buffer and manipulate program behavior.

# Exploit and Flag

Entering a specially crafted input resulted in a buffer overflow and revealed the flag: `picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}`

