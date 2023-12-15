<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - babygame01 Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup guides you through the process of solving the "babygame01" challenge in PicoCTF. The challenge falls under the Binary Exploitation category and requires analyzing a binary executable to find the flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 13, 2023

<b>Tools Used:</b><br>
- Terminal
- Online Decompiler

<b>Challenge Description:</b><br>
The "babygame01" challenge in PicoCTF requires participants to exploit a binary executable. It includes solving a game instance to retrieve the flag.

<b>Exploitation:</b><br>
1. Begin by running the binary to understand its behavior. Check if there are any obvious vulnerabilities. Solving the game did not retrieve the flag.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Solving_Game.png>)

</p><br>

2. Open the code in an online decompiler to look at the source code for any vulnerabilities. I used an online Ghidra decompiler for this code.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Ghidra_Code.png>)

</p><br>

3. Analyzing the main function, we see a couple of variables and functions. Checking out the print_map function. We can see this function just prints the map after the user makes a move.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Print_map.png>)

</p><br>

4. In the main function, we see that the flag will be printed once the variable 'local_aa4' is not a null value. To trigger this condition we must firstly win the game and the local variable 'local_aa4' must be non-zero to drop the flag.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Flag_Conditions.png>)

</p><br>

5. 'init_player()' takes the address of 'local_aac' and writes three words, array indexing flowing into subsequent parameters of main(). '*param_1' refers to editing the value of 'local_aac' or the y-coordinate. 'param[1]' refers to the next location following the location of the 'local_aac', which is the location of 'local_aa8' or the x-coordinate. '*param1 + 2' refers to changing the value of 'local_aa4', our flag variable.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Init_player.png>)

</p><br>

6. 'init_map()' confirms the purpose and ordering of the player position coordinates. It also exposes the exit position which is the game win condition, that is the player must reach {29, 89} = {0x1d, 0x59}.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Init_map.png>)

</p><br>

7. Analyzing the move_player function. We can see that the user uses w, a, s and d to move. Apart from that, we see two other entries, l and p. 'l' changes the player tile, and 'p' solves the map for us. We can notice that there is no bound on checking position increment/decrement operations, and these new player position values form the index of an array dereference.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Move_player.png>)

</p><br>

8. Therefore we have found the exploitable code. By manipulating the player's position values, we can control the array indexing and write data to a specific location in memory.<br>
'local_aa4' is located on the stack, and it immediately precedes the 'map_buf[]' array. Underflowing the 'map_buf' array involves manipulating the array index in a way that we access memory before the beginning of the array. This can lead to unintended consequences, such as overwriting variables on the stack.<br>
By setting the player's position to {0, -4}, we are effectively moving the array index four positions backward. This positioning is crucial to writing data to 'local_aa4' on the stack.<br>
The player_title character is used to write data to the least significant byte (LSB) of 'local_aa4', effectively changing its value.<br>

9. Going to position {0, -4} has effectively changed our flag variable value from 0 to 64.

<p align = 'center'>

![](<Pictures/babygame01 - Reached_Pos_-4.png>)

</p><br>

10. Typing 'p' will effectively solve the map for us and display the flag.<br>

<p align = 'center'>

![](<Pictures/babygame01 - Flag.png>)

</p><br>

<b>Conclusion:</b><br>
The "BabyGame01" challenge in PicoCTF provides participants with an opportunity to practice binary exploitation. By identifying and exploiting vulnerabilities in the binary executable, participants gain hands-on experience in software security.

</font>