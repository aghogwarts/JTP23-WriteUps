<font size = '4'>
<p align = 'center'>
<b>
Advent of Cyber - Day 5 Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup details the solution to Day 5 of the Advent of Cyber 2023 challenge titled "Restoring Backups in DOS." The challenge involves working with an old DOS system to restore a backup using the BackupMaster3000 program. The task includes navigating the DOS environment, understanding file signatures, and fixing a file with incorrect magic bytes.<br>

<b>Author:</b> Misha Jain

<b>Date:</b> December 5, 2023

<b>Tools Used:</b><br>
- DOS emulator (DosBox-X)
- MS-DOS Editor
- ASCII table
- Online converters

<b>Challenge Description:</b><br>
Day 5 explores the Disk Operating System (DOS) environment to restore a backup using the BackupMaster3000 program. The challenge involves navigating DOS commands, viewing file contents, and understanding the importance of file signatures (magic bytes) in data recovery and file system analysis.

<b>Exploitation:</b><br>
1. Currently we are in C:\ directory. Run the dir command to list the subdirectories and files with their information. You should see the AC2023.BAK file there and it's size in bytes.<br><br>

2. Now move to the C:\tools\backup directory with the command cd as cd C:\tools\backup. You should be in the directory of the tool that can be used for recovery of the currepted files. You will have the readme.txt file there. You can read it with edit command such as edit readme.txt. You should see the name on the top of the file.<br><br>

3. Correct bytes can be found in the same eadme.txt file's troubleshooting section. It is also mentioned in the day's description.<br><br>

4. Now if we check our file C:\AC2023.bak then it has it's first bytes as XX which are not correct. We need first bytes to be AC(hexadecimal representation) as per the troubleshooting guide from the readme.txt. Now use the edit command like edit C:\AC2023.bak to edit the first two characters to AC and then run the backup program with the command bumaster.exe C:\AC2023.bak, it should provide you the flag.<br><br>

5. Provide answers to questions related to the challenge:

- How large (in bytes) is the AC2023.BAK file?
    - Answer: 12,704
- What is the name of the backup program?
    - Answer: BackupMaster3000
- What should the correct bytes be in the backup's file signature to restore the backup properly?
    - Answer: 41 43
- What is the flag after restoring the backup successfully?
    - Answer: THM{0LD_5CH00L_C00L_d00D}<br><br>

<b>Lessons Learned:</b><br>
- Navigating and using DOS commands.
- Understanding the significance of file signatures (magic bytes) in file identification.
- Troubleshooting and fixing file signature issues.
- Practical application of reverse engineering in a DOS environment.<br><br>

<b>Conclusion:</b><br>
Day 5 of Advent of Cyber 2023 provided hands-on experience with DOS commands and file signatures. The challenge required participants to navigate an unfamiliar legacy system, troubleshoot file signature issues, and successfully restore a backup. This exercise contributes to a foundational understanding of historical operating systems and their relevance in cybersecurity.

</font>