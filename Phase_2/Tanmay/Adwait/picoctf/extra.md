# pico
this is my repository for writeups of the pico ctf challanges problems for particular domains are in their respective branches which can be seen through code and this contains writups for extra problems


# PYTHON WRANGLING
## PROBLEM:
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
## solution:
in thie problem we were given three files out of which one was a python file ,so first i tried to run it on a web compiler but it led to errors, i then looked at the hints given which were:
* Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py
* $ man python
These made me realise that this problem must require terminal and not a python compiler, after looking at the man page i tried running the python file through the terminal in shwll using python3. and it gave me an output reguarding the commands usage.

![Screenshot from 2023-11-04 13-11-59](https://github.com/adwait3/pico/assets/148553626/a3683bcf-16c5-462e-8294-6e1d30c4db65)

I followed it and used -d flag (for decode) with our file and then provided the password which gave me the flag.
## FLAG
picoCTF{4p0110_1n_7h3_h0us3_6008014f}






