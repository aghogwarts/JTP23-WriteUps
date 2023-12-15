
  # STOONKS
  ## problem
  I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! vuln.c nc mercury.picoctf.net 33411
  * hint = Okay, maybe I'd believe you if you find my API key.

## SOLUTION
 first after downloading the code i tried running it on cs code on my machine which gave me an error in the following :
 ![Screenshot from 2023-11-08 10-45-22](https://github.com/adwait3/pico/assets/148553626/2e1d9cef-c3e7-4bda-8fa7-5d00162261c5)
 as the format (data type ) of user_buf was not defined in the code.
 after studying a bit about printf and how it works i got to know that it prints what we want from a stack which is known as the buffer eg in printf ("%s", a)
 %s is our format in which we want the output and a is like an address in the buffer which we want in that particular format, in our code we only have a user_buf and if that is not present in the buffer and format is not defined , the printf statement just starts giving output of whatver is in the stack(buffer), we can specify the format of this output buy using format specifiers , in this problem i wanted all of the stuff whihc is in the stack since we dont know what format we are looking for so we use %x (hex) as the specifier as 
 ![Screenshot from 2023-11-08 11-44-53](https://github.com/adwait3/pico/assets/148553626/2cec20ba-60d0-47ec-a3d2-ef4f9b02717b)

which gives us the output now we convert it into ascii using cyberchef
![Screenshot from 2023-11-08 11-54-21](https://github.com/adwait3/pico/assets/148553626/37cc6f08-cc8d-4142-950d-f9cb2d7fe70c)
in this i was able to find something which looked like my flag but it was jumbled so i truncated the excess hex to just get my flag 
![Screenshot from 2023-11-08 11-55-51](https://github.com/adwait3/pico/assets/148553626/2c16e2a2-e480-42cd-9f9d-e345c14b2f26)
now after reading a bit more abt how stuff is stored ina buffer i found i out that a maximim of 32 bits are stored in every slot of the stack and each ascii value is 8 bits that means 4 characters and that made sence as in the jumbled flag i could figure out that every group of 4 characters was written backwards 
so i manually broke the jumbled flag into parts of 4 and reversed each of them  and conctanated them together which gave me 

## FLAG
picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}


