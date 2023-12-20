# base mod1 Challenge Writeup

## Challenge Overview

Encountering a mysterious message being passed around on the servers, I took on the challenge of creating a decryption program to unravel its meaning. The decryption involved taking each number in the message, applying a modulo operation with 37, and mapping the result to a character set.

## Solution Approach

1. **Custom Decryption Program (`decrypt.c`):**
   - Leveraging my programming skills, I crafted the `decrypt.c` program to outline the decryption scheme.

2. **Mapping Numbers to Characters:**
   - The program performed the essential task of taking each number in the message, applying a modulo operation with 37, and mapping the resulting values to the specified character set.

3. **Flag Formatting:**
   - Wrapped the decrypted message in the picoCTF flag format: `picoCTF{decrypted_message}`.

## Flag

The decrypted message, formatted as the flag, is:

`picoCTF{R0UND_N_R0UND_79C18FB33}`
