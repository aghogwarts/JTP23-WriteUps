<font size = '4'>
<p align = 'center'>
<b>
Advent of Cyber - Day 3 Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup details the solution to Day 3 of the Advent of Cyber 2023 challenge titled "Feasibility of Brute Force." Detective Frost-eau and the team are faced with a lockdown of critical systems, including the IT room, and must resort to hacking to retrieve backup tapes. The challenge involves understanding password complexity, the number of possible combinations, and conducting a brute force attack using tools like Crunch and Hydra.

<b>Author:</b> Misha Jain

<b>Date:</b> December 3, 2023

<b>Tools Used:</b><br>
- Crunch
- Hydra
- AttackBox
- Web Browser

<b>Challenge Description:</b><br>
Day 3 focuses on the feasibility of brute force attacks by understanding password complexity and the number of possible combinations. The challenge involves generating a list of PIN codes using Crunch, a tool for creating password lists, and then using Hydra to perform a brute force attack on a PIN-protected door control system.

<b>Exploitation:</b><br>
1. Click on the "Start Machine" button for both the Target Machine and AttackBox. Once both machines are started, visit http://10.10.82.50:8000/ in the AttackBox’s web browser.<br<br>

2. Understand the number of possible PIN codes by considering a scenario where a three-digit PIN code is used. The total number of different PIN codes is 1,000 (000 to 999).<br><br>

3. Use Crunch to generate a list of all possible three-digit PIN codes using the command:<br><br><p align = 'center'>crunch 3 3 0123456789ABCDEF -o 3digits.txt</p><br>This command generates a list of 16 hexadecimal characters, and the output is saved to the "3digits.txt" file.<br><br>

4. Use Hydra to perform a brute force attack on the door control system. Analyze the HTML code to extract relevant information about the login page. Run the following Hydra command:<br><br><p align = 'center'>hydra -l '' -P 3digits.txt -f -v 10.10.82.50 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000p><br>This command specifies the login page, form data, and the password file. Hydra will attempt all possible passwords until it finds the correct one.<br><br>

<p align = 'center'>

![](<Pictures/Day 3 - Brute_Force_with_Hydra.png>)

</p><br>

5. Upon successful brute force, Hydra will find the correct PIN code. Enter the discovered PIN code at http://MACHINE_IP:8000/ using the AttackBox’s web browser to gain access to control the door. The flag will be displayed, which is 'THM{pin-code-brute-force}'.<br><br>

<p align = 'center'>

![](<Pictures/Day 3 - Retrieve_the_Flag.png>)

</p><br>

<b>Lessons Learned:</b><br>
- Understanding the feasibility of brute force attacks based on password complexity and the number of possible combinations.
- Using tools like Crunch to generate password lists and Hydra to perform brute force attacks.
- Analyzing HTML code to extract information for Hydra command parameters.<br><br>

<b>Conclusion:</b><br>
Day 3 of Advent of Cyber 2023 provided practical insights into the feasibility of brute force attacks on systems with PIN code protection. The challenge demonstrated the importance of password complexity and highlighted tools used in password cracking.

</font>