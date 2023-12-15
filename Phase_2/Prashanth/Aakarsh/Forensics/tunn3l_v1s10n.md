# tunn3l_v1s10n

### Approach Used

After downloading the file we can see in our file manager that it does not have any file extension, which means we don't know the file type hence can't open it in any app. We can use `xxd -g 1 tunn3l_v1s10n | head` where 'g' is used to group the bytes and 1 to group them in bits mode, also we can use head tool by piping to get only the first 10 lines and not get the unimportant data. 
![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/7248d058-4a9f-49de-a79e-4f42486c90f8)

Now we can check [list of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures) to see what type of file do we have.
![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/d6cf5a6a-2f9a-447b-bd90-6d1075e1d89d)

We can see that the starting '42 4d' matches with the 'bmp' file type so this is a bmp image file so first we will rename it 'tunn3l_v1s10n.bmp' and use some photo editors like [ImageMagick](https://imagemagick.org/index.php), [Photopea](https://www.photopea.com/) to open this file and we will get the below pic.

![download (4)](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/fd261768-9709-4125-9e8e-3c5c642ebfaa)

It looks like this pic is not complete and is cropped so we will increase its height, but because this is a bmp file so we will use a hex editor to edit the bitmap header for that we will change `32 01` to `32 04` in the `6E 04` to increase the height. for this we will use [HexEd.it](https://hexed.it/).

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/63b485c0-b627-450e-af2e-9d8858fd1bf1)

After doing this we will get the entire picture and the flag too.

![download (5)](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/0245888a-5227-423d-96d2-8be7023cdb3c)

### Flag
> picoCTF{qu1t3_a_v13w_2020}
### Resources Used
[BMP Wikipedia page](https://en.wikipedia.org/wiki/BMP_file_format) to know more about bmp and header, and [height property of bitmap](https://stackoverflow.com/questions/1973903/reading-and-parsing-the-width-height-property-of-a-bitmap) forum to get more idea.

