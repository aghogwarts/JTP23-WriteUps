## CaaS
The `index.js` file appears to be passing the __message__ directly to the system and executing it, __message__ being the URL portion that comes after `cowsay`. This is a command injection vulnerability which can be exploited by passing multiple commands using `;`. First the contents of the page can be found using `ls`, which reveals a file `falg.txt`. The contents of this file canbe accesssed using the `cat` command. The command needs to be URL encoded, which can be done by replacing the space with `%20`.


flag: picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}

![CaaS_sol](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/935616f2-be03-48d4-8680-93fb4f7fe4c3)


## Forbidden Paths
From the problem statement, it appears that the website searches for files at the given address `/usr/share/nginx/html/`. However, the required file is stored in the root directory itself. To access it without using the absolute path `/flag.txt`, we use `..` which takes us to the previous directory. With the knowledge that we need to jump back 4 times, the relative path to be used is `../../../../flag.txt`


flag: picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}

## Local authority
Inspecting the login failure page revealed a file `secure.js` which contained the login credentials. Once logged in, the flag was obtained.


flag: picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}

![image](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/1aa3a051-2a84-44b2-8c12-4cfa1066e9c0)


##  Cookies
By inspecting the elements and navigating to cookies, and loading the website with different values for the cookie, the flag was obtained.


flag: picoCTF{3v3ry1_l0v3s_c00k135_cc9110ba}

![cookies](https://github.com/aghogwarts/JTP23-WriteUps/assets/76529146/d54f884e-f4d3-471a-9351-f4a3e3a49537)

## Inspector
Inspecting the three sources of the page, the comments formed the complete flag.

flag: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
