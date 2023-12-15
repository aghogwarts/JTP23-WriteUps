We have been given a pptm file over here. 
Checking file details there is nothing useful found:

![mw1](https://github.com/poorvi1910/Cryptonite/assets/146640913/f73458d0-44ab-49b8-b54c-c835f48daa9a)


Hence we can convert the file to a zip instead by changing extension to ‘.zip’ instead of ‘.pptm’ and sorting through the files, we come across a file named ‘hidden’

Opening the hidden file we get the cipher below:
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q

Since there are uppercase, lowercase AND digits in the license, it might be base64 encoded
Decoding through base64 we get:

flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
