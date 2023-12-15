## Challenge: tunn3l v1s10n  
Download the given file via webshell.  
Checked its file format -> data  
tried cat and got disconnected from the webshell.  
I tried using different variations of the grep command but nothing worked.  
I looked up a writeup to understand what exactly to do since i could not even think of an approach to begin with.  
I referred 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/tunn3l%20v1s10n/tunn3l%20v1s10n.md'  
Shifted to virtual machine to use hex editors.  
While i was downloading the GNOME Hex Editor, i tried to opent he tunn3lv1s10on file with the default image viewer and got the prompt saying the "bmp image had unsupported header size". This gave me 2 important details.  
1. The file is BMP format.
2. There is something wrong with the header.  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/4ee64442-dcf3-45dd-b6d8-134a57883726)  
I reffered the blog shared in the writeup about BMP format 'http://www.novell.com/documentation/ndsv8/usnds/c1help/novell_common/hexeditor.html' & 'https://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm'  
Given the clue, i focused on header and infoheader categories.  
I opened the file with photopea.com  
As expected it says not a flag and is oddly stretched out.  
The width of the bitmap is at offset 0x12 and height is at 0x16. I gave height the same values as that of width, i.e. 6E 04 and saved it.  
![Screenshot 2023-11-14 202630](https://github.com/Azure9733/picoCTF/assets/143328010/cea2f81d-6a2d-4fad-8923-6429691baf07)
![Screenshot 2023-11-14 202944](https://github.com/Azure9733/picoCTF/assets/143328010/fab30c07-219f-46f6-a470-43ead9bccd68)  
Opening it on photopea gave me the correct flag.  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/33966840-2ee8-4b2c-9fcf-8ee48c160b7b)  
picoCTF{qu1t3_a_v13w_2020}
## Challenge Trivial FTP  
The given file is a network packet capture so i opened it with wireshark.  
filtered ARP(Address Resolution Protocol) messages by !arp  
I went through the packets to find any odd patterns but it was more or less just data request and acknowledgements.  
I couldnt figure out what to do so i tried to take a look at a writeup to see their approach. I referred 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/Trivial%20Flag%20Transfer%20Protocol/Trivial%20Flag%20Transfer%20Protocol.md' and right away i could tell i did not know anything to be able to solve this one so i learned as i followed along.  
I exported the TFTP files into a folder and opened the intructions file up.  
Used 'https://www.dcode.fr/cipher-identifier' to identify the encryption format as i am not used to encrypted data yet.  
It is Rot13. After decyphering it, the instructions read "TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN" (without the spaces).  
Opened the plan.txt file and decrypted it form Rot13 format. Read "I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS" (without spaces).  
Extracting the Program.deb file gave 3 more files out of which 2 zip files were of particular interest. Extracting 'Control.zip' let to a file called control which was describing a package called 'steghide'.  
So i sudo apt installed steghide.  
Inside the 'data' folder usr/share/doc/steghide there is a readme file zipped. That told me everything about steghide along with how to use it.  
Installed libraries libmhash, libmcrypt, libjpeg and zlib as instructed.  
Then i ran steghide --info picture1.bmp. As for the passphrase i used DUEDILIGENCE as mentioned in 'plan.txt'.  
It did not work. Tried picture 2 and 3. And it worked on picture3:  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/b4d8439f-c69c-42df-9fbd-98cd9d5ddd85)  
Then i used steghide extract -sf picture3.bmp and the flag.txt file was saved in the working directory.  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/c712d8b6-e453-4b81-8e8b-bda32d67de65)  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/0235fa57-2d98-4248-a2f7-76512446d0c4)  
## Challenge Macrohard Weakedge  
The file is a Macro PPT. Opening it gives blank slides.  
I find the name quite revealing. Macro is hard but Edge is weak. There must be a meaning behind that.  
After looking up online, i couldnt find any meaning behind that :(  
I ended up referring a writeup for this as well 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/MacroHard%20WeakEdge/MacroHard%20WeakEdge.md'  
Installed binwalk and checked the ppt file via binwalk.  
I find alot of zip files. Using binwalk -e 'Forensics is fun.pptm', i extract the files.  
Here i was totally relying on the writeup and focused more on trying to understand what was the approach.  
Extracting the 0.zip file, the command  `find -D tree|grep hidden` was used. Using man find i found that we are finding via debug option tree which shows the expression tree in its original and optimised form.  
I wanted to know more about tree and ended up downloading the tree command library.  
Using that i was able to see a tree of all the files and folders in my working directory.  
I found hidden folder as well here:  
![Screenshot 2023-11-15 020304](https://github.com/Azure9733/picoCTF/assets/143328010/c603ae23-b211-4dae-bd8b-2cc089fcd2d1)  
I ended up finding a better way on my own!!  
Changing the directory towards the hidden file and opening it, i found a cyphered text:  
![image](https://github.com/Azure9733/picoCTF/assets/143328010/6631ce1c-67f5-4bc0-8e4b-67e10ac1ac33)  
Using the cypher identifier 'https://www.dcode.fr/cipher-identifier', it was found to be Base64.  
Decoding it gave the flag  
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}  
