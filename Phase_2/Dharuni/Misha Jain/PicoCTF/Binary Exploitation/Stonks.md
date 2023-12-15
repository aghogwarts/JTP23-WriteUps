<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - Stonks Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup guides you through the process of solving the "Stonks" challenge in PicoCTF. The challenge falls under the Binary Exploitation category and requires analyzing a C file to find the flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 11, 2023

<b>Tools Used:</b><br>
- Terminal
- Text Editor
- CyberChef

<b>Challenge Description:</b><br>
The "Stonks" challenge in PicoCTF requires participants to exploit a binary executable. The goal is to identify and trigger a vulnerability in the binary to obtain the flag.

<b>Exploitation:</b><br>
1. Begin by running the binary to understand its behavior. Check if there are any obvious vulnerabilities. In this case, I checked for the string buffer overflow vulnerability.

<p align = 'center'>

![](<Pictures/Stonks - Basic_Vulnerabilities.png>)

</p><br>

2. Open the code in VSCode Text Editor to analyze for any vulnerabilities. Here, we find the potential vulnerability while entering the API token.

<p align = 'center'>

![](<Pictures/Stonks - API_Vulnerability.png>)

</p><br>

3. To check the data type of the user_buf pointer, we can enter "%p" as the API token. This shows the data type is a hexadecimal.

<p align = 'center'>

![](<Pictures/Stonks - Mod_p.png>)

</p><br>

4. We can enter a string of "%x" to find the API token of the creator.<br>

<p align = 'center'>

![](<Pictures/Stonks - Mod_x.png>)

</p><br>

5. Copying the given string of hexadecimal characters into an online converter.<br>

<p align = 'center'>

![](<Pictures/Stonks - Online_Converter.png>)

</p><br>

6. Cleaning up the hexadecimal string.<br>

<p align = 'center'>

![](<Pictures/Stonks - Cleaned_Up_String.png>)

</p><br>

7. Swapping endianness.<br>

<p align = 'center'>

![](<Pictures/Stonks - Swapping_Endianness.png>)

</p><br>

<b>Conclusion:</b><br>
The "Stonks" challenge in PicoCTF introduces participants to binary exploitation. By identifying and exploiting vulnerabilities in the binary executable, participants can gain insights into the fundamentals of software security.

</font>