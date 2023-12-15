
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

