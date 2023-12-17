# mod2
This challenge is similar to the previous challenge, the indexing is 1-38 instead of 0-37, and we are asked to calculate inverse mod41 which is

Regular Mod : enc[i] % 41

Inverse Mod : enc[i]^-1 % 41 ===== 1/enc[i] % 41

```
enc = "268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131".split()    #new encyption

mods = [i for i in range(1,38)]           #new indexing

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")      #same character set as previous code

d = {mods[i]: chars[i] for i in range(len(mods))}       # same dictionary defintion as previous code

for i in range(len(enc)):
    print(d[pow(int(enc[i]),-1,41)], end='')        # here i used the power statement syntax since the regular one was showing syntax error


DECRYPTED OUTPUT : 1NV3R53LY_H4RD_8A05D939
```

Hence the flag is "picoctf{1NV3R53LY_H4RD_8A05D939}"

