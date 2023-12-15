import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
cipher_flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
    count = 1
    hexaDeciNum = ['0'] * 100
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
        if count % 4 == 0:
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
    if count == 1:
        i = i-1
    hex_string = ''
    while i >= 0:
        hex_string += hexaDeciNum[i]
        i = i-1
    if hex_string == '':
        hex_string = '00'
    return hex_string

tmp = ""
guess_strings = ""
for i in range(1, 16):
    for e in cipher_flag:
        tmp += "{0:04b}".format((ord(e) - LOWERCASE_OFFSET + i) % len(ALPHABET))
        if len(tmp) % 8 == 0:
            guess_strings += chr(int(binToHexa(tmp), 16))
            tmp = ""
    tmp = ""
    print(guess_strings)
    guess_strings = ""
