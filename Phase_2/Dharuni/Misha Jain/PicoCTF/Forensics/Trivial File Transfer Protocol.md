<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - Trivial File Transfer Protocol Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup guides you through the process of solving the "Trivial File Transfer Protocol" challenge in PicoCTF. The Trivial File Transfer Protocol (TFTP) challenge involves analyzing network traffic to uncover a transferred file. Participants are tasked with identifying the transferred file's content and extracting the flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 15, 2023

<b>Tools Used:</b><br>
- WireShark
- Terminal

<b>Challenge Description:</b><br>
In the TFTP challenge, participants need to analyze a packet capture containing TFTP traffic. The goal is to extract the transferred file and discover any hidden information or flags within the file.

<b>Exploitation:</b><br>
1. Begin by downloading the file and opening using wireshark. We can see some TFTP traffic using this. We will extract these TFTP files to a local folder.<br>

<p align = 'center'>

![](<Pictures/Trivial File Transfer Protocol - TFTP_Traffic.png>)

</p><br>

2. 6 files have been extracted to our folder. Out of these, 2 are .txt files, 3 are .bmp files, and 1 is a .deb file.<br>

<p align = 'center'>

![](<Pictures/Trivial File Transfer Protocol - Extracted_Files.png>)

</p><br>

3. Looking through instructions.txt, we can put the text into an online cipher identifier. This shows that the text is encrypted in a ROT-13 cipher. So is the 'plan' file.<br>

<p align = 'center'>

![](<Pictures/Trivial File Transfer Protocol - ROT13.png>)

</p><br>

4. Looking through the .deb file, we can see that the user has encrypted the flag using steghide. The plan file tells us that the flag is hidden in one of the images using the password 'DUEDILIGENCE'. Using the following command on all three images, we can find the flag file.<br>

<p align = 'center'>steghide extract -sf picture1.bmp</p><br>

<p align = 'center'>

![](<Pictures/Trivial File Transfer Protocol - Steghide.png>)

</p><br>

5. Cat-ing the contents of the new flag.txt file, we can acquire the flag.

<p align = 'center'>cat flag.txt</p>

![](<Pictures/Trivial File Transfer Protocol - Flag.png>)

<b>Conclusion:</b><br>
The TFTP challenge provides hands-on experience in analyzing network traffic and extracting files transferred using TFTP. It reinforces the importance of using packet capture analysis tools like Wireshark for forensic tasks.

</font>