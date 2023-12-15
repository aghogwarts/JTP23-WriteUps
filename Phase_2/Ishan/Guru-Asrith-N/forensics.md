### writeup on forensics

started reading primer initially whose link is sent in readme

#### tunn3l_v1s10n

openned the tunn3l_v1s10n challenge    
downloaded the link in webshell using `wget https://mercury.picoctf.net/static/01be2b38ba97802285a451b94505ea75/tunn3l_v1s10n `    
used `file tunn3l_v1s10n` . It showed that it is a data file   
used `cat tunn3l_v1s10n` . It didn't work  
used `grep picoCTF tunn3l_v1s10n` . It didn't work     
used `strings tunn3l_v1s10n` . It didn't work       
used `grep pico tunn3l_v1s10n | cat > data`. It didn't work     
got stuck for a while     
saw writeups 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/tunn3l%20v1s10n/tunn3l%20v1s10n.md'   
opened ubuntu because hex editor is required   
opened it using a image viewer. Got to know it was a 'BMP' file as well as the fact that there was a problem in the header     
downloaded 'GHex editor'      
downloaded the file in computer    
opened it in 'GHex editor'   
read about this file 'http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm' and 'http://www.novell.com/documentation/ndsv8/usnds/c1help/novell_common/hexeditor.html' in the writeup to understand about hex editor and BMP header   
noticed the incongruencies in header and width size . Increased the height of image as indicated in hint . Made the size of the width and header equal to make it a square     
opened the image in a photo editor 'photopea.com' to view the image   
got the flag    
```
flag : picoCTF{qu1t3_a_v13w_2020}
```

#### trivial FTP

opened the challenge     
downloaded the file in ubuntu terminal using `wget https://mercury.picoctf.net/static/e4836d9bcc740d457f4331d68129a0bc/tftp.pcapng`     
used `file tftp.pcapng`     
opened it in 'wireshark' since it is a packet distribution     
searched in google for what is tftp . found that it was more of sending data and recieving acknowledgements     
looked it up in a writeup 'https://medium.com/@quackquackquack/picoctf-trivial-flag-transfer-protocol-writeup-20c5d2d0dfdf'      
used `tftp.type` to filter all files      
after filtering all files i exported them using 'file--> export --> TFTP'     
after that saved them in downloads      
after that went to terminal     
went into downloads using `cd downloads` and used `cat instructions.txt` . found encrypted text    
tried using ROT13 decryption pattern using `cat instructions.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`    
got a code which says 'TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN' . this is without space in between words   
it says to check the plan    
so used `cat plan` . the text is encrypted again mostly using ROT13    
tried using ROT13 decryption pattern using `cat plan | tr 'A-Za-z' 'N-ZA-Mn-za-m'`    
got a code which says 'IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS'     
since it says program tried to run the program using `cat program`     
didn't work    
so used `sudo apt-get install program.deb`    
gave an output to replace program with steghide    
so used `sudo apt-get install steghide`     
looked up 'http://steghide.sourceforge.net/'    
tried to find where steghide was installed    
tried to extract the pictures using `steghide extract -sf picture1.bmp -p “DUEDILIGENCE”` since it said that he used the program with DUEDILIGENCE as password    
tried the same with picture2 and picture3 .Didn't work      
later realised that once you open 'program.deb' in files you have to unzip 3 files in it     
after unziping them went through each of the files      
inside the 'data' folder "usr/share/doc/steghide" there is a readme file zipped     
unzipped it and read it     
it said that you have to also install libmhash, libmcrypt, libjpeg and zlib for steghide to work    
so installed them     
tried to extract the pictures using `steghide extract -sf picture1.bmp -p “DUEDILIGENCE”` . no output    
got an output when i tried the samething for picture3    
using steghide extracted the file `steghide extract -sf picture3.bmp`    
gave the output as a file named flag.txt    
used `cat flag.txt`    
got the flag      
``` 
flag : picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}  
```

#### macrohard weakedge

opened the challenge    
installed the file using `wget https://mercury.picoctf.net/static/d3dd8cd51524d9fafcccd1b7d55f85e7/Forensics%20is%20fun.pptm`      
used `file 'Forensics is fun.pptm'` . found that it is a microsoft ppt    
used `cat 'Forensics is fun.pptm'` . got nothing     
went through writeup 'https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/MacroHard%20WeakEdge/MacroHard%20WeakEdge.md' . Didn't understand properly     
installed binwalk and used `binwalk 'Forensics is fun.pptm'`    
found zip files . extracted them using `binwalk -e 'Forensics is fun.pptm'`    
used `ls`     
found 0.zip file     
extracted using `extract 0.zip`     
tried using `grep -r pico`. Didn't work     
tried using `find hidden` . Didn't work     
used `man find`. found tree function as interesting    
downloaded tree using `sudo apt install tree`     
used `tree`    
found a file name hidden     
used `cd ppt/slideMasters`   
used `ls`    
used `cat hidden`   
after searching in google found that it was a base64 encoded file    
after decoding it got the flag   
```
flag : picoCTF{D1d_u_kn0w_ppts_r_z1p5}   
```


