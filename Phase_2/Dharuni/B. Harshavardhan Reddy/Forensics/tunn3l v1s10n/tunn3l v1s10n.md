### tunn3l v1s10n

**Description**

We found this file. Recover the flag.

**Solution:**

check the file type `file tunn3l_v1s10n`
 >`tunn3l_v1s10n: data`

Open tunn3l_v1s10n using imagemagick
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/97fca5d4-ad62-4e44-a308-2a3c17c211a7)
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/e6ec378e-04bd-41cd-9084-8c25940d428f)

It is a BMP(bitmap) file. we can learn more about at  [BMP File format](http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm?source=post_page-----ed6fbbf1c54--------------------------------)

hexdump the file `hexdump -C tunn3l_v1s10n | head`
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/f094be4b-bc62-4bdc-9dac-73de145970ae)

`exiftool tunn3l_v1s10n`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/a6005579-46bd-4db6-af17-1b2f43df50fb)

The file size is `2893400` bytes. Given that `bit depth = 24`, this should be account for around `(2893400 * 8) / 24 ~= 964466` pixels. However, we only have `1134 * 306 = 347004` pixels according to the dimensions. We can adjust the dimensions so that all the data is accounted for. Adjusting the width`1134` seems to distort the image, so we should probably stick to adjusting the height`306`. `964466 / 1134` gives us `~850` so let's try that as the height

Let check the hex values of dimensions using `python3`. 

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/67b52dff-36d2-4cd3-95ad-ff322f7114c0)

Now, Let change the hex values of bmp file using `hexedit tunn3l_v1s10n`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/0b511af0-193c-4915-98f4-256d9b5601f5)
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/8cd955d8-b0b4-436d-99bc-9f5896fcc678)
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/32a48857-c9ed-4a03-9c3f-48ef1531dc11)

We need to fix the header by comparing another `.bmp` file
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/e31fb3b6-c1c6-43b8-b008-22772afefa7d)


Try to open the image now, Using `display tunn3l_v1s10n` 
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/36c300e0-5178-403a-b1cc-f925b6992de1)

we get the **flag:** `picoCTF{qu1t3_a_v13w_2020}`

[References](http://www.novell.com/documentation/ndsv8/usnds/c1help/novell_common/hexeditor.html?source=post_page-----ed6fbbf1c54--------------------------------)
[1](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/tunn3l_v1s10n.md?source=post_page-----ed6fbbf1c54--------------------------------)
[2](https://www.youtube.com/watch?v=d63buMlAUHM&pp=ygUVdHVubjNsIHYxczEwbiBwaWNvY3Rm)
