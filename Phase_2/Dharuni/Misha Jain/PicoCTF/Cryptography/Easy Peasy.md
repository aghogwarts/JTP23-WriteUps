<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - Easy Peasy Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup provides a step-by-step guide for solving the "Easy Peasy" challenge in PicoCTF. The challenge provides a Python script (otp.py) and a server to connect to (nc mercury.picoctf.net 64260). The goal is to recover the flag from the OTP encryption.

<b>Author:</b> Misha Jain

<b>Date:</b> December 15, 2023

<b>Tools Used:</b><br>
- Python
- Netcat

<b>Challenge Description:</b><br>
In the "Easy Peasy" challenge, participants are tasked with recovering the flag from a one-time pad encryption. The challenge involves connecting to a remote server and interacting with an OTP (One-Time Pad) encryption script.

<b>Exploitation:</b><br>
1. Use netcat to connect to the provided server.<br>

<p align = 'center'>

nc mercury.picoctf.net 64260

</p><br>

<p align = 'center'>

![](<Pictures/Easy Peasy - Encrypted_Flag.png>)

</p><br>

<p align = 'center'>

![](<Pictures/Easy Peasy - Encrypted_Text.png>)

</p><br>

2. Review the otp.py script to understand how the encryption is performed. Take note of the key generation and encryption process.<br>

<p align = 'center'>

![](<Pictures/Easy Peasy - Source_Code.png>)

</p><br>

3. Since OTP is theoretically unbreakable, the vulnerability likely lies in the key generation or usage. Explore potential weaknesses in the key generation or any reuse of the key. For OTP to be unbreakable, the key must not be repeated. However, in this code, we can see that the key is being repeated once the key length of 50000 is reached. Hence, using the python code below, we can exploit this vulnerability. The flag is picoCTF{3a16944dad432717ccc3945d3d96421a}<br>

<p align = 'center'>

![](<Pictures/Easy Peasy - Decryption.png>)

</p><br>

<b>Conclusion:</b><br>
The "Easy Peasy" challenge demonstrates the importance of understanding the limitations and vulnerabilities of encryption schemes. It provides hands-on experience in breaking a supposedly unbreakable encryption method.

</font>