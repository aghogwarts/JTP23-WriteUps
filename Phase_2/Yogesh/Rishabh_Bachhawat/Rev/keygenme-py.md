Read through the python code and after going through each method read the check_key() method to get the dynamic part of the licence key.
The username specified was "SCHOFIELD" and the method first checked the static part of the key which was declared in the 
program as **key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"**. Then it hashed the username_trial variable using sha256 and checked if the element of the entered key are equal to the digest in the order 4,5,3,6,2,7,1,8. 
Wrote a python program to hash the username and extract the elements in the given order from it. Appended that as the 8 character long dynamic part and got the final flag.

Flag :picoCTF{1n_7h3_|<3y_of_e584b363}
