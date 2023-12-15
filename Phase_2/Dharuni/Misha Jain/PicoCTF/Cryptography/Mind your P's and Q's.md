<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - Mind your P's and Q's Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup provides a step-by-step guide for solving the "Mind your P's and Q's" challenge in PicoCTF. The challenge provides the following RSA-related values:

- N (modulus)
- e (public exponent)
- Ciphertext

The goal is to decrypt the ciphertext and reveal the plaintext message.

<b>Author:</b> Misha Jain

<b>Date:</b> December 15, 2023

<b>Tools Used:</b><br>
- Python
- Online Factorization Calculator

<b>Challenge Description:</b><br>
In the "Mind your P's and Q's" challenge, we are given values related to an RSA encryption: N, e, and the ciphertext. The task is to decrypt the given ciphertext using the provided values.

<b>Exploitation:</b><br>
1. We are given the values of c, n and e in the text file.<br>

<p align = 'center'>

![](<Pictures/Mind your P's and Q's - Values.png>)

</p><br>

2. We know that n is a product of two prime numbers, p and q. Hence, we can use an online factorization calculator to find the values of p and q.<br>

<p align = 'center'>

![](<Pictures/Mind your P's and Q's - P_and_Q.png>)

</p><br>

3. Using the following Python script, we can get the flag, which is 'picoCTF{sma11_N_n0_g0od_05012767}'. <br>

<p align = 'center'>

![](<Pictures/Mind your P's and Q's - Python_Script.png>)

</p><br>

<b>Conclusion:</b><br>
The "Mind your P's and Q's" challenge explores the potential vulnerabilities associated with small RSA values. It reinforces the significance of using secure parameters in RSA key generation.

</font>