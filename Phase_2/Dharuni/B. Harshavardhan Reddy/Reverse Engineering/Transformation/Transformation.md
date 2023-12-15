### Description

I wonder what this really is... [enc](./enc)

**HINT:** ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

### Approach

Using python3 in termianl
```code
>>> enc=open("enc").read()
>>> print(enc)
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽
```
```
>>> print(enc[0])
```
`灩`

```
>>> print(hex(ord(enc[0])))
```
`0x7069`

```code
>>> for c in enc:
...     print(hex(ord(c)).lstrip("0x"),end="")
```
>`7069636f4354467b31365f626974735f696e73743334645f6f665f385f37356434383938627d`

```code
>>> hex_string = "7069636f4354467b31365f626974735f696e73743334645f6f665f385f37356434383938627d"
>>> byte_string = bytes.fromhex(hex_string)
>>> ascii_string = byte_string.decode("ASCII")
>>> print(ascii_string)
```

Output: `picoCTF{16_bits_inst34d_of_8_75d4898b}`
