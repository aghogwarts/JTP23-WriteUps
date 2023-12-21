# Day 5
## taskname
A Christmas DOScovery: Tapes of Yule-tide Past 
### learnings
What is DOS? - The Disk Operating System was a dominant operating system during the early days of personal computing. Microsoft tweaked a DOS variant and rebranded it as MS-DOS, which later served as the groundwork for their graphical extension, the initial version of Windows OS. The fundamentals of file management, directory structures, and command syntax in DOS have stood the test of time and can be found in the command prompt and PowerShell of modern-day Windows systems.

Different commands to be used in DOS:- 
![image](https://github.com/vishwatejD/advent-of-cyber-2023/assets/141154035/3d2b7a56-1efe-4c0a-869f-56a200211dda)
> other commands :- `tc filename` command used for opening a file with borland turbo c compiler for c files.

QUESTION 1:-

How large (in bytes) is the AC2023.BAK file?

As we use the DIR command we can see that the size of the required file is **12,704** bytes.

___
QUESTION 2:-

What is the name of the backup program?

When we use the command CD TOOLS we can find the Directory named BACKUP when we jump into that directory we can find the backup file.
Inintially when we use the command TYPE README.TXT we find the name of the backup program as _**Backup master 3000**_.
___

QUESTION 3:-

What should the correct bytes be in the backup's file signature to restore the backup properly?

When we read the README.TXT file , the troubleshooting column has the correct magic bytes for the file to excecute properly. (41,43)
___

QUESTION 4:-

What is the flag after restoring the backup successfully?

To restore the flag we first try to run it using the backup program but it fails because the file didnot have the correct magicbytes.
We use the command EDIT c:\AC2023.BAK then change the first two letters from `XX` to `AC`.
> we change it to AC because the bytes were 41, 43

Now we save it and run the command BUMASTER.EXE C:\AC2023.BAK this gives us the flag.

FLAG:- THM{0LD_5CH00L_C00L_d00D}
