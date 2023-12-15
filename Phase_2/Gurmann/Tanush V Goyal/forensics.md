## macrohard_weakedge


In programming, a macro is a fragment of code which has been given a name. This name, represented by an identifier, is replaced by the code it represents before the program is compiled. Even though it can make the code more readable it also poses security threats.

After going through the ppt and finding nothing, i searched the web aand got to know that sometimes these files can be zipped. By using the unzip command of linux i was able to get the contents of the file which also contained the hidden file.

<img width="692" alt="Screenshot 2023-11-14 at 1 25 25 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/77ce6c3e-139f-4653-9725-167ddbbdb84c">

<img width="692" alt="Screenshot 2023-11-14 at 1 35 37 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/3f791489-445e-4445-bb0c-33d131568e18">

After entering through the directories and reading the file i found a text which seems to be base64 encoded. After decoding it i found the flag.

## transferftp

First we install wireshark which is an open-source software which helps to capture the data travelling back and forth to the network. We then export the data as tftp on our computers. The following files are exported. 
<img width="758" alt="Screenshot 2023-11-14 at 11 48 02 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/7d1bf6e5-be4f-4466-9cb3-2c4bb26a65df">

We then use the ls command to list these files in terminal and to read them we use the cat command.
<img width="559" alt="Screenshot 2023-11-14 at 11 47 44 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/c4917b30-cf23-4c31-8b0f-2a143b72c111">

These files look to be encoded by rot13. After passing through a decoder online the plan file prints out the following message:

<img width="487" alt="Screenshot 2023-11-14 at 11 49 49 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/9ea4fd2d-ecdf-4f62-8c41-c098a1df0bf7">

I have also read that data in images can be concealed by steganography. I then opened an online steganography decoder and started to pass the images one-by-one using DUEDILIGENCE as the password. Image 3 hid the flag.
<img width="487" alt="Screenshot 2023-11-14 at 11 52 25 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/8c267005-7315-42b9-a37a-7542ac4e59ae">
<img width="487" alt="Screenshot 2023-11-14 at 11 52 17 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/02faf048-1dba-4566-a3f3-eca5da208cb2">

## tunnelvision

The file which we downloaded is a bmp file. I first tried opening the file using a bmp file opener however it was showing an error. On opening the hexdump of the file and comparing it to a normal bmp file its header had a BAD component due to which it could not open. After replacing it with standard values the file opened.
 
 <img width="487" alt="Screenshot 2023-11-14 at 11 01 39 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/9c9241ed-da69-409c-97eb-940a88b5cf6a">

 <img width="1137" alt="Screenshot 2023-11-14 at 11 02 41 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/c4a42c52-2594-4e54-a9be-d77c047055d3">

However the full file wasnt being displayed. After checking for the width and height of the file, the height of the file could still be increased. On putting a height of 850 by converting it to hex and opening it we find the flag.

<img width="374" alt="Screenshot 2023-11-14 at 11 02 56 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/6824d2e5-277d-477d-b92c-84c41c49f831">


<img width="374" alt="Screenshot 2023-11-14 at 11 03 17 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/7a07b1b0-6d6d-4dff-9096-91549467bb83">


<img width="910" alt="Screenshot 2023-11-14 at 11 02 10 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/3db078f9-1c06-432b-9c5b-83711ed13d9f">
