# CaaS

So we get a link and an `index.js` file which prints the input that's written in the curly braces portion of the URL. The `index.js` file reveals that it prints whatever's written in the curlybraces, but there's also a `$` symbol before the braces which means we can try putting some commands before the braces. So I tried using ls command with a message as `https://caas.mars.picoctf.net/cowsay/afk;ls `to get the below result.
![Screenshot (3)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/dee43c0e-d2f7-46ec-8f1d-83c3cd035252)
So as expected, the command lists out the files in the cowsay directory and the flag seems to be stored in the falg.txt folder. So we'll try using cat with the file name as `https://caas.mars.picoctf.net/cowsay/afk; cat falg.txt`.
![Screenshot (4)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/8c2d7ba9-7e51-42c7-9292-aec91f992b41)
The flag- `picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`  



# Fobidden paths

It seems that we are in some directory with 3 txt files. The problem states that we can't specify absolute file paths and if we do so we get an error message saying "Not Authorized". I looked up the internet to learn about absolute and relative paths. The files are stored in `/usr/share/nginx/html/` . So maybe we can read out the `flag.txt` file by going back 4 directories to the root directory. That we can do by entering the command `../../../../flag.txt`. 
![Screenshot (7)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/3b741418-2da6-458e-ab16-3aeaf52c79cb)
The flag-`picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}`

# Local authority

The page asks for username and password as login credentials. Inspecting the page doesn't help but upon inspecting the login failure page, we can see a `secure.js` file which contains the correct login credential. We use that to get the flag.
![Screenshot (5)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/8303e8f2-9f6a-47cd-ad05-b91e47324d85)
The flag- `picoCTF{j5_15_7r4n5p4r3n7_05df90c8}`


# Insp3ct0r
 
So went to the link as instructed. The page said `Inspect Me`. So I inspected the page, and it contained 3 files, namely `9670/`, `myjs.js`  and `mycss.css`. Looking through all three files, they all had a part of the flag as followed:-
![Screenshot (52)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/af59097f-2df5-479e-89bf-1ee99479fc90)
![Screenshot (53)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/3440c21e-b9df-464e-9ccb-affca7fcc20e)
![Screenshot (54)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/95cef894-d302-4154-9814-a4fcecf7afb5)
So concatenating the parts, we get the flag.

 The flag- `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}`

 # Some Aseembly Required 1

 So going to the link, the page wants us to enter a flag, and if the flag input is wrong, it shows an "incorrect" message. So on inspecting the page and going to the source file `G82XCw5CX3.js`, the `const__0x402c` holds what it looks like a file path named `./JIFxzHyW8W`.
 ![Screenshot (63)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/dfe4b7e8-850d-412b-be99-f58c8513b819)
 So I tried going to that the path using `view-source:mercury.picoctf.net:37669/JIFxzHyW8W` which downloaded a file named `JIFxzHyW8W`. I opened it on Notepad++ which gave out the flag for the challenge.
 ![Screenshot (62)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/4b03afe9-5a09-4ed4-9029-574f74235deb)

 The flag- `picoCTF{a8bae10f4d9544110222c2d639dc6de6}`

 # where are the robots

 As hinted `What part of the website could tell you where the creator doesn't want you to look?`. I remember learning about `robots.txt` file from a video resource linked in the TP-2 instruction pdf. So basically a `robots.txt` file tells engine crawlers about which URL's the crawlers can access on the site. So I opened the robots.txt file by (https://jupiter.challenges.picoctf.org/problem/56830/robots.txt) 
 ![Screenshot (56)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/dc84e943-44af-45d9-93ea-0b7fde90d002)
 It shows that it disallows going to `/1bb4c.html`. So I pasted the HTML extension as (https://jupiter.challenges.picoctf.org/problem/56830//1bb4c.html) to get the flag.
 ![Screenshot (64)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/0874968a-8acf-491a-8ab9-06cec16f003e)

 The flag- `picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}`
