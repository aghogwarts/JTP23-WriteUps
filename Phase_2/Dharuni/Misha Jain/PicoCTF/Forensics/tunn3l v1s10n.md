<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - tunn3l v1s10n Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup guides you through the process of solving the "tunn3l v1s10n" challenge in PicoCTF. The tunn3l v1s10n challenge involves exploring a web application that has issues displaying a bitmap image. The goal is to identify the cause of the image problem and uncover any hidden information or flags.

<b>Author:</b> Misha Jain

<b>Date:</b> November 15, 2023

<b>Tools Used:</b><br>
- Terminal
- Web Browser (Firefox)
- HexEditor

<b>Challenge Description:</b><br>
'tunn3l v1s10n' is a web exploitation challenge where participants need to investigate why a bitmap image isn't displaying correctly on the web application. The challenge may involve or image manipulation techniques.

<b>Exploitation:</b><br>
1. Begin by downloading the file and checking its file type using the file command.<br>

<p align = 'center'>file tunn3l_v1s10n</p><br>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - Filetype.png>)

</p><br>

2. However, since the file command doesn't provide sufficient information about the file, we will use the mimetype command.<br>

<p align = 'center'>mimetype tunn3l_v1s10n</p><br>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - Mimetype.png>)

</p><br>

3. Use the mv command to change the extension of the file to .bmp

<p align = 'center'>mv tunn3l_v1s10n tunn3l_v1s10n.bmp</p>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - Change_Extension.png>)

</p>

4. Since tunn3l_v1s10n is an image bitmap file, and it isn't displaying, we will view it in a hexeditor.<br>

<p align = 'center'>wxHexEditor tunn3l_v1s10n</p><br>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - HexEditor_Initial.png>)

</p><br>

5. A few of the initial header values are incorrect, and need to be static values. Using the editor, we can edit these values to their correct forms.<br>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - HexEditor_Changed_Once.png>)

</p><br>

6. Using the feh command, we can display the bitmap image.<br>

<p align = 'center'>feh tunn3l_v1s10n.bmp</p><br>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - First_Image.png>)

</p><br>

7. This image still doesn't display the correct flag. Use the exiftool command to view the resolutions of the image.<br>

<p align = 'center'>exiftools tunn3l_v1s10n.bmp</p><br>

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - Exiftool.png>)

</p>

8. This shows that the Image Length (Image Width * Image Height * Bit Depth / 8) is 2893400, so assuming the width is correct, the height should be just under 850. I took it as 840. Changing the values in the HexEditor to match the hexadecimal value of 840 in little endian.

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - HexEditor_Changed_Twice.png>)

</p>

9. Using the feh command to display the final image. The flag is displayed.

<p align = 'center'>

![](<Pictures/Tunn3l v1s10n - Final_Image.png>)

</p>

<b>Conclusion:</b><br>
The tunn3l v1s10n challenge provides hands-on experience in identifying and resolving image display problems on a web application. It introduces participants to the concept of and encourages creative problem-solving.

</font>