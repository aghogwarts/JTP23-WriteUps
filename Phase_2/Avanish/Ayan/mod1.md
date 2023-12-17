# mod1
The challenge asks us to mod37 each number and map it to the given set of charcters


Comments in each line to explain the code

```
enc = "165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138 ".split()      #splits the given string into a list

mods = [i for i in range(0,37)]      #list of positions for mapping

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")         #list of charcters in the decrypted message

d = {mods[i]: chars[i] for i in range(len(mods))}           # a dictionry is created as mapping with positions and respective characters in the decrypted message here mods and chars are replacable in len() since both are of same length

for i in range(len(enc)):
    print(d[int(enc[i]) % 37], end='')     # this function prints out the respective values after modding by 37 and matching the values from the dictionary, normally this prints the message character by charcter line by line which is the default end argument, so we set the end to nothing to get the final decrypted message

GIVES OUTPUT : R0UND_N_R0UND_B6B25531 
```

Thus the flag is "picoctf{R0UND_N_R0UND_B6B25531}"
