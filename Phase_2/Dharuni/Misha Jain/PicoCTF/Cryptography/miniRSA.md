<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - miniRSA Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup provides a step-by-step guide for solving the "miniRSA" challenge in PicoCTF. The challenge provides a ciphertext encrypted using RSA. The hint suggests that the key size might be small, indicating a potential vulnerability.

<b>Author:</b> Misha Jain

<b>Date:</b> November 15, 2023

<b>Tools Used:</b><br>
- Online Converter Tools

<b>Challenge Description:</b><br>
In the miniRSA challenge, we are given a ciphertext and are tasked with decrypting it. The challenge hints that "something seems a bit small," suggesting that the key size used for encryption might be small.

<b>Exploitation:</b><br>
1. Inspect the provided ciphertext and take note of its length. In an RSA algorithm, the ciphertext, c, is equal to m^e % N. However, in this case, we can see that the value of m ** e may just be smaller than N. Hence we can write c = m ** e.<br>

<p align = 'center'>

![](<Pictures/miniRSA - Text_File.png>)

</p><br>

2. We can find m by finding the cube root of c using an online cube root calculator to prevent loss of precision.<br>

<p align = 'center'>

![](<Pictures/miniRSA - Cube_Root.png>)

</p><br>

3. Converting the decimal number to hexadecimal, and then converting the hexadecimal number to ASCII, we get the flag.<br>

<p align = 'center'>

![](<Pictures/miniRSA - Flag.png>)

</p><br>

<b>Conclusion:</b><br>
The miniRSA challenge highlights the importance of using an adequate key size in RSA encryption. It provides hands-on experience in factorizing moduli and decrypting RSA-encrypted messages.

</font>