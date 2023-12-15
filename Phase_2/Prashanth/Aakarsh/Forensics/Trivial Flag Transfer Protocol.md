### Approach used
* First we will download the file and using [Wireshark](https://www.wireshark.org/) (which basically is a file pockets analyzer) we find the TFTP objects and save the different txt and bmp files in a folder named 'tftp pcapng'. Ater that we will open a file we got, called 'instruction.txt' and after opening we get a sequence of different letters. So we will just go to [dcode website](https://www.dcode.fr/cipher-identifier) which identifies the sequence of characters as a ROT13 cipher. So, we will just decode it.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/3ce78b69-4631-4c8f-bdba-414acc957569)

* Now we read the second txt file that is named 'plan'. It looks like the sequence given in it is also rot13 encoded so we will just go to [ROT13 decoder](https://rot13.com/) and get the decoded text.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/0b17e29a-ce71-4d13-8282-cd599d2e2ae3)

* The text say "hid it with DUEDILIGENCE " which probably means it is the password. Also, it tells us to check the photos and we also saw 'deb' file where we saw a tool steghide being used which basically hides data in bmp,jpeg,wav files. We also steghide to extract the data from the photos.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/0f3bfad5-2e5d-4310-bd91-abf623de984c)

* Using `steghide extract -sf __________` we can find the data kept inside the photos and use the passphrase "DUEDILIGENCE" and in picture3 we will get a file flag.txt and we will use 'cat to read it and get the answer.

### Flag
>picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
### Resources used
[Wireshark wikipedia](https://en.wikipedia.org/wiki/Wireshark), Steghide manual page to understand the usage of this tool.
