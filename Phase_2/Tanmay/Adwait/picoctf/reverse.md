
# keygenme-py
## PROBLEM:
we are just given a code with no hints.


## BACKGROUND:
first i tried to run the code on a web compiler but i had trouble because of the cryptography module:
![Screenshot from 2023-11-05 19-38-11](https://github.com/adwait3/pico/assets/148553626/66297520-9fb2-41a7-9170-7b6889a476a5)

after this i tried running the code on vs code but had issues with compiling it which i could not rectify or understand.
SO i tried running the code on idle after installing cryptography module via the terminal.

## SOLUTION:
i was successfully able to run the code on idle after a silpe debugging of the try and except block,which gave me the output as
![Screenshot from 2023-11-05 19-19-25](https://github.com/adwait3/pico/assets/148553626/f6ac6edb-4230-4849-adeb-4c87b19dd3d2)

 after this i tried reading the code and realised the answer only concerns the enter_liscence()
functionand rest were redundant, so i focused my attention there,
![Screenshot from 2023-11-05 19-24-08](https://github.com/adwait3/pico/assets/148553626/1bc4f7ba-47bf-4cdd-8e45-0ce3915fffab)

this block tells us that
* the lenth of the key should be equal to the key_full_template_trial which is the concatenated string of key_part_static1_trial + key_part_dynamic1_trial + 
 key_part_static2_trial , so we can guess the length of the key from here which is picoCTF{1n_7h3_|<3y_of_xxxxxxxx} characters long 
* the first part of string is equal to the static portion.
  ow we have to find the second part instead of the xxxxxx portion, loooking at further code we figure out what the next charaxters should be equal to in order to not break from the loop, so i print the statements with which we are checking the key 
![Screenshot from 2023-11-05 19-30-58](https://github.com/adwait3/pico/assets/148553626/82b1fe59-3ef4-4991-8583-e717815b410f)

  this gives me an error stating that Unicode-objects must be encoded before hashing so i look for what this means and fnd out that we are given another username bUsername_trial which is already encoded so i use it while printing and this given me the output and i build up my key using thiese and sure enough the key is right and im able to access the full verion of the calculator.
  ![Screenshot from 2023-11-05 19-35-50](https://github.com/adwait3/pico/assets/148553626/48585f5e-a6ff-4ca7-9bc7-5aad7ac8a69a)

  ## KEY;
  picoCTF{1n_7h3_|<3y_of_0d208392}


# GDB baby step 1
## PROBLEM:
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Disassemble this.

## SOLUTION:
the problem statement in this was pretty much self explanitory and i did exactly everything it specified .
first i learned about gdb and how to use it to dissassemble the file 
after using the help 
![Screenshot from 2023-12-16 01-22-40](https://github.com/adwait3/pico/assets/148553626/921b2f86-59b7-4ce4-8bfe-ec197ff3d8d2)
then i used help all and found 
![Screenshot from 2023-12-16 01-25-00](https://github.com/adwait3/pico/assets/148553626/b1097e4b-abdb-426d-8546-9b8557099f9e)
so i used this command to dissasemble the main and found the eax register

![Screenshot from 2023-12-16 01-28-09](https://github.com/adwait3/pico/assets/148553626/4920ea67-c4a3-44c0-b4d9-3ce5d690ee14)

i converted this hexadecimal to integer and got 549698

![Screenshot from 2023-12-16 01-29-44](https://github.com/adwait3/pico/assets/148553626/68c92d46-fa43-4340-a1c9-0365b281c2d4)
and got the flag

  ## FLAG
  picoCTF{549698}

# ARMssembly 0
## PROBLEM:
What integer does this program print with arguments 4134207980 and 950176538? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## SOLUTION:
 after downloading the file i knew it was assembly language so i tried to compile it using as and gcc commands but i got errors which i couldnt understand completely but might be because of architecture as my machine was 64bit processor and it required armv8 .
 ![Screenshot from 2023-12-16 13-44-02](https://github.com/adwait3/pico/assets/148553626/f36acc76-7ce2-4815-a0f6-0032f6da10ad)
![Screenshot from 2023-12-16 13-44-12](https://github.com/adwait3/pico/assets/148553626/5c1f9180-8aa2-4e09-a1b9-fd60d281467b)
so i decided to search for web compilers and found one 
![Screenshot from 2023-12-16 13-46-31](https://github.com/adwait3/pico/assets/148553626/ff737035-3f6b-48a5-97cd-057b02c5a0ea)
but this also gave me errors which i could not understand so i tried to open the code and try to undertrand what it does to see if i can compute the output myself.
i understood ldr is for load and str for storing the numbers which were the specified bytes long and sp meant a stack and next to it is the amount of bytes which we want to allocate by subtracting them from the top of the stack. 
In our case x0 would be our register and we would be cutting it into two parts w0 and w19 wo would be the lower 32 bits and w19 the others now we load our first value in the form of a string (  ldr	x0, [x0]) and convert it to  integer (bl	atoi )  now we move our first value to w19 and add 16 more bytes to our register (add	x0, x0, 16) 
now we get the second argument and concert it to integer noe both the values are stored in the register the first one in the beginning ie bottom of the stack and second one above it , now we call the function1 which puts our values from the register to the stack and interchanges them so w1 becomes the larger value and w0 the shorter and now we compare them which calls the .l2 of w1 in smaller but w1 is larger so the programs continues and makes the w0 also equal to sp 12 which is our larger value so now both the w1 and w0 are larger values.
 now we move to .l3 which dosent do anything and go back to main where .Lco is called(adrp	x0, .LC0) in which we print the result and conidering both the values in our register are now larger value im guessing it must be the larger value (4134207980) so i try converting it to the hex and et the flag.
 
## FLAG
picoCTF{F66B01EC}
