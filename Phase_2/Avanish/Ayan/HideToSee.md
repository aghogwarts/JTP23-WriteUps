# HideToSee
We are given the image, I run steghide on the image to see for any hidden files, and it shows as file called "encrypted.txt", cat the file to get an encrypted flag, the name of the image gives the hint that this is an
atbash cipher, I used cyber chef to decode the text to get the flag "picoCTF{atbash_crack_7142fde9}".

```
nayanko-picoctf@webshell:~$ steghide extract -sf atbash.jpg
Enter passphrase: 
wrote extracted data to "encrypted.txt".
nayanko-picoctf@webshell:~$ cat encrypted.txt
krxlXGU{zgyzhs_xizxp_7142uwv9}
```
