# Macrohard Weakedge

1) I first downloaded the pptm file and then compressed it into a zip file

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/c824d98f-767a-41ce-8604-8455e8c70516)

2) I then extracted all the files and I saw there were many directories and subdirectories in it.
3) I then went on linux command line and used 'ls -aR' to list all the files and its subdirectories.
4) I was browsing through the files listed and found a hidden file

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/cab14285-7810-4f53-996f-967cbe533991)

5) I then ran a python code to remove all the space from the given text.

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/62e4fea7-2f6e-4e21-8d11-a2354fed1507)

6) I realised it was base64 text so converted it to a string using an online converter: https://www.base64decode.org

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/8d2227cf-6881-4b09-891b-aec428277e7d)

7) I got the required flag to complete the level after conversion.

   # Flag

    picoCTF{D1d_u_kn0w_ppts_r_z1p5}



