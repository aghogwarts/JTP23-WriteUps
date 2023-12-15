# tunn3l v1s10n
We are provided with a corrupted file, after looking through stuff i found the the first letters being BM signified it to be .bmp file.
Opening it up on a hexeditor like hexed.it, we found some corrupted characters in as BAD in the hex format, the way i did was comparing it to another bitmap sample file. Replacing those corrupted spots with valid values.

Then opening the file showed a small image with text 'notaflag{sorry}', for a while a did not understand what do to but seeing as the title is called tunnel vision and how small of a image we had, it probably had to do with height and width of the image.

Changing the values of height and width in the bitmap header from `32` `01` to `40` `03` reveals the full image and the flag, make sure to not put the values too big else file will show corrupted.

Flag: 'picoCTF{qu1t3_a_v13w_2020}'

