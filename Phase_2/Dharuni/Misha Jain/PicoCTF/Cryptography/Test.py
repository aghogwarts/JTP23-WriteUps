from pwn import *

enc_flag = bytes.fromhex("51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959")
enc_text = bytes.fromhex("23661d392722201d397024331d392376631d3922701d3970761d3920711d3979")
dec_text = b'A'*32

key = xor(enc_text, dec_text)

flag = xor(key, enc_flag)
print (flag.decode())