<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - Local Authority Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup explains the process of solving the "Local Authority" challenge in PicoCTF. The Local Authority challenge involves exploiting a web application that has a local file inclusion vulnerability. The goal is to leverage this vulnerability to read sensitive files and retrieve the flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 14, 2023

<b>Tools Used:</b><br>
- Web Browser (Firefox)

<b>Challenge Description:</b><br>
Local Authority is a web exploitation challenge that requires participants to identify and exploit a local file inclusion (LFI) vulnerability in a web application. By manipulating input parameters, participants can read sensitive files and retrieve the flag.

<b>Exploitation:</b><br>
1. Visit the provided URL for the Local Authority challenge and explore the functionality of the web application.<br>

<p align = 'center'>

![](<Pictures/Local Authority - Exploring_Domain.png>)

</p><br>

2. After reaching the "http://saturn.picoctf.net:59126/login.php" URL, view the page's source code. Here, we can see a locally included file, "secure.js", which tells us our required username and password.

<p align = 'center'>

![](<Pictures/Local Authority - SecureJS.png>)

</p>

3. We retrieve the flag after using username = "admin" and password = "strongPassword098765".

<p align = 'center'>

![](<Pictures/Local Authority - Flag.png>)

</p>

<b>Conclusion:</b><br>
The Local Authority challenge provides hands-on experience in identifying and exploiting local file inclusion vulnerabilities. It highlights the importance of input validation to prevent such security risks in web applications.

</font>