Read the vulc.c code. The interesting part was the buy_stonks() function because that is where the flag gets loaded and where input is taken.
Tried to send like *f,*p or other things but could not get the flag to print. I even tried to get a buffer_overflow by sending 350 characters but to no avail.

Had to see its solution after trying everything.
Learnt about endian-ness and how to print from stack.

Flag: picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}
