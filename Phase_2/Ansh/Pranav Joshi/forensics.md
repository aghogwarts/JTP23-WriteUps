## Macrohard weakedge
After going through the given `.pptm`, it was found that it uses macros. A `.pptm` file is a compressed file that contains all the elements of a presentation and is macro-enabled. 
To inspect the different elements, the file was unzipped. This revealed a file named `hidden` whose contents appeared to be encrypted. 

![macrohard_sol_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/d27c25e0-0f26-40dc-87cf-bfe94eb8dda2)
![macrohard_sol_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/4e3b0a5d-bcc7-4251-9f94-b6c2c2f66d9c)


The encryption used couldn't have been rot13 or hexadecimal because it contained digits and letters beyond F. The flag was obtained after decryption with `base64 --decode`.

![macrohard_sol_C](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/09260d33-ee56-4050-9094-dca74e4e75a7)

flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## tunn3l_v1s10n
`cat tunn3l_v1s10n` gave an output that started with BM. Since the first two characters of a file determine its type, therefore it could be inferred that this was a bitmap file. Renamed the file to `tunn3l_v1s10n.bmp`. It still didn't open in Photos. Might have been due to being corrupted. 

When opened in a hex-editor side-by-side with a non-corrupt bitmap file, it was found that some characters in the header had been changed to `BAD` for the given file.

![tunn3l_v1s10n_sol_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/f60ef731-2c49-4034-8e10-d3ae3f639929)

After changing the characters, the file could finally open but it still didn't display the flag. Since the challenge is called tunnel vision, it might have been due to the file's dimensions being changed. After finding the bits in the hexdump that represented dimensions, and after multiple trials, the flag was found when the height was changed to 850 pixels. 

![tunn3l_v1s10n_sol_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/186f8616-35bd-499e-99ce-4098a1a7be4e)


flag: picoCTF{qu1t3_a_v13w_2020}

## Trivial FTP
The wireshark capture file contained many packets from which the objects were exported to a known location.

![tftp_sol_A1](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/df571e52-3288-4749-9c7d-f11051109891)

These objects included three `.bmp` images. The text files included rot13 encoded communication, supposedly between two parties using tftp to communicate.

![tftp_sol_A2](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/266a6f91-02ce-4b0d-948c-efd0d2954fdb)

From the communication, it appears that the flag might have been moved after being hidden in one of the images. However the images themselves don't reveal any flags. There's another way to hide messages in images, called steganography, which can be done using the `steghide` package in Linux. After using its `--extract` command with the passphrase DUEDILIGENCE, the flag was obtained from one of the pictures.

![tftp_sol_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/2b0df395-274c-4523-86e5-20758dd42a76)

flag: picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
