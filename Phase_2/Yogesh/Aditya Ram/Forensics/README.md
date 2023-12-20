# tunn3l_v1s10n

1) After downloading the given file in the question, on analysis as a text file, it has 'BM' at the beginning indicating it is in a bitmap format.
2) I then converted the file into a bitmap file.
3) When i opened the file, it showed the following image: 

![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/8f715c03-06d2-4991-baa9-d01520b6754c)

4) I then printed the hex dump for the file.

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/44ae3174-02a2-4594-98f5-aec0ead6eb56)

5) On analysis of the hex dump, the pixel array of the bitmap header file was wrong because the byte at which it started was too high.
6) So instead, I used the address of the cursor offset 54 in the hex dump and put it in the pixel array of the header.
7) I then changed the height and size of the image so all the contents can be seen.

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/3a61a3ad-e109-4f39-9456-7d02ded33df5)

8) After editing the hex dump, i then opened the file again and got this image with the flag

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/af4f36da-dd08-4210-a338-482f1a1533c2)

   # Flag

   picoCTF{qu1t3_a_v13w_2020}



   




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



