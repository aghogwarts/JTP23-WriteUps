DAY 1:

In this task, we learnt about how an AI's vulnerabilities can be exploited. If we ask the right questions, we can get the bot to leak information. Hence Though it's exciting, chatbot technology still has a long way to go. Like many parts of cyber security, it's always changing as both security measures and tricks to beat them keep evolving together.


DAY 2:

In this task, we learn about Python and its libraries like Pandas, DataFrame and Matpltlib and using them to analyse packet capture using Jupyter notebook.


DAY 3:

In this task, we learn how to brute force using hydra. Since a single pin can have millions of possible combinations, it impossible to manually insert numbers to crack the code. So instead we create a password list using another tool Crunch and use the passwords file along with hydra which bruteforces all the passwords into the link we provide and tells us when its gotten a hit.

Using crunch and hydra, find the PIN code to access the control system and unlock the door. What is the flag?
THM{pin-code-brute-force}


DAY 6:

In this task, we leanr about buffer overlow vulnerability. In the given game we are supposed to get enough coins to buy a star which gives us the flag. The star requires 10000 coins which makes the game unwinnable practically. We can use one coin to change our name and this is where we get an opportuniy to attack. If we change the name to something big enough, the stack overflows into the next memory allocated to coins and get how many ever coins we wish.

There is also the concept of little endianness. Integers in C++ are stored in a very particular way in memory. First, integers have a fixed memory space of 4 bytes, as seen in the debug panel. Secondly, an integer's bytes are stored in reverse order in most desktop machines. This is known as the little-endian byte order.

Finally the challenege of the rigged star, where the star gets replaced by another object whenever we buy it can again be solved using buffer overflow, where we can make the name large enough to fill the memory for all slots before the inventory memory and then enter the value we need 'd' which was generally getting replaced by 'e' due to the rig and give the star to the tree.

If the coins variable had the in-memory value in the image below, how many coins would you have in the game?
1397772111

What is the value of the final flag?
THM{mchoneybell_is_the_real_star}


DAY 8:

In this challenege, we use the FTK imager which is a forensics tool that allows forensic specialists to acquire computer data and perform analysis without affecting the original evidence, preserving its authenticity, integrity, and validity for presentation during a trial in a court of law. We can analyse malware infected system to retrive deleted files which can trace us back to the perpetrator. It clearly shows which files have been deleted and we get hidden information from it. Additionally, the SHA hash value option in the imager can  verify the integrity of a drive/image.

What is the malware C2 server?
mcgreedysecretc2.thm

What is the file inside the deleted zip archive?
JuicyTomaTOY.exe

What flag is hidden in one of the deleted PNG files?
THM{byt3-L3vel_@n4Lys15}

What is the SHA1 hash of the physical drive and forensic image?
39f2dea6ffb43bf80d80f19d122076b3682773c2


DAY 9:

This task starts off initially by giving basic syntax of C# programming and then explains abut C2. C2, or command and control, refers to a centralised system or infrastructure that malicious actors use to remotely manage and control compromised devices or systems. It serves as a channel through which attackers issue commands to compromised entities, enabling them to carry out various activities, such as data theft, surveillance, or further malware propagation.

We can decompile malware using dnSpy. dnSpy is an open-source .NET assembly (C#) debugger and editor. It is typically used for reverse engineering .NET applications and analysing their code and is primarily designed for examining and modifying .NET assemblies in a user-friendly, interactive way. It's also capable of modifying the retrieved source code (editing), setting breakpoints, or running through the code one step at a time (debugging).

We run through the program functions and understand what each of them do and answer the question based on that.

What HTTP User-Agent was used by the malware for its connection requests to the C2 server?
Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15

What is the HTTP method used to submit the command execution output?
post

What key is used by the malware to encrypt or decrypt the C2 data?
"youcanthackthissupersecurec2keys

What is the first HTTP URL used by the malware?
http://mcgreedysecretc2.thm/reg

How many seconds is the hardcoded value used by the sleep function?
15 (15000 milliseconds , so 15 seconds)

What is the C2 command the attacker uses to execute commands via cmd.exe?
shell

What is the domain used by the malware to download another binary?
stash.mcgreedy.thm


DAY 10:

This task deals with SQL injection vulnerabilities. A website was defaced because the website didnt check for malicious input. Taking in user-supplied input gives us powerful ways to create dynamic content, but failing to secure this input correctly can expose a critical vulnerability known as SQL injection (SQLi).

It also introduces us to PHP.PHP is a popular general-purpose scripting language that plays a crucial role in web development. It enables developers to create dynamic and interactive websites by generating HTML content on the server and delivering it to the client's web browser. PHP is a server-side scripting language, meaning the code is executed on the web server before the final HTML is sent to the user's browser. Unlike client-side technologies like HTML, CSS, and JavaScript, PHP allows developers to perform various server-side tasks, such as connecting to a wide range of databases.

We then understand the 'OR 1=1' payload. The 1=1 makes the OR statement always true and the -- at the end of the input is a comment in SQL. It tells the database server to ignore everything that comes after it. Ending with a comment is crucial for the attacker because it nullifies the rest of the query and ensures that any additional conditions or syntax in the original query are effectively ignored.

Stacked query-Stacked queries enable attackers to terminate the original (intended) query and execute additional SQL statements in a single injection, potentially leading to more severe consequences such as data modification and calls to stored procedures or functions.

xp_cmdshell : It is a system-extended stored procedure in Microsoft SQL Server that enables the execution of operating system commands and programs from within SQL Server. It provides a mechanism for SQL Server to interact directly with the host operating system's command shell. While it can be a powerful administrative tool, it can also be a security risk if not used cautiously when enabled.

To get access into the hacked website, we use the MSFvenom, a command-line payload generation tool. We then exexcute the commands mentioned to get access to the database and restore it useing the restore website file present in the Desktop directory.

Manually navigate the defaced website to find the vulnerable search form. What is the first webpage you come across that contains the gift-finding feature?
/giftsearch.php

Analyze the SQL error message that is returned. What ODBC Driver is being used in the back end of the website?
ODBC Driver 17 for SQL Server

Inject the 1=1 condition into the Gift Search form. What is the last result returned in the database?
THM{a4ffc901c27fb89efe3c31642ece4447}

What flag is in the note file Gr33dstr left behind on the system?
THM{b06674fedd8dfc28ca75176d3d51409e}

What is the flag you receive on the homepage after restoring the website?
THM{4cbc043631e322450bc55b42c}

