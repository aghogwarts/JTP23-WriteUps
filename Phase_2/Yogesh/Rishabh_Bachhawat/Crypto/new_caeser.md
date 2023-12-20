After reading the code the observations are:


The key is lowercase_alphabet among the first 16 alphabets.
For each character of flag, its ascii value is found and converted to its 8 bit binary equivalent. Then it is broken in to 2, 4 bit binary strings, each is converted to its respective 
integer and appended to the **enc** string.


Then each character is sent to the shift method which finds t1 & t2 by substracting the ascii value of the character and the key from the lowercase offset and (t1+t2 % 16)th element of
the list ALPHABET is the final encoded character.


Now I need to code program to reverse these steps.
