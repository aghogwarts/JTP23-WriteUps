Since the name of the challenge hints at FTP, we can try opening the file in wireshark and analysing it

![tf1](https://github.com/poorvi1910/Cryptonite/assets/146640913/1f0a6363-5f5d-4b45-ae61-119054c748ff)

Opening instructions.txt we get the following cipher:
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

Using ROT13 on the cipher and adding space between words:
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER.FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

Doing the same for plan.txt :
I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE.CHECK OUT THE PHOTOS

On running the program.deb file, it opens up a package installer for steghide

Steghide is steganography program which hides bits of a data file in some of the least significant bits of another file in such a way that the existence of the data file is not visible and cannot be proven.
Steghide is designed to be portable and configurable and features hiding data in bmp, jpeg, wav and au files, blowfish encryption, MD5 hashing of passphrases to blowfish keys, and pseudo-random distribution of hidden bits in the container data.

Installing the package and running the command on the three images using ‘DUEDILIGENCE’, we get no output for first 2 images 

![tf2](https://github.com/poorvi1910/Cryptonite/assets/146640913/427c05db-ede6-4c7a-9b30-5d63b212bdee)

But the third image:

![tf3](https://github.com/poorvi1910/Cryptonite/assets/146640913/1df1ab51-8dbb-48cd-b49b-32ba099cf991)

Using cat command on the flag.txt file, we get the flag:
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
