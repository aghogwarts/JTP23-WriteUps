# Macrohard Weakedge 

After attempting scavenger hunt i know the reality of pptm files now. They are extractable !!!!

## Solution Steps:

1. **PPT Extraction:**
   - Discovered that PPT files are essentially zipped archives.
   - Extracted the PPTM file and found a `vbaproject.bin` file.

2. **VBA Analysis:**
   - Extracted the VBA content using 7zip, revealing a VBA folder with three files.
   - Hex dumped `Module1` but found that the flag was not present there.

3. **Hidden File Discovery:**
   - Explored further within the extracted PPT.
   - Discovered a hidden file within the `slideMasters` directory, marked with the 'hidden' attribute.

4. **Base64 Decryption:**
   - Extracted the hidden file, revealing base64-encoded text in the filename.
   - Decrypted the base64 text, resulting in the flag: `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`.

## Flag
The flag for this level is: `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`