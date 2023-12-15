## mod 1
Wrote code to implement the given instructions. Flag: picoCTF{R0UND_N_R0UND_B6B25531}

![mod 1_sol_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/ca7a6975-8389-4c5b-8828-c89a3f7a75cf)

![mod 1_sol_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/c7ab72f3-2218-45db-bb03-a9fed6d6e398)


## miniRSA
RSA encryption keys are generated using the product of two very large prime numbers and an exponent `e`. Encryption is more secure for larger primes and larger values of `e`.
used an online RSA decoder.

flag: picoCTF{n33d_a_lArg3r_e_606ce004}

![miniRSA_sol](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/4190128c-daa7-424d-8f03-371453d7021a)


## new caeser
From the given code it appears that there are two functions being used fo encryption.

The first function takes the first letter of the _plaintext_, converts it to 8-bit ASCII, splits it into half, takes the letters whose indices are at the decimal values of the split binary numbers, and adds it to the encoded string. We end up with 2 letters for every letter of the _plaintext_

The second function is a shift function that uses a key to shift the letters of the output from the first function. To do this we go lettter by letter. First, the offset is subtracted from the ordinal values of both the letter to be encoded and the key, and the sum of the values thus obtained modulo 16 is used as index to find the encrypted letter from `string.ascii_lowercase[:16]`. This function works in two steps: 

1. First a (ord = 97) is shifted to 0. This means that b => 1, c =>2, d =>3, ..., z => 25. This is done for both the character and the key whose value is fixed.
2. Now as we go through the characters, the above value changes for each letter, but remains fixed for the key. Both of them are added i.e the letter is _shifted forward_ by the key value. The `sum mod 16` value is taken as the index for `string.ascii_lowercase[:16]` to get the encrypted value.

![new_caesar_sol_B png](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/6192edca-78cb-42d8-b2a5-150d04501f80)

The above figure shows how the second function works. It can be used to write the decryption code, which is seen below.

![new_caesar_sol_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/3c36d6b1-e976-43ba-b74f-d6dbb0548b84)

From all the strings that are obtained, we need to identify the one we need. Since the challenge is named new caeser, we select the one starting with et tu? which references one of the most famous lines from Shakespeare's Julius Caeser.

flag: picoCTF{et_tu?_23217b54456fb10e908b5e87c6e89156}

## la cifra de
I tried all rot-n ciphers with no luck. I realised that the 4-digit numbers in the ciphertext might be years so I Googled all of them together. That led me to the Vignere cipher Wikipedia page. In order to decode the cipher without the key, I looked up online Vignere decoders. I used [this tool](https://www.boxentriq.com/code-breaking/vigenere-cipher) which identified `flag` as the key. Hence I obtained the flag.


flag: picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}

![la cifra de](https://github.com/aghogwarts/JTP23-WriteUps/assets/76529146/1b4debb5-1c25-43fa-9c7f-8b52d88c8e33)






