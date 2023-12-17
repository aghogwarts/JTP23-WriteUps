# Trivial Flag Transfer Protocol
We get a file tftp.pcapng, tftp is trivial file transfer protocol which is an inferior version to ftp, to analyse the pcapng file we use wireshark, we can observe that a file transfer is taking place, we can export these tftp files using wireshark.

We get 5 files, including 3 bitmap images, 1 text file and a deb file, analysing the deb file we find that its beng used to install a program steghide which is probably being used to hide the flag,

Then we see that the instructions and plan has some encrypted data, by using a cipher identifier, its found to be a rot13 shift cipher,

```
Information.txt file
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

Rot13:
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN



Plan file
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF

Rot13:
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

So the creator used the program the to hide the flag into one of the photos, and used the passphrase 'DUEDILIGENCE',

Now we need to extract steghide on all the images

```
nayanko@Ayan:~/Desktop/TRIVIAL FTP$ sudo apt install steghide
Reading package lists... Done
Building dependency tree... Done
...
all that installation stuff i removed from here
...
Processing triggers for libc-bin (2.35-0ubuntu3.5) ...
nayanko@Ayan:~/Desktop/TRIVIAL FTP$ steghide extract -sf picture1.bmp 
Enter passphrase:                                                
steghide: could not extract any data with that passphrase!
nayanko@Ayan:~/Desktop/TRIVIAL FTP$ steghide extract -sf picture2.bmp 
Enter passphrase: 
steghide: could not extract any data with that passphrase!
nayanko@Ayan:~/Desktop/TRIVIAL FTP$ steghide extract -sf picture3.bmp 
Enter passphrase: 
wrote extracted data to "flag.txt".
nayanko@Ayan:~/Desktop/TRIVIAL FTP$ ls
flag.txt  instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb  tftp.pcapng
nayanko@Ayan:~/Desktop/TRIVIAL FTP$ cat flag.txt
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```

So i first installed steghide and then extracted using it from all pictures to get the flag from picture 3 i.e. " picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919} "

