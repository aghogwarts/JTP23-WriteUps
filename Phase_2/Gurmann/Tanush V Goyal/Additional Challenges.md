## Cookies (web)
I inspected the website. In the cookies tab there was a cookie `name` ehose value was -1. On reloading the website after changing the cookie value, the text on the screen kept changing. I kept incrementing the value until at 18 the flag was obtained.
flag: picoCTF{3v3ry1_l0v3s_c00k135_ac9150bb}

## Inspector (web)
Again, it was a matte rof simply inspecting the page. The three files contained the flag in three parts.
flag: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?fe7ba3e3}

## information (forensics)
The hint said something about the flag being hidden in the details of the file which led me to think about the exif data. Used an online tool to look at the metadata. Found an encoded string between two `PicoCTF`s. Decoded it using base64 to get the flag.
flag: picoCTF{the_m3tadata_1s_modified}

![information_T](https://github.com/aghogwarts/JTP23-WriteUps/assets/107710230/83754e79-b071-4f95-9c0d-f5a47deb32a5)

## Matryoksha doll
A simple google search about Matryoksha dolls led me to the this [binwalk tutorial](https://gist.github.com/briankip/8f8747a2488af827e3b4). Using binwalk on the image provided and extracting the Matryoksha doll images one by one, I found the flag.txt file.

![Matryoksha_sol](https://github.com/aghogwarts/JTP23-WriteUps/assets/107710230/5ebfb647-99ec-4b6e-b281-642b76bf9c40)


picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}
