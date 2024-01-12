#### tunn3l_v1s10n

I downloaded the file and ran it on my linux machine
![Screenshot from 2023-11-04 11-23-30](https://github.com/s4twik/picoctf/assets/147993943/0b0af434-00ef-47e1-8bcf-bd61874041e7)
I didn't knew what header file was so i googled it and found out it's the first line of the hex file of the bmp file
so to run the bmp file i had to edit the header file, so i googled what the header file of the bmp file should look like
and accordingly the changes in offset `0A` and `0E` i didn't understand what to do in `0A` so i put it as 0 and `0E` to 40 in hex for which is 0028
![Uploading Screenshot from 2023-11-04 18-58-57.png…]()

i ran the file it worked but i didn't get the password
![Screenshot from 2023-11-04 19-05-49](https://github.com/s4twik/picoctf/assets/147993943/d2382b44-ad96-4d30-8522-3b21204629d3)
i coldn't figure out the problem, then it clicked that the aspect ratio is a bit off
so i googled what offset are meant for the aspect ratio of the file 
i kept changing the height little by little and after a few attempts i got the flag
![Screenshot from 2023-11-04 19-09-32](https://github.com/s4twik/picoctf/assets/147993943/b1ae2f42-53fd-4ecf-b8f8-ee39caca9c4d)
![Screenshot from 2023-11-04 19-09-57](https://github.com/s4twik/picoctf/assets/147993943/09c88b03-0d2a-4d5a-9ad9-245bb005bff9)
![Screenshot from 2023-11-04 18-21-41](https://github.com/s4twik/picoctf/assets/147993943/5ff0aa80-118c-4c22-a224-a880e92b6ae8)

#### Typical Flag Transfer Protocol
Started by downloading the file, saw it was a pcapng file
I had no clue what that is so i googled what that is, read a bit about. Didn't understand anything
so I googled how to run it, it gave me a software called `Wireshark`. Downloaded it via terminal following : https://www.geeksforgeeks.org/how-to-install-and-use-wireshark-on-ubuntu-linux/
uploaded the file

![image](https://github.com/s4twik/picoctf/assets/147993943/ba040d0d-1950-43a2-827c-db338ad8393e)
I see something called `TFTP Protocol` and reaslised it was the name of the file i just ran. I take it as a clue and google `TFTP Protocol`
it's a file transfer function which doesn't require authentication.
I export all the Networks w/tftp protocol to a folder
i get a 3 bmp files and 2 text files. I go through one of the file. It's Encryted so i run it through dcode.fr
it was encrypted in ROT13 format
![Screenshot from 2023-11-07 17-44-33](https://github.com/s4twik/picoctf/assets/147993943/eb5505b7-b4d8-4a1c-8b27-67e5853563bb)
a/to it should go to plans.txt
![image](https://github.com/s4twik/picoctf/assets/147993943/5aafe5ac-18b6-4be1-a678-2ec0cc9c002d)
check out the photos!!??
didn't make alot of sense so i went to other files which i extracted from deb
![image](https://github.com/s4twik/picoctf/assets/147993943/cb870c68-9308-46e2-91ee-179566f27424)
`steghide`
i read about it. so i have to use it on terminal to extract those bmp file
which i do.
![Screenshot from 2023-11-07 16-36-54](https://github.com/s4twik/picoctf/assets/147993943/0b97e3ff-9174-4ca3-a365-2eec9c9ed7cd)

DONE!

![Screenshot from 2023-11-07 16-38-57](https://github.com/s4twik/picoctf/assets/147993943/aa18f49c-efb2-4a0f-8e91-7d1211e63dfe)

#### Macrohard Weakedge
the best approach to finding files hidden inside other files is binwalk
if we perform binwalk "Forensics is fun.pptm" we'll see there's a bunch of .zip files. we can extract it using binwalk -e "Forensics is fun.pptm"

Now there's _Forensics is fun.pptm.extracted folder which I will navigate using 7zip.

Since there's too many things in 0.zip I decided I might as well automate the search process. I extracted 0.zip then navigated to it in the terminal.

![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/944324da-3ba9-4f26-8704-26263e66cfa1)
i see this file at the end of the list of files
i cat it
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/d46f677f-7884-47e0-89f0-16c65d5b8438)
it seems like an encryption 
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/90037681-fa7d-4a1f-b04d-54f0dcb030b8)
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/3702639d-62fc-4eea-bcd2-8faa99e4ff63)
#### Lookey here
downloaded the file, quite straight forward tbh tried a few variations of grep
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/e2de4bea-260c-4bd9-befa-065dccaf7fec)
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/6f03c016-2fba-4c69-8196-5307fc4862ce)
#### Enhance
downloaded the file looked up the meaning of the file
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/956dd586-5e31-4030-8ba9-b8f82c376e09)
it's vector!
i have worked with vectors before in designing (more of the reason that i should be in cryptonite)

it cat the file to get the strings format of the file i get this!!
it's kind off like an html code

````
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   viewBox="0 0 210 297"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.5 (2060ec1f9f, 2020-04-08)"
   sodipodi:docname="drawing.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.69833333"
     inkscape:cx="400"
     inkscape:cy="538.41159"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1872"
     inkscape:window-height="1016"
     inkscape:window-x="48"
     inkscape:window-y="27"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1">
    <ellipse
       id="path3713"
       cx="106.2122"
       cy="134.47203"
       rx="102.05357"
       ry="99.029755"
       style="stroke-width:0.26458332" />
    <circle
       style="fill:#ffffff;stroke-width:0.26458332"
       id="path3717"
       cx="107.59055"
       cy="132.30211"
       r="3.3341289" />
    <ellipse
       style="fill:#000000;stroke-width:0.26458332"
       id="path3719"
       cx="107.45217"
       cy="132.10078"
       rx="0.027842503"
       ry="0.031820003" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
       x="107.43014"
       y="132.08501"
       id="text3723"><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09824"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3758">o </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10265"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3760">C </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10706"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3762">T </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan></text>
  </g>
</svg>

````
i go through this and all i find is a bunchof x axis and y axis coordinates and the text files present there
on the ends of the code i see { 3 n h 4 n 3 d _ a a b 7 2 9 d d } looks like a flag to me!

so i try picoCTF{3nh4nc3d_aab729dd}
haha! easy
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/b63bc40a-493f-46a9-be12-15a7f9662e4f)
#### Wireshark doo dooo do doo...
opened the file in wireshark, skimmed through the protocol, nothing interesting
opened protocol hierarchy to check if there are any txt files
i find two of them one in html format, i see {} looks like a flag so i copy and run through a decoder i get the flag
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/bd18b2f3-3073-46c9-96da-01c0cba43bb5)
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/4223a564-5806-4684-be7a-465bd32ebab4)

#### advanced-potion-making
i downloaded the file, i opened it in a hex editor, i couldn't figure out the file type so i googled how to do it! i got this article
https://www.hackingarticles.in/forensic-investigation-examining-corrupted-file-extension/
acc to this the file should be png!
i correct the header the file
i thought i was done and i saved my image here, but it wouldn’t open. Going back to my comparison between a random valid PNG and my corrupted file
i realized that the hex values of addresses 0x00000009 to 0x0000000B were incorrect. 
after changing them to 00 00 0D to match my valid PNG, I saved it and opened it to see a red image.
So we’re not done yet. Ugh.
However, when I see red (or really any solid color), I try using stegsolve. I flipped through a bunch of options until Red plane 0, and we have our flag!
I thought I was done and I saved my image here, but it wouldn’t open. Going back to my comparison between a random valid PNG and my corrupted file, I realized that the hex values of addresses 0x00000009 to 0x0000000B were incorrect. After changing them to 00 00 0D to match my valid PNG, I saved it and opened it to see a red image.

So we’re not done yet. Ugh.

However, when I see red (or really any solid color), I try using stegsolve. I flipped through a bunch of options until Red plane 0, and we have our flag!

The hardest part of CTF really is reading the flag. For some reason, I thought the 1 was an l at first!

I thought I was done and I saved my image here, but it wouldn’t open. Going back to my comparison between a random valid PNG and my corrupted file, I realized that the hex values of addresses 0x00000009 to 0x0000000B were incorrect. After changing them to 00 00 0D to match my valid PNG, I saved it and opened it to see a red image.

So we’re not done yet. Ugh.

However, when I see red (or really any solid color), I try using stegsolve. I flipped through a bunch of options until Red plane 0, and we have our flag!

The hardest part of CTF really is reading the flag. For some reason, I thought the 1 was an l at first!

![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/8ee84ca2-9d03-485c-84cb-5b45adaeea7a)

#### So meta
lmao too easy, by meta i go and look at metadata
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/372e76a7-a9be-4678-ba1d-a636c92852c7)
got the flag picoCTF{s0_m3ta_d8944929}
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/695364a1-909b-4749-bdc8-1150477e1eb8)

#### Milkslap
i download the png file
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/21f356bd-9c7c-4d52-9f0b-8c2e9678be01)
from here i tried looking at it's metadata, hexdump and all of the stuff i couldn't find anything so i saw a write up online, it used a commnad called zsteg
and for some reason it's not working on my terminal
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/887cc5d9-5aa7-4900-bdac-ed6d16ab37d4)
so i 

#### hideme
downloaded the file, did all the basic hit and trial!
thought of going with binwalk, worked surprisingly
i find files there, so i extract it, i see a file called "secret" so obviously i open it, then i find one more image 
![flag](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/32c6baf3-fd7e-4548-9973-4043b18bf48f)
i got the flag!
#### Packet Primers
opened the file in wire shark went through a few netwoks found the flag
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/6e818ed8-9345-4a35-8671-ba936daa1737)
![image](https://github.com/aghogwarts/JTP23-WriteUps/assets/147993943/80720640-67c5-4bc5-bdfc-3be7cf5af08d)
####
