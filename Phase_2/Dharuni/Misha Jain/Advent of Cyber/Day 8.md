<font size='4'>
<p align='center'>
<b>
Advent of Cyber - Day 8 Writeup
</b>
</p>
</font>

<br>
<font size='3'>

<b>Introduction:</b><br>
This writeup unveils the digital forensic journey of Day 8 in the Advent of Cyber 2023 challenge. The plot thickens as Tracy McGreedy's sinister plan is exposed through the meticulous work of McSkidy, Forensic McBlue, and their team. Van Sprinkles, torn between loyalty and morality, plays a crucial role in dismantling McGreedy's cyber conspiracy.

<b>Author:</b> Misha Jain

<b>Date:</b> December 8, 2023

<b>Tools Used:</b><br>
- FTK Imager
- Hex mode for file analysis

<b>Challenge Description:</b><br>
The task involves using FTK Imager to analyze digital artifacts and recover deleted evidence from a USB drive containing malware. McSkidy's team explores the digital breadcrumbs left by McGreedy's cyber attack, uncovering the depth of the conspiracy.

<b>Investigation Highlights:</b><br>
- Examining the write-protected USB drive with FTK Imager.
- Analyzing digital artifacts and evidence related to the cyber attack.
- Recovering deleted files and folders to reconstruct the sequence of events.
- Verifying the integrity of the forensic image for legal validity.

<b>FTK Imager Analysis:</b><br>
1. What is the malware C2 server?
    - Open the deleted folder and click on the text file, you’ll find the c2 server: mcgreedysecretc2.thm

2. What is the file inside the deleted zip archive?
    - Open the deleted zip file and you can see a program: JuicyTomaTOY.exe

3. What flag is hidden in one of the deleted PNG files?
    - Click the portrait.png → Click the Hex View → Click Ctrl+F on the Hex pane and search THM{: THM{byt3-L3vel_@n4Lys15}

4. What is the SHA1 hash of the physical drive and forensic image?
    - Click on the Drive → File → Verify Drive/Image: 39f2dea6ffb43bf80d80f19d122076b3682773c2

<b>Conclusion:</b><br>
Day 8 of Advent of Cyber 2023 immersed participants in a captivating digital forensics challenge. The use of FTK Imager showcased the importance of preserving evidence integrity while uncovering McGreedy's malicious activities. The collaboration between McSkidy, Forensic McBlue, and Van Sprinkles underscored the significance of ethical choices in the face of cyber threats.

</font>
