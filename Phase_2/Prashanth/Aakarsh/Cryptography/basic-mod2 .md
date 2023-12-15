### Approach used
We will just modify the same code we used in basic-mod1 by again using nano editor and this time using the new sequence '268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131' and also changing ` flag += alphabet[int(i) % 37]` to `flag += alphabet[pow(int(i), -1, 41) - 1]`.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/596cf674-b07d-4b5c-9f90-46c39d602e4b)

and after saving we will run the code using python3 and get the flag.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/67be8ed3-3422-4509-8c4d-a767dca470a4)

### Flag 
> picoCTF{1nv3r53ly_h4rd_8a05d939}

### Resources used 
To edit the code I referred to [this video.](https://www.youtube.com/watch?v=L18kp5QXhEk)
