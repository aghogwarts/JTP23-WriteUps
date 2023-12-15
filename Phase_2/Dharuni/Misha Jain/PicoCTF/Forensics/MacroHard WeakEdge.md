<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - MacroHard WeakEdge Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup explains the process of solving the "MacroHard WeakEdge" challenge in PicoCTF. The MacroHard WeakEdge challenge involves analyzing a Microsoft Powerpoint document (.pptm) that contains hidden information. Participants are tasked with uncovering the hidden content and finding the flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 15, 2023

<b>Tools Used:</b><br>
- Terminal
- Microsoft PowerPoint

<b>Challenge Description:</b><br>
In the MacroHard WeakEdge challenge, participants need to inspect a powerpoint document for hidden content or embedded macros. The goal is to extract any concealed information and locate the flag within the document.

<b>Exploitation:</b><br>
1. Download the file and use the following command to find any externally embedded macros. The 'olevba' command is used to extract and analyze Visual Basic for Applications (VBA) macros embedded in Microsoft Office documents.<br>

<p align = 'center'>olevba Forensics\ is\ fun.pptm</p><br>

<p align = 'center'>

![](<Pictures/MacroHard WeakEdge - olevba.png>)

</p><br>

2. Use the following command to unzip the ppt and store the unzipped contents in a directory called macro.<br>

<p align = 'center'>unzip Forensics\ is\ fun.pptm -d macro</p><br>

<p align = 'center'>

![](<Pictures/MacroHard WeakEdge - Unzipping.png>)

</p><br>

3. Upon directing to the slideMasters directory, we see a hidden file. Cat the contents of that file. We get a base64 encoded string.<br>

<p align = 'center'>

![](<Pictures/MacroHard WeakEdge - slideMasters.png>)

</p><br>

4. Use the following command to remove the spaces of the string. The sed command is used to replace certain characters of a string with other characters. 's' stands for substitute and 'g' stands for global. Use the base64 -d command to decode the string<br>

<p align = 'center'>cat hidden | sed 's/ //g' | base64 -d</p>

<p align = 'center'>

![](<Pictures/MacroHard WeakEdge - Decoding.png>)

</p>

<b>Conclusion:</b><br>
The MacroHard WeakEdge challenge provides practical experience in inspecting powerpoint documents for hidden information and flags. It reinforces the importance of document forensics in cybersecurity.

</font>