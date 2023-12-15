# GDB Baby Step 1

I had the most fun learning reverse engineering and the use of GDB seemed fun so this problem should be easy I guess. So we have to look for the hexadecimal value stored in the eax register. The porblem gives us a `dbugger0_a` file which is executable. I opened the file on gdb and looked for information all the functions. Well GDB disassbembly by default is set to AT&T syntax, I changed it to intel so as it's more familiar and easy to read. Then I disassembled main. The eax register stored the value `0×86342`. 
![Screenshot (19)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/68c4fe06-272d-4e2c-8c94-8f0223745829)

As per the problem, the flag should be closed in decimal so I converted the hexadecimal value to decimal and got the flag.
![Screenshot (20)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/0c2c8be8-1541-4d14-86bd-13284a4133e8)

The flag-`picoCTF{549698}`

# ARMssembly 0

I learnt a bit of Assembly Language but I wasn't able to read ARM Assembly. So I resorted to looking at the solution from [Martin Carlisle](https://www.youtube.com/watch?v=BMvda3d0dt8) learnt how it works. Basically the code was printing the number the larger number `w0`. The flag could be obtained by converting the decimal number to hexadecimal.
![Screenshot (22)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/400275a7-ffce-4d74-ba7a-e99b19a74c49)

The flag-`picoCTF{E5C69CD8}`

# keygenme-py

So looking at the python file, It is likely that if the key check trial return true, it will lead us to the flag. We already have a portion of the flag and the last 8 characters in it are to be found. The key can be reverse engineered from the check_key function and the below code can give us the the last 8 characters of the flag.
![Screenshot (18)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/251a7b19-9756-46e4-b179-c062fb71be4c)

The flag- `picoCTF{1n_7h3_|<3y_of_e584b363}`

# crackme-py

We get a python file with a code which has ROT47 encoded secret of their biggest client. 
![Screenshot (28)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/afae4de7-b139-4be5-be58-4706ece74683)
The encrypted text is `bezos_cc_secret = "A:4@r%uLM-^M0c0AbcM-MFE0d_a3hgc3N"` and can be decoded using ROT47 decrypter on CyberChef to get the flag.

The flag- `picoCTF{1|\/|_4_p34|\|ut_502b984b}`

# vault-door-training

This was an easy one as the flag was present in the source code of the training vault.
![Screenshot (32)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/39f02956-411e-494f-9a15-c49ec5b4afb1)

The flag- `picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b}`

# speeds and feeds

Connected to `nc mercury.picoctf.net 20301` as instructed. It returned set of line which looked like some sort of code. Upon looking at the hint `What language does a CNC machine use?`, I searched for it and learnt that CNC machine used G-code. Going through the wikipedia page for [G-code](https://en.wikipedia.org/wiki/G-code), I learnt about the `.gcode` extension. So I flushed the code in to a `pico.gcode` file as such.
![Screenshot (30)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/5987195c-a900-411a-8b59-a5537eb87554)
Didn't have any apps to view GCode so looked for an online viewer and came across [NC VIEWER](https://ncviewer.com/). Uploaded the file over there and ran the code to get the flag.
![Screenshot (31)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/7cf21f7d-cba1-4705-863f-6c4dadad0b8c)

The flag- `picoCTF{num3r1cal_c0ntr0l_68a8fe29}`

# vault-door-1

Got a java file. The case this time is that we don't have a string as the key to check whether the password is correct or not in the `checkPassword` function. Instead, we have the string crumbled in pieces with `charAt()` method. What this method does is that it retreives the character from the position give inside the braces from a string. In our case, we have 32 characters (0 to 31) as such.
![Screenshot (33)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/ae82c3ce-7d67-4ecc-82b2-41dd0c716bfa)
We can rearrange the chracters manually to get the flag or write a code for it. I did it manually.

The flag- `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}`

# file-run1

So we have a `run` file in hand which when executed gives us the flag.
![Screenshot (35)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/63bca4e6-3ec7-4ace-90bc-a853dbc63e79)

The flag- `picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}`

# file-run2

Same as before, we get a `run` file, but this time we don't get the flag when the file is executed. As said in the instruction to try to run the file with input `"Hello!"`. So we do just as it says and write `./run Hello!` to get the flag.
![Screenshot (72)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/1bafd48c-312c-4495-8e85-5f0969dde579)

The flag- `picoCTF{F1r57_4rgum3n7_96f2195f}`

# Safe Opener

Looking through the java code, It easily strikes the eye that there is a Base64 encoded string which when decoded will fetch us the flag.
![Screenshot (37)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/0048e1b2-7bfe-4545-9418-6b26b4368006)
So ran the encoded string `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz` on CyberChef with Base64 decryption to get the flag.

The flag- `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`

# patchme.py

We get a python file. Seems like we get the flag after we run the program and give the correct input for the password. So going through the check condition for the correct user input for password which is broken into fragments, as hinted by the challenge name, joining them together will give us the correct password.
![Screenshot (61)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/b5a0851e-0334-4d49-9b4d-88eaf160bf20)
So ran the program and gave the correct password as input to get the flag.
![Screenshot (38)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/5df2ab95-efc3-416c-8078-33bb48f08d6a)

The flag- `picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}`

# unpackme.py

We get a python file. So we have string in `key_str` which is Base64 encoded and uses fernet cryptography library. I read about Fernet but wasn't able to understand much about it so went through a video tutorial for this challenge from [Almond Force](https://www.youtube.com/watch?v=E2ySnQFMgDg&t=173s) and understood how it's been done. So basically, instead of executing `plain.decode()`, we can just modify the program and print it to get the flag as such.
![Screenshot (39)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/80a37e99-67dd-4b6d-ac3f-5ef78cf0d4f8)
![Screenshot (40)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/dbbec3db-c5c1-4557-a68d-2e80d3018354)

The flag- `picoCTF{175_chr157m45_cd82f94c}`

# Reverse

So we get a file which I opened on GHIDRA debugger. The decompiler gives a rough code of the C compiler which could possibly be innacurate, but it thankfully gave out the flag.
![Screenshot (41)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/ed17c529-a1bc-4f09-928a-a7a30d638c0f)

The flag- `picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}`

# GDB Test Drive

So we get a binary file which it instructed to open on GDB. So I ran it on GDB and gave all the inputs as given in the instructions to bring out the output.

![Screenshot (71)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/da7853cd-904b-43c2-bc24-efd3a6b9efaf)

The flag- `picoCTF{d3bugg3r_dr1v3_72bd8355}`

# Safe Opener 2

We get a `SafeOpener.class` file. I ran it on GHIDRA and was looking around for anything that resembled to be part of the flag but eventually got the whole flag.

![Screenshot (70)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/1f547ee8-8b7f-43e0-9ea0-4d2bfc162cbe)

The flag- `picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}`

# Bit-O-Asm

We ge ta disassembler dump text file and on reading the file, value `0x30` is moved in to the `eax` register. So converting `0x30` into decimal and closing it in the flag syntax, I completed this challenge.

The flag- `picoCTF{48}`

# Fresh Java

So we get a `KeygenMe.class` java file which when decompiled using an online java decompiler will give the code below.

` import java.util.Scanner;

public class KeygenMe {
   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.println("Enter key:");
      String var2 = var1.nextLine();
      if (var2.length() != 34) {
         System.out.println("Invalid key");
      } else if (var2.charAt(33) != '}') {
         System.out.println("Invalid key");
      } else if (var2.charAt(32) != 'e') {
         System.out.println("Invalid key");
      } else if (var2.charAt(31) != 'b') {
         System.out.println("Invalid key");
      } else if (var2.charAt(30) != '6') {
         System.out.println("Invalid key");
      } else if (var2.charAt(29) != 'a') {
         System.out.println("Invalid key");
      } else if (var2.charAt(28) != '2') {
         System.out.println("Invalid key");
      } else if (var2.charAt(27) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(26) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(25) != '9') {
         System.out.println("Invalid key");
      } else if (var2.charAt(24) != '_') {
         System.out.println("Invalid key");
      } else if (var2.charAt(23) != 'd') {
         System.out.println("Invalid key");
      } else if (var2.charAt(22) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(21) != 'r') {
         System.out.println("Invalid key");
      } else if (var2.charAt(20) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(19) != 'u') {
         System.out.println("Invalid key");
      } else if (var2.charAt(18) != 'q') {
         System.out.println("Invalid key");
      } else if (var2.charAt(17) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(16) != 'r') {
         System.out.println("Invalid key");
      } else if (var2.charAt(15) != '_') {
         System.out.println("Invalid key");
      } else if (var2.charAt(14) != 'g') {
         System.out.println("Invalid key");
      } else if (var2.charAt(13) != 'n') {
         System.out.println("Invalid key");
      } else if (var2.charAt(12) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(11) != 'l') {
         System.out.println("Invalid key");
      } else if (var2.charAt(10) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(9) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(8) != '7') {
         System.out.println("Invalid key");
      } else if (var2.charAt(7) != '{') {
         System.out.println("Invalid key");
      } else if (var2.charAt(6) != 'F') {
         System.out.println("Invalid key");
      } else if (var2.charAt(5) != 'T') {
         System.out.println("Invalid key");
      } else if (var2.charAt(4) != 'C') {
         System.out.println("Invalid key");
      } else if (var2.charAt(3) != 'o') {
         System.out.println("Invalid key");
      } else if (var2.charAt(2) != 'c') {
         System.out.println("Invalid key");
      } else if (var2.charAt(1) != 'i') {
         System.out.println("Invalid key");
      } else if (var2.charAt(0) != 'p') {
         System.out.println("Invalid key");
      } else {
         System.out.println("Valid key");
      }
   }
}`

When the characters are read backwards and then concatenated, we obtain the flag.

The flag- `picoCTF{700l1ng_r3qu1r3d_9332a6be}`







