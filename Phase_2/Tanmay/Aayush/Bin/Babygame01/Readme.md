# BabyGame01 CTF Writeup

## Navigating the Game

Upon opening the BabyGame01 CTF challenge in IDA, I identified an interesting mechanic. It seemed that `p` immediately led to a win, but the flag was elusive.

## Unveiling the Trick

After some experimentation, I discovered a crucial step. Moving back four positions from the top-leftmost visible position changed the value of the flag to 64. Executing `p` after this manipulation triggered the coveted "You Win!" message, along with the flag.

## The Flag

The flag obtained is: `picoCTF{gamer_m0d3_enabled_ec1f4e25}`


