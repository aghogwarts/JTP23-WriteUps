# MacroHard WeakEdge
## GOAL
I've hidden a flag in this file. Can you find it? Forensics is fun.pptm
## WRITE UP
If we download the file and open it, we get a powerpoint presentation which is empty. After searching in google for comands which help in finding hidden files inside a file, I found it is `$ binwalk` and to extract the files we do `$ binwalk -e filename `

Now we go to the terminal and dive into the directory which consists of the given file and run binwalk command.

`$ binwalk 'Forensics is fun.pptm'`

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/767f0585-16fb-4d3a-bcb5-6dd1778605d4)

Now we have found the hidden file, thus we have to extract these files.

`$ binwalk -e 'Forensics is fun.pptm'`  e -stands for extraction.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/a6342cad-57b6-4c26-8fdb-30eca1564586)


Now it shows the file forensics is fun as a directory.

Now we can dive intoit using the cd command and run the cat command.

We get a string of characters which is in base 64 format. We can use this site to convert [base 64](https://www.base64decode.org/) to ascii.

We get the flag.

FLAG:- picoCTF{D1d_u_kn0w_ppts_r_z1p5}

____

# Trivial Flag Transfer Protocol
## GOAL
Figure out how they moved the flag.
## HINTS
What are some other ways to hide data?
## WRITE UP
If we download the given file we get a pcapng file.
```NOTE:- to read pcapng there is a program that can be used named as wireshark.If wireshark is not present install it.```
It can be downloaded by using the command `$ sudo apt install wireshark`
We then go to wireshark and open the file given.we will get an ouptut similar to the image given below.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/168dff11-f65a-4bb7-a79a-f94fb207b5cc)

As the name of the challenge states we only need the TFTP files.

So we use the export objects option in the file menu to export the TFTP.

We get the following 5 files.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/a21c3ae7-a9b6-4814-92b6-0c80e008e85e)

If we open the `instructions.txt` we find a string of text that doesnot make any sense, thus we have to decrypt it into readable form, I figured out that the possible forms of decryption are substitution, caesar, or rot13.

Trying each of them will finally give meaningful sentence for rot13.

### Instructions.txt and plan

Before :`GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA`

After  : `TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`

After proper punctuation we get 
> TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

Similarly for plan we get

> I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE.CHECKOUTTHEPHOTOS

It asks me to check out the photos and open the program file.

### program.dep

Running the file command for program.dep file we get
`$ file program.dep`

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/2b7be81d-4fbf-45ab-891d-78f44c47c459)

It says debian binary package.

If we open the file we find

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/b93c4585-adee-423d-ab69-7b3e4da989cc)

If we explore all the files in these folders. we notice there is a README.txt file which guides us what to do and we also notice that the word steghide is repeated many times.

Reading the README file we get to know how to extract the files.

>Note:- Steghide is a steganography program that is able to hide data in various kinds
of image- and audio-files. The color- respectivly sample-frequencies are not
changed thus making the embedding resistant against first-order statistical
tests.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/f4196cd5-d97f-4bfc-aaf0-21dcea23600c)

By running that command with every picture.bmp file With the passcode `DUEDILIGENCE` 

>NOTE:- it was mentioned in the plan file that the files were hidden with DUEDILIGENCE

we Find the `flag.txt` file in picture3.bmp

> NOTE:- we must be in the directory where all these files are save to perform these actions.

Now we use the command `$ cat flag.txt `

FLAG : picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

___


# Tunnel vision
## Goal
We found this file. Recover the flag.
## write up
When we try to open the file given we get the following output.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/a748a970-f2e8-4f3b-87b3-35991a2a7ee0)

This lets us know that the given file is corrupted and is a bitmap file with corrupted header.

Now change the extension of the file as `.bmp`

To know whats the mistake in the header we can take sample files from the internet.

We can download them from this [site](https://filesamples.com/formats/bmp)

Open the smaple file and the given file simultanoeusly in [hexed.it](https://hexed.it/)

Now by comparing the headers and changing the corrupted parts and saving it, we can now open the file to get the following output.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/27737d45-a17b-4ef9-b395-8b2cb7d36c46)

Now we save it and open the file once again.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/ec342bf5-582e-44aa-a5d2-529daf4176b3)

The image we get is actually cropped. so we need to change the height/ pixels of the image.

``` formula for no of pixels = (no.of bytes * 8)/bit depth```
We can know these properties by running the exiftool command in tthe terminal for this file.

NOTE: if the command doesnot exist for the computer we can install it by using `sudo apt install exiftool`

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/741109a1-2f2a-48d5-af80-fc3a63af545b)

Now, if we check the number of pixels using the formula, it must be `964466` bytes. But it is only `1134*306 =347004` pixels.

If we examine the image we can understand that the image height is cropped up.

Thus we have to change the image height. 

 ``` 964466/ 1134 = 850.499 ~ 850```

 Now to change the cell which maps to the image height we first convert 850 to hex.
 Which is `0x352`

 ![image](https://github.com/vishwatejD/picoCTF/assets/141154035/f9f44dcb-6bfe-4f4f-bb6e-d9b7edfd4cd1)

 we now save the file and open it . we get the full image and the flag.
 
![image](https://github.com/vishwatejD/picoCTF/assets/141154035/762d72a2-d8ff-4e85-a479-4c9b18ce1461)
