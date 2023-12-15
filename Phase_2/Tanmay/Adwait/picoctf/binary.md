
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



  # babygame01
  ## problem
  Get the flag and reach the exit.
Welcome to BabyGame! Navigate around the map and see what you can find! The game is available to download here. There is no source available, so you'll have to figure your way around the map. You can connect with it using nc saturn.picoctf.net 50533.


## SOLUTION
i ran the instance and opened the game and first just tried random movements and figured out u can move multiple steps at a time.
i also tried ls command to see if we can run commands from the game terminal but saw that the game character changed to s i tried it again and again and figured out you can change your chracater to anything by typyng l and the character you want
![Screenshot from 2023-12-15 23-54-29](https://github.com/adwait3/pico/assets/148553626/ce700eaa-3f0f-44ed-8457-ec9a8c7add4e)
i tried going to the x to finish but it just showed "you win" so i tried exploring the map and figured out you can off screen by going up or down but right left just puts you in the next or previous line. after a lot of efforts i couldnt figure anything out so decided to check how to read the source code of the game file which was a executable file and came across the software GHIDRA, after figuring out the basics i opened my file in ghidra and decided to look into the main, i saw several functions and going through the player movement function i found 

![Screenshot from 2023-12-15 23-59-58](https://github.com/adwait3/pico/assets/148553626/ef8fd0fd-285f-40c4-bfe7-ce6251661890)

this showed what i found earlier that l can be used to change player and wasd for the movements another input p was there so i tried it and found it is used to iterate to the end and solve the game which can be really handy to speed things up now i just had to find the flag.
and i found
![Screenshot from 2023-12-16 00-33-10](https://github.com/adwait3/pico/assets/148553626/4bfc1461-241e-4366-b8bc-a78229ca9888)
i figured local_aa4 must be our flag in the game and w just need to make it anything except null to get the answer.
after going around the map and spamming different commands i found that going back the first top left space by 4 or 5 steps gives us two different values for flag which was the ascii value of aur player character.
![Screenshot from 2023-12-16 00-42-57](https://github.com/adwait3/pico/assets/148553626/585f018e-2b8f-43b5-8b0e-0ec078fcf95f)
then after that i typed p to complete the game which gave me the flag.

![Screenshot from 2023-12-16 00-43-24](https://github.com/adwait3/pico/assets/148553626/a779becb-5bee-432b-8569-e5c07cdb919c)

## FLAG
picoCTF{gamer_m0d3_enabled_f4f6ad7d}

 # buffer overflow 0
  ## problem
  Smash the stack
Let's start off simple, can you overflow the correct buffer? The program is available here. You can view source here. And connect with it using:
nc saturn.picoctf.net 64712
hints
* How can you trigger the flag to print?
* If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
* Run man gets and read the BUGS section. How many characters can the program really read?

## SOLUTION
first i ran the program and got

![Screenshot from 2023-12-16 00-52-55](https://github.com/adwait3/pico/assets/148553626/86f3c5b0-169c-4121-b09a-c75be5bd59ea)

then according to the second hint i read the man gets and found out it can be used to read very very long strings and thats why shouldnt be used and fgets shoulf be used instead.
![Screenshot from 2023-12-16 00-59-38](https://github.com/adwait3/pico/assets/148553626/3aba529d-0809-4ed6-bc38-3c19b944820c)
then i looked at the source code and found that gets had been used there

![Screenshot from 2023-12-16 01-02-12](https://github.com/adwait3/pico/assets/148553626/962cb1e7-0846-476f-9c43-09f76ccddedf)
gets had been used to take the input of a buf1 which was of size 100
looking at the hints and question name i thought this might be related to overloading the buffer so i treid to run the program again witha long string and sure enough it gave me the answer
![Screenshot from 2023-12-16 01-06-00](https://github.com/adwait3/pico/assets/148553626/76e039ca-0c56-4d18-9a95-082d8ee8f4fc)


## FLAG
picoCTF{ov3rfl0ws_ar3nt_that_bad_9f2364bc}
