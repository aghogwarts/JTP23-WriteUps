### Approach used
After downloading the file, we can first observe the properties of the fil so for that we will use 'exiftool'. So, command will be `exiftool cat.jpg`.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/5f202d46-5c42-4515-bca6-63d65acdad15)

Here we can see that the license looks a bit weird and seems base64 coded, so we can just decode this base64 text to get the flag.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/5d1fe6c3-a2ee-45b3-a1ff-664a2762a7c3)

### Flag
> picoCTF{the_m3tadata_1s_modified}
