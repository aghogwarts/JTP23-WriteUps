# keygenme-py

1) In the question there is a python code linked to the question.
2) I then analysed the python code, which uses hashlib to deal with hexadecimal text.
3) A part of the flag has been given. They flag has been split into 3 parts, 2 static parts and 1 dynamic part which we need to decipher.
4) The dynamic part has been stored in an array called key. The array has the dynamic flag in a scrambled order.
5) I then logged into the UDF with the username 'ANDERSON' (which was given) sha256 with hashlib, which contains the key.
6) I then printed each hex character in order as given in the code.
7) Then a bunch of hex characters came up.

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/b8fa766a-38b8-4c86-985b-c39e8ea6c0b1)
   

8) I then attached it with the rest of the flag and I got the final flag.

   # Flag

   picoCTF{1n_7h3_|<3y_of_e584b363}


# ARMssembly 0

1) I first downloaded the file provided in the question and analysed it.
2) On analysis I realised that it's an assembly language which is a lower-level programming language used to represent machine code instructions.
3) Using AI tools and different compilers, I learn that:
   - 'func1' function takes two numbers as arguments and prints the larger number
   - The 'main' function takes two integers as input and then calls the func1 function      with the inputted numbers as parameters and prints the result
4) putting the parameters of the function as 4112417903 and 1169092511, the output would be 4112417903.
5) I then had to convert that to hex as per the question.

   ![image](https://github.com/Snapskillz123/picoCTF/assets/149099858/5bf3b7ae-080b-4b34-a758-d6ccff062485)

   # Flag

   picoCTF{f51e846f}
   

