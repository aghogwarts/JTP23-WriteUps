# buffer overflow 0

We get a C source code and looking at it, the flag is being printed on a segmentation fault. So basically we have to overflow the length of characters which is **16** to trigger a segmentation fault. When the input becomes too large for the buffer causing it to overflow, it triggers the `sigsegv_handler()` function to give out the flag.
![Screenshot (27)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/9db04ffc-07fd-49c5-acfb-d181efe0726d)


The flag-`picoCTF{ov3rfl0ws_ar3nt_that_bad_9f2364bc}`

# stonks

We get a` vuln.c` file. On running the program, it asks for the API  TOKEN. The `user_buf` variable is printed without any format specifier. This is a format string error. So we can try giving series of `%X` as input for API Token.

![Screenshot (25)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/d96e955c-7f25-40e6-918b-23a5fc6047ce)

We get some hex values which I converted it into **ASCII** text.


![Screenshot (26)](https://github.com/Wixter07/CRYPTONITE-JTP-2/assets/150792650/103f5af7-c245-43e1-b971-5ed6b565bff2)

We can see something written as `picoCTF....`, but the order seems off. On taking a closer look, I could notice that every 4 characters of the flag are reversed. So I tried correcting it manually to get the flag, but it was incorrect. So then I ommited the last two characters which looked odd and  the other reason could be that I haven't encountered such characters in any of the flags for the other problems. The flag after omitting the last two characters turned out to be correct. Though I got the flag, I had to look up the internet as to why those two characters where there in the first place. This is where I learnt about **little endian** and **big endian** from this writeup by [zeyu2001](https://ctf.zeyu2001.com/2021/picoctf/stonks-20).This cleared the doubts I had.


The flag-`picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}`

# CVE-XXXX-XXXX

So we need to find the CVE of the first **RCE**- Remote Code Execution vulnerability in 2021 in the Window Print Spooler Service. I don't know much about what this challenge wante me to do but a simple Google search about the vulnerability would give us the result `CVE-2021-34527`.

The flag- `picoCTF{CVE-2021-34527}`

# two-sum

So the instruction asks for two numbers which meet this condition `n1 > n1 + n2 OR n2 > n1 + n2` and enter the in the C file and try to get the flag. Entering two random values will result in the output `No Overflow`.
![Screenshot (66)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/2bb52dc1-c487-48e5-b697-a0a2eca75ed9)
So this challenge might be somewhat similar to the buffer-overflow challenge, and as expected the hint suggested of a integer flow. An integer overflow happens when the sum of the two positive integer values is more than the maximum value that can be held by an integer data type. So we can overflow it by giving an input whose sum would be greater than the maximum value an integer data type can hold. So I ran the code and gave the input **2147483647** and **2** but it said to `please run this on server`.
![Screenshot (67)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/8e6b0706-52c9-4f59-8af0-2a5013f88e91)
So I ran it and gave the same input to get the flag for the challenge.
![Screenshot (68)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/f2650fe4-9c98-4fe9-a9c5-8c19dac0009f)


The flag- `picoCTF{Tw0_Sum_Interger_Bu773r_0v3rfl0w_e06700c0}`

