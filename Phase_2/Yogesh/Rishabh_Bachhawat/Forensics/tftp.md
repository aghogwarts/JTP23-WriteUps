Read the first packet and found a **instructions.txt** file. Used https://www.cachesleuth.com/multidecoder/ and found decoded text in ROT13:
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN

So maybe there are more such files, but there are too many packets to manually inspect. Using this thread https://www.reddit.com/r/wireshark/comments/6ndvpq/extract_tftp_file_from_pcapng/ found and extracted the other files.

![Screenshot 2023-11-15 142107](https://github.com/CoderZonora/picoCTF/assets/140229408/7b85b072-c0e5-4772-a39b-34617f899a50)

The plan file was similarly ROT-13 encoded.


Decoded to: IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS

Next file was program.deb, so looked into the file and found **steghide**, which meant the flag must in one of the 3 photos, but steghide needs a password to extract the text.
Pass: DUEDILIGENCE

Used succesfully on picture3.bmp


flag:picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
