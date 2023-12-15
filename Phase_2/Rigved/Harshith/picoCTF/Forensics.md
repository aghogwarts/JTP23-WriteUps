# tunn3l v1s10n

I opened the file on hexed.it website. The header states that it's a Bitmap file. So I changed the file extension to `.bmp` and tried opening it but it gave an error stating that the file format is no supported. So it seems the file has been corrupted. We can compare the file in hand with the actual bmp file format. I reffered to the bmp size format on [Wikipedia](https://en.wikipedia.org/wiki/BMP_file_format) and compared the hex values. The hex values  in the header have been replaced with some letters as `BA D0`. I didn't know how to  go beyond this point so I had to look up for the solution. I watched a video from [Martin Carlisle](https://www.youtube.com/watch?v=X4kJiQdDn7M) where he epxlains what hex values can be used to correct the file. After making the corrections, I opened the `.bmp` file and the image said **notflag{sorry}**. So had to go back to the video again to learn that the bits for the image dimensions were altered. Upon trying some combinations, I got the flag. Images below show the corrected hex values and the flag.
![Screenshot (11)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/fa9a684e-becf-48f7-bab9-7eb4d6841d9a)
![Screenshot (10)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/32588c1d-ce47-4754-a91e-f2f16ec1f60f)

The flag-`picoCTF{qu1t3_a_v13w_2020}`

# Trivial Flag Transfer Protocol

So TFTP is a simple protocol for exchanging files between to IP machines. I opened the file on wireshark and exported the TFTP object list. I saved the files present in it on my PC. The `instructions.txt` had bunch of letters which seems to be encoded in some format. I could think of two basic one being **base64** and **rot13**. On decrypting using an online **rot13** decrypter, I got a message saying to check the `plan` file. The `plan` file had a bunch of characters which I decrypted using the same **rot13** decrypter. It said to check out the photos. It could be possible that some information was hidden in the images as it said in the hints. I tried searching for the flag in an hex editor but that didn't workout. So I looked for ways to hiding information in images and then I came to learn about Steganography. I then had to install `steghide` command on my wsl through `sudo apt install steghide -y`. After I looked for a way to use the steghide command through `man steghide`, I tried `steghide extract -sf picture1.bmp`. It oppened a (Enter passphrase:) promt. Seems that it requires some password. Ok the `plan` file said that it hid it with` DUEDILIGENCE`. This could possibly be the passphrase. It got "couldn't extract any data" message with the first 2 image files but got a flag.txt file which I read out what's stored in it using cat command. I got the flag that way.
![Screenshot (13)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/98976330-0d14-4da5-9a6f-08a17134b3b7)
The flag-`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`
# MacroHard WeakEdge

Got a `Forensics is fun.pptm` file. So I thought of looking for macros in the edit section of the ppt but the ppt wasn't opening. I had to look for some help online. This is where I learnt that we can unzip ppts. So I tried to unzip it on Windows but didn't work. So I copied the `.pptm` file into my wsl user directory and unzipped the ppt into a another file using the command `unzip Forensics\ is\ fun.pptm -d macro`. Had to be extra careful with the spaces in the file path. The I tried navigating through that file and found some set of characters in the hidden file.
![Screenshot (14)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/cf99b0e7-c54d-4278-90c7-73a0f8bab08e)
So the letters seem to be encrypted. Again the two basic encryption methods of **base64** and **rot13**  came to my mind. **rot13** decrypter didn't give me anything useful but **base64** decrypter did.
![Screenshot (15)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/9fdf2917-5b68-48b4-9b22-43498dfd758b)

The flag-`picoCTF{D1d_u_kn0w_ppts_r_z1p5}`

# information

We get a `cat.jpg` which when opened on an hex editor tool gives out two decoded text which has likely been encrypted using some method.
![Screenshot (57)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/d433cea2-f1c7-4b1c-bda2-bb859ed03512).
I didn't get anything useful trying various decryption methods on the first decoded text but when I tried for the second one with Base64 decode, I got the flag.
![Screenshot (58)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/66b9a426-0d66-470f-80c5-b76ba08fc1e5)

The flag- `picoCTF{the_m3tadata_1s_modified}`

# Glory of the Garden

Opened the `garden.jpg` file on a hex editor tool and got the flag.

![Screenshot (59)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/0beb8cc5-078a-4789-a07a-527236645fc6)

The flag- `picoCTF{more_than_m33ts_the_3y33dd2eEF5}`

# Enchance!

On opening the `drawing.flag.svg` file on a hex editor tool, didn't get anything useful. So I tried searching for strings in the image by using `strings drawing.flag.svg` and found that the flag was broken into two parts which when concatenated gives us the flag. Basic steganography it seems.
![Screenshot (60)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/6bd60bca-6368-40ab-802b-7898b7171dd5)

 The flag- `picoCTF{3nh4nc3d_aab729dd}`


