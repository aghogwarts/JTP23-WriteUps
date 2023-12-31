# Disk Analysis

We'll try answering question from the USB flash drive using FTK Imager tool. We'll export the deleted files if required but the tool already has a file previewer built in so that helps.

## What is the malware C2 server?

So we can find a secrets.txt text file in the deleted **DO NOT OPEN** file. We can read through the texts to get malware C2 server.

![Screenshot (5)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/3c8e3b6d-0c88-40cb-aec1-fc9efbb0e500)

**Ans- `mcgreedysecretc2.thm`**

##  What is the file inside the deleted zip archive?

This is pretty straight forward. There's **JuicyTomaTOY.zip** file in the **DO NOT OPEN** file where inside it is the **JuicyTomaTOY.exe** executable file which is our required anwer.

![Screenshot (6)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/3fc3aaa2-044f-4336-8dfe-d3d505d30df7)

**Ans- `JuicyTomaTOY.exe`**

## What flag is hidden in one of the deleted PNG files?

We can go through the two png image files in the and look for the flag by searching for **THM** part of the flag using **Ctrl+f** while view the image in hex mode. We find the flag in the **portrait.png** file.



**Ans- `THM{byt3-L3vel_@n4Lys15}`**

## What is the SHA1 hash of the physical drive and forensic image?

We can find the SHA1 has of the physical drive and forensic image by simply verifying the drive file. This detail was present in the challenge description.

![Screenshot (7)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/df9d292a-ba29-45a7-9877-accd02f3c5a9)

**Ans- `39f2dea6ffb43bf80d80f19d122076b3682773c2`**
