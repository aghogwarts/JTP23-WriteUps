When we go to the website, type in file.txt and read, we get an expected error of ‘File does not exist’.

The description mentioned that we are now located at /usr/share/nginx/html/, and flag is stored in  /flag.txt. So we can use path traversal. Path traversal is also known as directory traversal. These vulnerabilities enable an attacker to read arbitrary files on the server that is running an application. To achieve this, we use   ../ to travel to the upper layer.
We need to go back 4 layers to travel back to the home directory, so we need to modify the filename section to ../../../../flag.txt

![fp1](https://github.com/poorvi1910/Cryptonite/assets/146640913/0c42cf1d-54c0-41fa-9693-17a5b99cc829)

When we click on read now, we get the flag:
picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}

What is path traversal:
https://portswigger.net/web-security/file-path-traversal

