# Memory Corruption

So we get a game which wants us to decorate the Christmas Tree with a star which we can buy. To change our name, we use the money generated from the computer which gives us a dollar everytime we press space bar. The computer breaks after we earn $16 and I used that to change my name to character **a** 16 times and boy oh boy!, we get a heck ton of money. I noticed in the debug panel. The **player_name** memory space can stores upto 12 bytes and since my input was of of 16 characters, the rest 4 characters where overflowed to the **coins** memory space and this is why I got that amount of money out of nowhere. This was noticable because the first 4 bytes from the **coins** memory space were overwritten by **41** which is **a** in ASCII text. So we're dealing with a buffer overflow problem.
Now I tried buying the star, but I got a error message stating that I have an absurd amount of money to buy the star. The game was desgined so that no one can win by McGreedy. Since the option to buy the star was **d**, what if we try to overflow the name input toa point where the inventory memory space is over written with **d** and we get a star in our inventory.
Since there were 4×11 bytes before the inventory memory space, we need to give an input of a random characters of length 4×11 followed by character **d** in the change your name option.

![Screenshot (124)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/c187947a-2546-4882-b9af-e81e3fcbbce1)

As expected, we get a star in the inventory. By placing this star on the Christmas Tree, we get the flag for our challenge

![Screenshot (93)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/99990e21-fa19-4015-a5c2-7c47c2cc2182)


##  If the coins variable had the in-memory value in the image below, how many coins would you have in the game?

So reading the hex values from the coins memory space in reverse order it would be **0×[53 50 4f 4f]** which when entered in a hexadecimal to decimal converter tool will give us the answer.

![Screenshot (123)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/40c2e534-d286-474e-986b-b2ba9aaed846)


**Ans- `1397772111`**

## What is the value of the final flag?

**`The flag- THM{mchoneybell_is_the_real_star}`**
