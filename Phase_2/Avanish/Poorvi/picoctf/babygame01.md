We first need to put the elf file game into ghidra to decompile and view the source code.On doing so we see in the main fnction:

![bb1](https://github.com/poorvi1910/Cryptonite/assets/146640913/9a63b408-12b6-495e-a2a3-5acc353ee290)

The blue highlight gives us the winning condition. If we notice carefully the condition for flag printing is only when variable local_aa4 is not equal to 0. So to get the flag our focus must be on getting the variable to become non zero.

The yellow highlighted portions give us the variables used in the code which are needed to understand what is happening.

player initialisation function is used to initially place the player on the board and from the below we can see that the values of local_acc, local_aa8 and char get set to 4,4 and 0 which are x cood, y cood and flag respectively [they come in this order on the stack thats why]

![bb2](https://github.com/poorvi1910/Cryptonite/assets/146640913/72f44144-71d5-4dfe-9d61-1463807be830)

![bb3](https://github.com/poorvi1910/Cryptonite/assets/146640913/cbd5edbd-04cd-40f0-a723-8efb070512b4)

PLAYER MOVE FUNCTION:

![bb4](https://github.com/poorvi1910/Cryptonite/assets/146640913/18decbb1-b0e6-4fe7-b795-bddc6dc153f6)

This function tells us that if we press p, the player directly reaches point X

Thus if we move to position (-4,0) that is going backwards into the stack we should be able to access the the flag variable and indeed, we get the flag variable changed to 46, so now if we enter ‘p’ and move directly to the X position, the flag is printed along with the winning message.This is a segmentation fault.

A segmentation fault is a specific type of error caused by accessing memory that “doesn't belong to you”. It's a helper mechanism that keeps you from corrupting memory and causing memory errors that are difficult to debug. Whenever you get a segmentation fault, you know you are doing something wrong with the memory – accessing a variable that has already been freed, writing to a read-only part of memory, etc.

The flag is : picoCTF{gamer_m0d3_enabled_8985ce0e}

