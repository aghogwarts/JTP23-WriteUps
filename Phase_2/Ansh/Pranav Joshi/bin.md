## stonks
In the code fragment below, it can be seen that no format specifier has been given to the printf() function, so it will read format specifiers if they are passed as input, while the second argument will remain empty. The '%x' format will start printing hex values of the contents of the stack. After trying a lot of %x's and converting the hex string to ASCII, the flag can be found. However, it is written in Little Endian.

![stonks_sol_A](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/edef7ea4-eac9-4384-9e8b-f8176a435c00)

![stonks_sol_B](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/b9c2ecec-3be4-48f6-80ca-e79d4bab337e)

![stonks_sol_C](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/664b25c0-360f-49e3-a883-dbc64a3a7727)



flag: picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}


## babygame 01



## buffer overflow 0
The given code uses the gets function which is prone to buffer overflow. When the input contains a string that is larger than the buffer size, it cause buffer overflow. This triggers the flag to print.

flag: picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}

![buffer_overflow_0_sol](https://github.com/mizar-0/Cryptonite-JTP-2/assets/76529146/41f4073a-b45f-40ed-bcf0-9afd506cc2e2)
