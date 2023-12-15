Read about RSA and how it is vulnerable for low 'e' value. Tried finding the eth root of c+n with high precision but that did not give the flag.
Had to write a script to find the i where c+i*n gives the exact root. Used the iroot() method of gmpy2.
Then decoded the integer to proper stiring. 


Also learnt about modular equivalence : https://math.stackexchange.com/questions/535053/what-is-the-equal-sign-with-3-lines-mean-in-wilsons-theorem


Flag:picoCTF{e_sh0u1d_b3_lArg3r_60ef2420}
