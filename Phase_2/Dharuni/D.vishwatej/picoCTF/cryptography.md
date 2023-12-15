# basic-mod1
## GOAL
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message here. Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
## message
128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140 
## HINTS
1. Do you know what mod 37 means?
2. mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## WRITE UP

 Do the modulus operation by using the following code
```c
x=128,322,353,235,336,73,198,332,202,285,57,87,262,221,218,405,335,101,256,227,112,140
y=37
c = [str(num % y) for num in x]
print (c)

```
we get the following output
output = `['17', '26', '20', '13', '3', '36', '13', '36', '17', '26', '20', '13', '3', '36', '33', '35', '2', '27', '34', '5', '1', '29']`

Now i manually coverted the numbers according to the conditions given in question.

Now i wrapped this text in picoCTF{}

FLAG :- picoCTF{R0UND_N_R0UND_79C18FB3}

___

# miniRSA
## GOAL 
Let's decrypt this: ciphertext? Something seems a bit small.

## HINTS
1. RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
2. How could having too small an e affect the security of this 2048 bit key?
3. Make sure you don't lose precision, the numbers are pretty big (besides the e value)

## WRITE UP

given values in the text file.
```
N: 293319224997949857827359760455911649366830593805589503865601601057403432015133699390063075
311659227089496191626986236753490304308595478257089947083218037053094594380993404277705800644
009114318566569019827899482853099561118486869061526644733509404865074517712234358352601689712
100874708944484607455939568405865305279158025414500929465746948095848808966013175197944428629
774711293197813131618420565017150405559640118995890028637308686795271844207890105514750678629
077390549661831206214072463985180989811064312192076978702934121764404829001835504673751902398
98455201170831410460483829448603477361305838743852756938687673

e: 3

ciphertext (c): 220531641393113403107460374692824779903015522125251987265007301078204917985697
6080512716237308882294226369300412719995904064931819531456392957957122459640736424089744772221
933500860936331459280832211445548332429338572369823704784625368933 

```

Then i went up to the site [decode.fr for RSA cipher](https://www.dcode.fr/rsa-cipher)

Entered the values and thus we get the flag.

FLAG:- picoCTF{n33d_a_lArg3r_e_ccaa7776}

___
