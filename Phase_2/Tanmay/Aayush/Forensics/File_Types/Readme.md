# Flag Extraction Challenge Writeup

## The Challenge Journey

Expressing frustration with the Flag Extraction challenge, I encountered a `Flag.pdf` file that turned out to be a shell extractor. After extracting the contents, I encountered numerous layers of compression, ultimately leading to a text file with the following content:

`7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f`
`6630725f3062326375723137795f39353063346665657d0a`


## Decoding the Message

Applying an ASCII converter, I decoded the hexadecimal string and unveiled the hidden message:

`picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}`