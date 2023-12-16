HideToSee

We download the file and extract from it, as given in the question.

![image](https://github.com/itstanayhere/phase2_2/assets/147296398/3a9f1ced-229d-4365-bf8f-b9ec8747aaa6)

(From previous task, steghide is a popular tool to hide files inside images, which is why I used it here)

steghide: This is the command-line tool for steganography, used to embed and extract data from files.

extract: This is the command that tells steghide to extract hidden data.
-sf atbash.jpg: This option specifies the file (the file that potentially contains hidden data). In this case, atbash.jpg is assumed to be the file.

These are the contents of the file:

krxlXGU{zgyzhs_xizxp_zx751vx6}

Decoding them using atbash cipher:

picoCTF{atbash_crack_ac751ec6}
