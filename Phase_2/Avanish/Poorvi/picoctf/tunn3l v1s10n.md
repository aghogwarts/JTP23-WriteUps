Putting the image in a hex editor, we get file signature as 42 4D which corresponds to a BMP file. Adding a ‘.bmp’ extension to the file and opening it in an online editor like Photopea, we get the following image

![tv1](https://github.com/poorvi1910/Cryptonite/assets/146640913/c262ae83-a980-4d06-90bc-b11329f55dcf)

The image does not look like it is displaying completely, so we can go to hex editor and change the height to equal the width(as width is more)

![tv2](https://github.com/poorvi1910/Cryptonite/assets/146640913/9c3c6731-2fba-4cc7-b4ea-29085a90e524)

Original header:

![tv3](https://github.com/poorvi1910/Cryptonite/assets/146640913/cc3ae526-dc0a-44a6-b0ef-7e69121ab759)

Changed header(4 bytes starting from offset 16):

![tv4](https://github.com/poorvi1910/Cryptonite/assets/146640913/6b274e7b-a7db-41ab-863a-fa7acdca77a7)

On doing so we get the following image

![tv5](https://github.com/poorvi1910/Cryptonite/assets/146640913/9d00cc46-131e-4b9f-8564-fb22fb29ec88)

On further changing dimensions we can get more and more of the image but we can stop since we have gotten our flag.

We have hence gotten our flag which is:
picoCTF{qut3_a_v13w_2020}

How hex offsets work:
https://stackoverflow.com/questions/141262/can-someone-explain-hex-offsets-to-me
