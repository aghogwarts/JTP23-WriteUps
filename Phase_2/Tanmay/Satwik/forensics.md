#### tunn3l_v1s10n

I downloaded the file and ran it on my linux machine
![Screenshot from 2023-11-04 11-23-30](https://github.com/s4twik/picoctf/assets/147993943/0b0af434-00ef-47e1-8bcf-bd61874041e7)
I didn't knew what header file was so i googled it and found out it's the first line of the hex file of the bmp file
so to run the bmp file i had to edit the header file, so i googled what the header file of the bmp file should look like
and accordingly the changes in offset `0A` and `0E` i didn't understand what to do in `0A` so i put it as 0 and `0E` to 40 in hex for which is 0028
![Uploading Screenshot from 2023-11-04 18-58-57.png…]()

i ran the file it worked but i didn't get the password
![Screenshot from 2023-11-04 19-05-49](https://github.com/s4twik/picoctf/assets/147993943/d2382b44-ad96-4d30-8522-3b21204629d3)
i coldn't figure out the problem, then it clicked that the aspect ratio is a bit off
so i googled what offset are meant for the aspect ratio of the file 
i kept changing the height little by little and after a few attempts i got the flag
![Screenshot from 2023-11-04 19-09-32](https://github.com/s4twik/picoctf/assets/147993943/b1ae2f42-53fd-4ecf-b8f8-ee39caca9c4d)
![Screenshot from 2023-11-04 19-09-57](https://github.com/s4twik/picoctf/assets/147993943/09c88b03-0d2a-4d5a-9ad9-245bb005bff9)
![Screenshot from 2023-11-04 18-21-41](https://github.com/s4twik/picoctf/assets/147993943/5ff0aa80-118c-4c22-a224-a880e92b6ae8)

#### Typical Flag Transfer Protocol
Started by downloading the file, saw it was a pcapng file
I had no clue what that is so i googled what that is, read a bit about. Didn't understand anything
so I googled how to run it, it gave me a software called `Wireshark`. Downloaded it via terminal following : https://www.geeksforgeeks.org/how-to-install-and-use-wireshark-on-ubuntu-linux/
uploaded the file

![image](https://github.com/s4twik/picoctf/assets/147993943/ba040d0d-1950-43a2-827c-db338ad8393e)
I see something called `TFTP Protocol` and reaslised it was the name of the file i just ran. I take it as a clue and google `TFTP Protocol`
it's a file transfer function which doesn't require authentication.
I export all the Networks w/tftp protocol to a folder
i get a 3 bmp files and 2 text files. I go through one of the file. It's Encryted so i run it through dcode.fr
it was encrypted in ROT13 format
![Screenshot from 2023-11-07 17-44-33](https://github.com/s4twik/picoctf/assets/147993943/eb5505b7-b4d8-4a1c-8b27-67e5853563bb)
a/to it should go to plans.txt
![image](https://github.com/s4twik/picoctf/assets/147993943/5aafe5ac-18b6-4be1-a678-2ec0cc9c002d)
check out the photos!!??
didn't make alot of sense so i went to other files which i extracted from deb
![image](https://github.com/s4twik/picoctf/assets/147993943/cb870c68-9308-46e2-91ee-179566f27424)
`steghide`
i read about it. so i have to use it on terminal to extract those bmp file
which i do.
![Screenshot from 2023-11-07 16-36-54](https://github.com/s4twik/picoctf/assets/147993943/0b97e3ff-9174-4ca3-a365-2eec9c9ed7cd)

DONE!

![Screenshot from 2023-11-07 16-38-57](https://github.com/s4twik/picoctf/assets/147993943/aa18f49c-efb2-4a0f-8e91-7d1211e63dfe)

#### Macrohard Weakedge
the best approach to finding files hidden inside other files is binwalk
if we perform binwalk "Forensics is fun.pptm" we'll see there's a bunch of .zip files. we can extract it using binwalk -e "Forensics is fun.pptm"

Now there's _Forensics is fun.pptm.extracted folder which I will navigate using 7zip.

Since there's too many things in 0.zip I decided I might as well automate the search process. I extracted 0.zip then navigated to it in the terminal.

![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/944324da-3ba9-4f26-8704-26263e66cfa1)
i see this file at the end of the list of files
i cat it
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/d46f677f-7884-47e0-89f0-16c65d5b8438)
it seems like an encryption 
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/90037681-fa7d-4a1f-b04d-54f0dcb030b8)
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/3702639d-62fc-4eea-bcd2-8faa99e4ff63)
