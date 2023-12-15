We know that rsa formula is:
c=m^e mod n
So to find m, we take any random integer k, so m will be:
m=( k*n+c)^1/e
Hence we write the following python program which finds all the possible m values and prints the one which has the flag

![rsa](https://github.com/poorvi1910/Cryptonite/assets/146640913/aa913b9f-8cad-4022-a7c5-f37504a4fac3)

Running the code we get : picoCTF{n33d_a_lArg3r_e_d0cd6eae}
