### MacroHard WeakEdge

**Description**
I've hidden a flag in this file. Can you find it? Forensics is fun.pptm

**Solution**

` file Forensics\ is\ fun.pptm`
>Forensics is fun.pptm: Microsoft PowerPoint 2007+

But there is nothing in the ppt. It means something hidden inside. The best approach to finding files hidden inside other files is [binwalk](https://www.kali.org/tools/binwalk/)

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/e610fb0b-55ce-4383-a03f-a9a549679a54)
There are so many hidden zip files hidden inside. To extract use `-e` with `binwalk`

Go to `~/Downloads/picoCTF/_Forensics is fun.pptm.extracted/ppt/slideMasters`

open hidden `cat hidden`
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/28ea0adc-aadd-44e8-9823-92bc3fdf6a6f)

Use this [website](https://www.base64decode.org/) to decode base64.

**Flag:** picoCTF{D1d_u_kn0w_ppts_r_z1p5}
