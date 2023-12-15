# Pixelated 

## Goal

I have these 2 images, can you make a flag out of them? 

![scrambled1](https://github.com/vishwatejD/picoCTF/assets/141154035/2b882ecc-f010-4222-be01-08a54c9e9dc9)
![scrambled2](https://github.com/vishwatejD/picoCTF/assets/141154035/a6794735-80cd-41ce-884f-a2df57183297)

# write up

The stacking of images at a bit or pixel level can be done using softwares like stegsolve.

We install the software and open one of the images.

Then we select the analyse option and click on the image combine feature.

![Screenshot from 2023-12-14 23-37-28](https://github.com/vishwatejD/picoCTF/assets/141154035/8be28e5c-f569-4488-bc37-72955944dd5a)

Now we we select the other image and try various layers, planes and inversions. We get our required output in the ADD option.


![solved](https://github.com/vishwatejD/picoCTF/assets/141154035/b4482974-1d55-4e67-8eea-b020cbdad561)

**FLAG:- picoCTF{0542dc1d}**

___

# John_pollard
## Goal 
Sometimes RSA certificates are breakable
>given a rsa certificate named as cert


### Write up

if we open the certificate we find this.
![image](https://github.com/vishwatejD/picoCTF/assets/141154035/90829e10-9c65-4e41-a620-9f06368389e4)

This doesnot give us any important information about the key.

Thus we ask it through the terminal.
when we go to the directory where **cert** is downloaded and run the command 
` $ cat cert` 

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/ca96d56e-e3f5-4878-84af-4a29bbbbd26e)

We now go to the website [decode.fr](https://www.dcode.fr/rsa-cipher)

There we go to the RSA certificate reader to get the required values.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/339b41b8-773e-4000-b1e0-2d6ae1ea72d1)

From it we get the values of the modulus(n), e, and bits.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/0d4f8744-99e6-4cd8-a4d6-b0e891430cdb)

To understand how Rsa certificate works I referred to https://sectigostore.com/page/what-is-an-rsa-certificate/

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/bb219e0c-702d-4693-a267-c5993a81dd03)

The hint also conveys that the flag is of the form picoCTF{p,q} where p, q are the factors.

Performing prime factorisation on the obtained n (modulus) we get the factors as 67867967 , 73176001

> the factorisation can be done using online calculators like factordb or through terminal using the command `$ yafu "factorise <modulus>"`

 **Flag:- picoCTF{73176001,67867967}**

 ___

# Sum-O-Primes
## Goal

We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

[gen.py](https://github.com/vishwatejD/picoCTF/blob/main/cryptography/sum-o-primes/gen.py)
[output.txt](https://github.com/vishwatejD/picoCTF/blob/main/cryptography/sum-o-primes/output.txt)

### write up
The output.txt file consists of values of x( sum of factors p and q), c (cipher text), and n(modulus or product of factors).

to find the unknown values of p,q ,d and phi. I wrote the following code in python.

```python
from gmpy2 import isqrt
from Crypto.Util.number import long_to_bytes

x=0x1429cf99b5dd5dde9f016095be650d5b0a9a73e648aa72324cb8eb05bd14c1b913539a97f5417474f6014de830ad6dee028dd8908e593b1e99c4cc88f400127214036e71112292e58a2ccffc48f57524aee90f9858d935c7a86297a90c7fe48b80f6c4e8df9eaae501ef40da7984502457255fbc8a9e1574ec6ba210be134f192

n=0x64fc90f5ca6db24f7bfc6419de407596d29a9ecda526101b8d0eff2181e9b8ed1538a1cbabe4dfc5bcd899976e7739f8b448815b50db36a994c5b1df97981d562c663113fc5ee84f3206aecd18248fb4e9bddf205c8119e8437f7d6522e63d05bc357ae4969a4b3000b8226f8d142c23c4e38cdb0c385bf9564e8a115e4c52b7a2e3a9073a5d99d7bec3bca6452cf0c1b8d8b6b123cc6a6980cf14088d6a2bbb5ed36b85cb0003e535bd16d79ad54ff5b26e62f57de074654493d3a26a149786d5fbf61b42c9305092eb018aa3db3cb18b24f188ae520bd18acf9ffced09a2ba302a520f6e2bfd8eea9adc01eb8ee941181694a3ab493e1aa53fbbbf2851a591

c= 0x56ed81bbc149701110f0a15e2e6078ab926d74ee2c11b804ae4fad4333a25c247f38bb74867922438d10ce529b75f5ee5e29ce71d6f704cc0644f7e78d60a2af8921fbc49326280e3f0c00f2769e837363cbb05dc3f30bda8fdc94111fb025008eae562ae57029d5cfde6bdd09893a738187578d22f82a5f8769f093681662329f05b262c2054f91696a24f631ba8132f3d92ae7758c91fa9b5657e4944c5d5f93afb4af68908d004ae5f97071bcaceb7d0034297eeb897f972b44b0d7def52f46ee45d386a5e24ed613bf7e5177c6e10f69a3d3de0f0c30de0b15d360ee81da3d277a4acf47b6df389c24615884b692e604eba711fc28c34bc56227b8455705

e=65537
delta = x ** 2 - 4 * (-1) * (-n)
delta_sqrt = isqrt(delta)

p = (- x + delta_sqrt) // -2
q = (- x - delta_sqrt) // -2

print (p)
print (q)

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

print (d)

flag= pow(c, d, n)
print (long_to_bytes(flag))
```

I arrived at the formulae for p and q using basic mathematics as follows

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/3a050174-4c23-4851-80a7-23c3f920b5e5)

>the long_to_bytes() function converts the long string to bits.

 The output we get is 

 ![image](https://github.com/vishwatejD/picoCTF/assets/141154035/f0505e4f-783e-4ba7-9162-bfa3bf5ef5cc)

 The code can be stopped after finding p and q and we can use online rsa decoders for further task.
 https://www.dcode.fr/rsa-cipher

**Flag:- picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_24929c45}**



