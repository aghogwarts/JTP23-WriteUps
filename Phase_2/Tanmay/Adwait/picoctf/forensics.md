# tunn3l v1s10n

## problem
we are given a file and been told to recover it 
## hint
Weird that it won't display right...

## solution
The first thing that i notice abt why cantr we open the file is that it dosent have a extension, so i tried to find out its type.
using terminal commands i couldnt find much so i researched abt how to find the type of a file , and i found out that the first two letters of the file head(first few lines of the file), guves us the type of file in our case BM which stands fir bitmap file.

![Screenshot from 2023-11-14 19-39-59](https://github.com/adwait3/pico/assets/148553626/96754839-0179-447a-9525-48b23f8f324c)

so i tried to add the extension to the file and open it but that didnt work and i was still unable to open the file.
so i searched abt how to open bmp files and found an application called imagemagik so i decided to give it a try and sure enough it worked and i got a image but it still said not a flag.

![Screenshot from 2023-11-14 20-41-42](https://github.com/adwait3/pico/assets/148553626/bfcba0cc-dba1-47a7-b30a-a314334d1802)

after going through what a non corrupted bitmap looks like in a hex editor i realised in the very beggning it said BAD i figured this was the corrupt part.

![Screenshot from 2023-11-14 20-51-50](https://github.com/adwait3/pico/assets/148553626/8e596238-7bb5-4336-a1da-e08a54a57708)

so after comparing it to a normal bmp image and changing the values to
  ![Screenshot from 2023-11-14 22-54-36](https://github.com/adwait3/pico/assets/148553626/36717a8c-40e3-49c6-9090-669789037eaf)
i am able to open the image normally without imagemagic but still not able to view the whole image.

to view the full image i then search where the boundaries of the image are in the hexeditor and find the maximum range for bmp images and change it 
![Screenshot from 2023-11-14 22-59-30](https://github.com/adwait3/pico/assets/148553626/77aff871-468b-4697-9f5d-cf4b2cd3ad82)
and sure enough after this im able to open the full image normally and get the flag
![Screenshot from 2023-11-14 23-00-46](https://github.com/adwait3/pico/assets/148553626/7a0779a6-6bdb-4c94-a561-fab4807bf889)

## flag
picoCTF{qu1t3_a_v13w_2020}

# Trivial Flag Transfer Protocol

## problem
Figure out how they moved the flag.
and we are given a .pcapng file
hint
* What are some other ways to hide data?

## solution
i searched abt pcapng files and found that they can be opened through wireshark so i went ahead and downloaded wireshark.
after opening the file in wireshark i found
![Screenshot from 2023-11-15 18-32-58](https://github.com/adwait3/pico/assets/148553626/33d64fb9-fd0f-4eb3-a145-3346c4aac2bf)
i learned that tftp stants for trivial file transfer protocol and saw a lot of tftp files with data packets in them after going around wireshark i found out we can export these files to them
![Screenshot from 2023-11-15 18-32-15](https://github.com/adwait3/pico/assets/148553626/4db63a34-d751-4a00-9a0d-3646cf2de1af)
out of these files picture 3 seemed a little off since it was way bigger in size than the rest
i openened the first file instructions.txt 
![Screenshot from 2023-11-15 18-38-04](https://github.com/adwait3/pico/assets/148553626/154bc06a-5c0d-443a-8baa-645370aec056)

and found gibberish figured it was encypted but since it was only letters and we didnt have any clue abt a key i tried the possible encryptions using cyberchef and found it to be ROT 13
![Screenshot from 2023-11-15 18-40-29](https://github.com/adwait3/pico/assets/148553626/ad0ae05a-aa65-49fa-b7e3-89da89b8b269)
this says
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

i coudldnt figuire this out so i opened the other file plan it had the same rot 13 encryption
![Screenshot from 2023-11-15 18-43-43](https://github.com/adwait3/pico/assets/148553626/85f89c4e-651d-429c-a96f-958e5d1333db)
this says
I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE. CHECK OUT THE PHOTOS
it says used the program and hid it in photos. so i opened our program file. and started looking at the files inside for clues and found teh control file 
![Screenshot from 2023-11-15 18-47-22](https://github.com/adwait3/pico/assets/148553626/24a9ea7e-6d93-4c49-adeb-a8c66eda3266)
this seemed like a major clue reading further i found this in the amn file
![Screenshot from 2023-11-15 18-55-41](https://github.com/adwait3/pico/assets/148553626/b790f761-bc95-4a53-ae7d-1547f6216451)
so i tried installing the program as it can help me get the flag from the images but i was unable to install the file
![Screenshot from 2023-11-15 18-58-06](https://github.com/adwait3/pico/assets/148553626/252a40ab-2db0-4faa-af07-2901247f389a)
so i installed the steghide software through terminal.
after installing and trying it out it asked for passphrase 
![Screenshot from 2023-11-15 19-03-15](https://github.com/adwait3/pico/assets/148553626/c35f5da5-3e21-446a-b9d4-fe26821f5634)
i looked through instrusctions and plan again for some clues and tried a lot of passwords and finally DUEDILIGENCE worked
![Screenshot from 2023-11-15 19-06-09](https://github.com/adwait3/pico/assets/148553626/3ec74a34-ece2-4d92-bae8-4bc9cc69ef7f)
this made me sure abt the text file in picture so i extracted it 
![Screenshot from 2023-11-15 19-12-07](https://github.com/adwait3/pico/assets/148553626/d4423020-0a46-4b11-b65f-efd5a1296332)
anf got the falg
## flag
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}


# MacroHard WeakEdge
## problem
I've hidden a flag in this file. Can you find it? Forensics is fun.pptm

## solution
after opening th eppt i found a 58 slides long blank ppt ppt reminded me of the challenge in scavenger hunt with a slide and planets so i decided to try binwalk and found a lot of zip files in the ppt
![Screenshot from 2023-11-15 19-26-04](https://github.com/adwait3/pico/assets/148553626/27a29d2e-ef79-460f-bd54-1a12a2cd3427)
after extracting i found most of them were xml files i searched more and found a bin file so i cat it but foud no flag written so figured this is not the file im looking for
![Screenshot from 2023-11-15 19-34-02](https://github.com/adwait3/pico/assets/148553626/3d492157-7d5c-495c-a8c0-9b1efb0e55bc)
after searching for more files a found hidden file after catting it i found some text
![Screenshot from 2023-11-15 19-37-04](https://github.com/adwait3/pico/assets/148553626/754421e0-ca38-418d-8f36-7d62225bcc41)

this seemed gibberish so i tried encryptiong it it was only letters so i thought it would be rot encryption but none worked so i tried the most common encryptions and using trial and error found it to be base 64
![Screenshot from 2023-11-15 19-40-58](https://github.com/adwait3/pico/assets/148553626/b4dfdb7b-4ab0-4869-aad9-004a13886be6)
 which gave me the flag

 ## flag
 picoCTF{D1d_u_kn0w_ppts_r_z1p5}

