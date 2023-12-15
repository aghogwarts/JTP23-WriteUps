# Macrohard Weakedge

### Approach Used
After downloading it, I used the unzip command in my linux terminal 'unzip 'Forensics is fun.pptm' -d flag' to get my extracted files into a directory called flag after that I used 'cd'  to enter and then ls to see the files inside. Then i use it again to enter the 'ppt' directory then again to enter 'slideMasters' directory. There I found a hidden file so I used 'cat' to read it.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/71b055a6-c9cb-4ea9-891c-ff53c5c2d6ca)

In the hidden file I will get the flag which looks like it is encoded in base64 so use an online [base64 encoder and decoder](https://www.base64decode.org/) to decode it and get the flag.

### Flag
> picoCTF{D1d_u_kn0w_ppts_r_z1p5}
### Resources Used
Virtual Box to use Linux terminal.
