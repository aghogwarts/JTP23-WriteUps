### Description

What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: [ciphertext](./ciphertext)

### Approach

After searching for resources to solve this. I found the solution at [Crypto StackExchange](https://crypto.stackexchange.com/questions/6770/cracking-an-rsa-with-no-padding-and-very-small-e/6771#6771) .

In RSA, the message `m` is interpreted as an integer, then raised to exponent `e`, and the result is reduced by modulo `n`. `M**3 mod n = c`. This can also be written as `M**3 = k*n + c` for some padding `k`. So, this means that `M = invpow(k*n+c, 3)`. We just need to find the right padding`k`.

Given that `(M ** 3)` is only "barely" larger than `n`, We can use python and write a [solution script](./miniRSAscripy.py) [Got this script from [HHousen GitHub](https://github.com/HHousen/PicoCTF-2021/blob/master/Cryptography/Mini%20RSA/script.py)] to search though thousnads of values for k until we find one that contains the start of the flag. 

Run the script in terminal: `python3 miniRSAscripy.py`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/5b057bc9-7d4d-4155-bfa1-47b12c12d9f5)

**Flag:** picoCTF{e_sh0u1d_b3_lArg3r_60ef2420}
