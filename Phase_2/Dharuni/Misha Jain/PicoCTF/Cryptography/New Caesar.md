<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - New Caesar Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup provides a step-by-step guide for solving the "New Caesar" challenge in PicoCTF. The New Caesar challenge involves decrypting a given ciphertext that has been encrypted using a modified Caesar cipher. Participants need to analyze the encryption method and determine the shift value to recover the original message.

<b>Author:</b> Misha Jain

<b>Date:</b> November 15, 2023

<b>Tools Used:</b><br>
- Text Editor

<b>Challenge Description:</b><br>
In the New Caesar challenge, participants are provided with a ciphertext that has been encrypted using a modified Caesar cipher. The goal is to identify the shift value used in the encryption and decrypt the message to find the flag.

<b>Exploitation:</b><br>
1. Upon analyzing the code, we see that the cipher takes place in two parts. One b16_encoder, and one shift.<br>

<p align = 'center'>

![](<Pictures/New Caesar - Source_Code.png>)

</p><br>

2. Create a program to reverse both these functions.<br>

<p align = 'center'>

![](<Pictures/New Caesar - Decoder.png>)

</p><br>

3. From the list of flags, choose the most appropriate one.<br>

<p align = 'center'>

![](<Pictures/New Caesar - Flags.png>)

</p><br>

<b>Conclusion:</b><br>
The New Caesar challenge provides an opportunity to practice analyzing and decrypting messages encrypted with modified Caesar ciphers. It reinforces the importance of understanding classic cryptographic algorithms.

</font>