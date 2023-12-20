<font size='4'>
<p align='center'>
<b>
Advent of Cyber - Day 9 Writeup
</b>
</p>
</font>

<br>
<font size='3'>

<b>Introduction:</b><br>
This writeup documents the investigation conducted by Forensic McBlue and the team on Day 9 of the Advent of Cyber 2023 challenge. Their objective was to analyze a retrieved malware sample, unravel its command and control (C2) infrastructure, and understand its capabilities. The team's focus on static analysis provided insights into the malware's functionalities and its communication with the C2 server.

<b>Author:</b> Misha Jain

<b>Date:</b> December 9, 2023

<b>Tools Used:</b><br>
- dnSpy
- C# programming knowledge

<b>Malware Analysis:</b><br>
The team approached the analysis with caution, utilizing a malware sandbox to prevent any harm during the investigation. Key learnings included understanding the fundamentals of .NET binaries, the C# programming language, and using dnSpy for decompiling malware samples.

<b>Analysis Highlights:</b><br>
1. **Malware Handling 101: Sandbox Setup**
   - The importance of a sandbox environment for safe malware analysis.
   - Components of a typical malware sandbox setup: network controls, virtualization, monitoring, and logging.

2. **Static Analysis with dnSpy:**
   - Decompiling the malware sample written in C# using dnSpy.
   - Exploration of the main functionalities and modules within the malware.

3. **Understanding .NET Compiled Binaries:**
   - Overview of .NET binaries and their compilation process.
   - Differentiating .NET binaries from traditional compiled languages.

4. **C2 Primer:**
   - Introduction to Command and Control (C2) in the context of malware.
   - Recognizing C2 behaviors, including HTTP requests, command execution, and sleep/delay tactics.

5. **Malware Functions Overview:**
   - Analysis of key functions within the malware, including GetIt, PostIt, Sleeper, ExecuteCommand, Encryptor, Decryptor, and Implant.
   - Identification of functionalities such as HTTP requests, OS command execution, encryption, and dropper capabilities.

6. **Building the Malware Execution Pipeline:**
   - Breakdown of the Main function's code execution flow.
   - Understanding the C2 communication, command parsing, and response reporting mechanisms.
   - Recognition of commands: sleep, shell, implant, and quit.

<b>Answers to Questions:</b><br>
1. What HTTP User-Agent was used by the malware for its connection requests to the C2 server?
    - You should see the Entry Point: JuicyTomatoy.Program.Main on the line no. 4. Click on the Main to open the Main method. We see the code of the C2 server. First imoprtant thing you will see is that it is making post requests to something on line no. 22. If you double click on the PostIt method to look inside it. You will see the User-Agent used for connection. That will be the answer.<br><br>
    - Answer: Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15

2. What is the HTTP method used to submit the command execution output?
    - Scroll back to the top to go to Main method again. If you look and understand the code you will see the line no. 54 to 56 is executing and sending the command. It is the same method as earlier. You can check the HTTP Method and that would be the answer.<br><br>
    - Answer: POST

3. What key is used by the malware to encrypt or decrypt the C2 data?
    - If you open the Program folder from the left panel and you will see Encryptor and Decryptor method. Open the Decryptor method and you should see the key there stored as the variable.<br><br>
    - Answer: youcanthackthissupersecurec2keys

4. What is the first HTTP URL used by the malware?
    - Go back to main method again. Let's see when the first request is being made in the code execution. We keep coming back to line no. 9. It is using the value from url variable which is string concatanation of str and other hardcoded string. Combine them and you have your answer.<br><br>
    - Answer: http://mcgreedysecretc2.thm/reg

5. How many seconds is the hardcoded value used by the sleep function?
    - In the Main method we see the Program.Sleeper method being called on line no. 14. It is using the count variable which is being set on the line no. 10. It is defined in the milliseconds so convert it to the seconds.<br><br>
    - Answer: 15

6. What is the C2 command the attacker uses to execute commands via cmd.exe?
    - From line no. 30 to 36 we see there are four commands: sleep, shell, implant and quit. Here, the function is in the second if-else statement so when the a == shell, the ExecuteCommand function will execute.<br><br>
    - Answer: shell

7. What is the domain used by the malware to download another binary?
    - From the same code, we can also get the domain used by the malware which use to download another binary.<br><br>
    - Answer: stash.mcgreedy.thm

<b>Conclusion:</b><br>
Day 9's challenge provided a deep dive into malware analysis, empowering participants with skills to dissect .NET binaries, understand C2 behaviors, and employ tools like dnSpy. The collaborative effort of Forensic McBlue and the team uncovered the intricacies of the malware's communication, shedding light on its capabilities and enabling them to thwart the mind control incident orchestrated by Tracy McGreedy.

</font>
