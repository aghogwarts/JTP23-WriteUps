So for this one I had no clue cuz the metafile I was opening was unreadable.  
Then I tried to change the file format like t zip files and all but that did not work either for me.  
After that I tried to change it into jpg format and to my surprise an image opened up that could lead me to the flag.  
![Screenshot 2023-11-14 235723](https://github.com/SuniCoder9567/Crypt0n1t3/assets/89261516/7e96d9c5-a7af-42c3-9468-2e47a92a8d07)  
_The sorry not a flag sign did not discourage me to discontinue but I was actually doubtful about how to go about this challenge after I moved one step closer towards the answer._  
Although a part of me wondered that the image size is like 2.8MB it must be holding much more than it shows so I decided to give my old friend _hexed.it_ a visit  
But I absolutely failed to find anything that I needed.  
Frustrated enough I open up a writeup on this challenge _https://medium.com/@joao_amaral/pico-ctf-tunnel-vision-forensics-exercise-2e3ed2234b54_ just to take a small hint and from there I came to know about BMP file format!!  
_Apparently, I did notice BM when I opened the meta file but I had no idea they were the headers of a BMP file XD._  
So, I tried to dig in and try to learn about the BMP file format.  
_I downloaded a software called "ImageMagick" as recommended by the writeup to open the image in BMP format_  
So I learnt about how I can change the value of the offset to alter the width and height of an image and I did so with the height offset of the BMP file image  
And Voila!, I got the image height increased to get the flag _picoCTF{qu1t3_a_v13w_2020}_  
![Screenshot 2023-11-15 004004](https://github.com/SuniCoder9567/Crypt0n1t3/assets/89261516/1f1f2b14-63c0-4d2e-b8ff-4f84f69239f8)








