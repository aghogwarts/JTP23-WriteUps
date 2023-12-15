### Description

Figure out how they moved the flag.

### Approach

[pcapng](https://pcapng.com/) is a capture file format. 

To extract the files use Wireshark:

File > Export Objects > TFTP

which shows all the files recorded in the packet capture
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/7218600d-2fc4-44dc-ac2c-c3069e6a8d80)

Click "Save All" to save them.

Analyze each one of them.

Open [instructions.txt](./instructions.txt): `cat instructions`

```text
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```

It's look like [ROT13](https://en.wikipedia.org/wiki/ROT13)

```code
echo "GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
`TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`

If we add spaces we can see the hint

`TFTP DO ESNTENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER.FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN`

Open [plan](./plan): `cat plan`
`VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF`

Once again, it is encrypted using ROT13. Here's the decrypted message

`IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS`

with some spaces:

`I USED THE PROGRAM AND HID IT WITH-DUEDILIGENCE.CHECK OUT THE PHOTOS`

## Pictures

![picture1](./picture1.bmp)
![picture2](https://github.com/Harsha-creates/PicoCTF/assets/68886253/877c83cf-ffe3-435d-8e6b-f52a12e9a0e1)
![picture2](./picture3.bmp)

Now,Install the [program](./program) using debian package manager `dpkg` : 
`sudo dpkg -i program.deb`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/a2e55381-342d-4977-8f36-39b8468c68c6)

Let see how to use Steghide
![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/49e4a721-100f-48bd-ac09-cfb5bfb9812c)

Lets check the each picture using Steghide with password `DUEDILIGENCE` a hint from plan

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/2869867d-bd7c-4c31-b481-ffe70b6fd460)

There is a [flag](./flag.txt) embedded in [picture3](./picture3.bmp)

Extract The embedded files: `steghide extract -sf picture3.bmp`

`cat flag.txt`

**Flag:** picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
