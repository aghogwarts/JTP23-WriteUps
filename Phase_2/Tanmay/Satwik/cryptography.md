#### NEW CEASER
I open the challenge
i see the code provided is in python, i don't know a lot of python so i decided to go through basics of it from youtube so i get bit of idea of what's going on
I know what base 16 is from the earlier challenges so i got that function then i used chat gpt to understand the shift function in the encryption!
i had a rought idea of the encryption's working.
so i with the help of GPT i try writing a code do decrypt(cuz all my experience in python is 2 hours at this point) but it didn't work cuz GPT ofc
then i watched the solution video on youtube, from there i get that i got the logic correct and tried getting the logic and tried writing the code on my own, i figured the solution will just have an extra decode function and the value of the variable `enc` as the encryption
````
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def b16_decode(enc): 
    dec = ""
    for i in range(0, len(enc), 2):
      binary = "{0:04b}" .format(ALPHABET.index(enc[i])) + "{0:04b}".format (ALPHABET.index(enc[i+1]))
      dec += chr(int (binary, 2))
    return dec

enc = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
for key in ALPHABET:
  flag =""
  print("Key:", key)
  for c in enc:
       flag += shift (c, key)
  print("Flag: ", b16_decode(flag))
  ````
  this is my final code i run it work with a few garbage value i get the key ` et_tu?_5723f4e71a0736d3b1d19dde4279ac03`
  ![image](https://github.com/s4twik/picoctf/assets/147993943/bafa495e-24f5-4826-a0c4-6fb6521c5903)


#### miniRSA
i looked up how does a RSA encryption work, got a reaally great lecture from eddie woo on YouTube
then i tried running it through a decyphering website and i got the flag.
![image](https://github.com/s4twik/picoctf/assets/147993943/8999091a-400e-4daf-a89a-729fc3716827)
![image](https://github.com/s4twik/picoctf/assets/147993943/4ae6ec05-4779-41b3-b2cc-809642a18c29)

#### basic-mod1
easiest one tbh!
found the modulo 37 of each number using python
````
numbers = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]

result_mod_37 = [num % 37 for num in numbers]

print("Original Numbers:", numbers)
print("Modulo 37 Result:", result_mod_37)
````

then i put the array found in this following code

````
def map_to_charset(mod_results):
    charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
    mapped_result = [charset[num] for num in mod_results]
    return "".join(mapped_result)

# Using the previously calculated mod results
mod_results = [17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 0, 3, 3, 27, 33, 4, 2, 28]

mapped_result = map_to_charset(mod_results)

print("Mapped Result:", mapped_result)
````
![Screenshot from 2023-12-15 20-27-54](https://github.com/s4twik/picoctf/assets/147993943/fa4b838a-372f-47b5-ba37-82686407a455)

![Screenshot from 2023-12-15 20-28-05](https://github.com/s4twik/picoctf/assets/147993943/d9e14ff4-1a24-487f-8d7d-766f8ce08f64)

