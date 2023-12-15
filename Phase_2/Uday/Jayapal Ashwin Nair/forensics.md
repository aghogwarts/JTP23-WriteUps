### tunn3l v1s10n


The first thing i did  was ope `tunn3l_v1s10n` in notepad++ and viewd in hex-editor mode. 

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/5de6b332-3d06-4223-97c8-ed83cc81b5f2)

There's the "42 4d" and 'BM' indicating it's a bamp file. Upon renaming the file to `tunn3l_v1s10n.bmp`i tried viewing it, but the file was corrupted.Upon looking at the hexdump, i came to notcie there's bad written 2 times in the first line. I went through a random bmp file's hexdump and changed the first line wherever bad appeared. 

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/bbb8c048-1099-4b49-a11e-eab0b87902e4)

this is the image:

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/46ad1074-bf0a-4a87-b837-94e1dd14a665)

it does look like it's cropped, so again i refer to wiki for [bmp](https://en.wikipedia.org/wiki/BMP_file_format)  file format to see where i can adjust the size.
in the first image you can see 046e which is the width in hexadecimal and 0132 which is the height in hexadecimal, in decimal the height is 300.
after that i just experimented with different height, for me 820 in decimal worked, which is 0334 in hexadecimal. So i changed `32 01` to `34 03`

final image:

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/1c0e64f1-feae-4e85-9ba5-aa3e7a286dba)

/flag :- picoCTF{qu1t3_a_v13w_2020}*

---

### trivial ftp

the file `tftp.pcapng` is a 'capture file format`, i opened this in Wireshark and viewed the objects available

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/d2599b1b-8455-407a-a62f-194cd0603ec0)

after saving these files, i went through them.
I copied the text from intruction.txt and plan and decoded them using rot13

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/f76ad5bc-8aca-43b5-86e7-4a150c70f85b)

![image](https://github.com/oxo-crab/picoCTF/assets/111520157/e0bd64cf-35cd-4558-9817-cb8c1a21f367)

According to it i am supposed to check the plan file and then it revealed that it used `program.deb` with `DUEDILIGENCE` and i had to check out the photos.
Opening  `program.deb` showed that it had steghide file in it, meaning steghide was used to hide the flag in the pictures with passcode being `DUEDILIGENCE`.

After applying in steghide on three image only `picture3.bmp` responded.

`steghide extract -sf picture3.bmp -p 'DUEDILIGENCE'`

It stored the flag in a txt file which i read.

`cat flag.txt`

*flag :- picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}*

---

### MacroHard WeakEdge

A ppt file is essentially compressed file, after extracting different files from it i get the file `hidden` from the `SlideMaster`folder in `ppt` folder.

the content of this hidden fodler is : "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q"

This seems to be base64 encoded, so after docing it i get the flag.

flag:- picoCTF{D1d_u_kn0w_ppts_r_z1p5}

