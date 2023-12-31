# Reverse Engineering

Today we'll be learning on how to use the DOS operating system. It once used to be a dominant operting system and is somewhat similar to the Windows Command Prompt. Our goal for this task is to restore the **AC2023.BAK** file found in the root directory using the backup tool found in the **`C:\TOOLS\BACKUP`** directory. We'll navigate to this directory and run the command **`BUMASTER.EXE C:\AC2023.BAK`** to inspect the file.
On trying to run the backup  tool by **BUMASTER.EXE C:\AC2023.BAK**, it gave the error as shown below.

![Screenshot (87)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/500a7903-8012-43d9-af1b-6f7ba087237e)

So it seems that we're dealing with a file signature error problem. Here we learn about magic bytes or file signature which are specific byte sequences at the beginning of a file that identify or verify its content type and format. These bytes often have corresponding ASCII characters, allowing for easier human readability when inspected. The identification process helps software applications quickly determine whether a file is in a format they can handle, aiding operational functionality and security measures.The first two bytes refer to the file type.
As instructed by the error message, we'll open the **README.TXT** file.

![Screenshot (91)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/8987c4e9-9b4c-4fb6-826d-4af2d868e206)
![Screenshot (88)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/11e2db79-705d-422b-980e-bfacd19b52a8)

The troubleshooting section clears our problem. Now we can correct the backup file using the bits **41 43** which corresponds to **A C** in ASCII text.
So we can correct it by opening **`EDIT C:\AC2023.BAK`** and replacing the first two ASCII charactes **X X** to **A C** and save the file.
Now on trying to run the backup file again using the backup program as **BUMASTER.EXE C:\AC2023.BAK**, we get our flag for the challenge.

![Screenshot (89)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/51a5764d-fa4e-4b49-b6fc-4ee232a1992e)

## How large is the AC2023.BAK file

This can be done by going to the **`C:\TOOLS\BACKUP`** and write **`DIR C:\AC2023.BAK`** lists out the size of the BAK file
![Screenshot (90)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/9f29baf0-070e-4b5f-844b-46a3383eb086)
**Ans- `12,704`**

## What is the name of the backup program?
**Ans- `BackupMaster3000`**

## What should the correct bytes be in the backup's file signature to restore the backup properly?
**`Ans- 41 43`**

## What is the flag after restoring the backup successfully?
**`Ans- THM{0LD_5CH00L_C00L_d00D}`**
