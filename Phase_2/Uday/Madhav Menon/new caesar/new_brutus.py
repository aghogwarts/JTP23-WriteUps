import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
encoded = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def decode(encoded):
	decoded = ""
	for i in range(0,len(encoded),2):
		bin = "{0:04b}".format(ALPHABET.index(encoded[i]))+"{0:04b}".format(ALPHABET.index(encoded[i+1]))
		decoded += chr(int(bin,2))
	return decoded

for j in ALPHABET:
	key = j
	flag = ""
	for k in encoded:
		flag = flag + shift(k,key)
	flag = decode(flag)
	print("\nkey : ",key)
	print("iska flag : ",flag)
	print("\n")