<font size = '4'>
<p align = 'center'>
<b>
Advent of Cyber - Day 6 Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This comprehensive writeup covers the solution to Day 6 of the Advent of Cyber 2023 challenge titled "Memory Corruption Vulnerabilities." The challenge involves exploring memory corruption vulnerabilities in a game, understanding buffer overflows, and exploiting them to manipulate in-game variables.

<b>Author:</b> Misha Jain

<b>Date:</b> December 6, 2023

<b>Tools Used:</b><br>
- Game environment (provided in the challenge)
- Debug panel in the game
- Online tools (hex to decimal converter, CyberChef)

<b>Challenge Description:</b><br>
Day 6 focuses on memory corruption vulnerabilities in a game. Participants learn about buffer overflows, how variables in memory are structured, and how manipulating one variable can affect adjacent memory spaces. The challenge involves exploiting buffer overflows to gain an advantage in the game.

<b>Exploitation:</b><br>
1. Access the game at the provided URL after starting the target machine.<br><br>

2. Play as CatOrMouse and understand the game's mechanics. Earn coins through freelance programming jobs and interact with characters in the game.<br><br>

3. Van Jolly reports strange behaviors related to changing the player's name. Changing the name to "scroogerocks!" results in an unexpected increase in coins. This indicates a memory corruption vulnerability.<br><br>

4. Press TAB in the game to access the debug panel, which provides ASCII and HEX views of the memory layout.<br><br>

5. Focus on the coins variable in the HEX view of the debug panel. Understand how the game stores the coin count in memory.<br><br>

6. Learn about buffer overflow by changing the name to "aaaabbbbccccx" and observing the overflow into the coins variable.<br><br>

7. Explore how strings are handled in memory by changing the name to "Elf" and observing the memory layout. Understand the role of NULL characters in string representation.<br><br>

8. Exploit the buffer overflow by getting 13 coins and changing the name to "aaaabbbbccccx" to overflow into the coins variable.<br><br>

9. Understand how integers are represented in memory, especially considering the little-endian byte order.<br><br>

10. Calculate the in-game coin value based on the given in-memory value (4f 4f 50 53) using online tools or CyberChef. <br><br>

11. Exploit the memory corruption to gain an advantage, purchase the star, and finish the game. <br><br>

12. Upon successfully completing the game, retrieve the final flag displayed. <br><br>

13. Answers to Questions:
- If the coins variable had the in-memory value in the image below, how many coins would you have in the game?
    - Answer: 1397772111
- What is the value of the final flag?
    - Answer: THM{mchoneybell_is_the_real_star}

<b>Lessons Learned:</b><br>
- Understanding memory corruption vulnerabilities.
- Exploring buffer overflows and their impact on adjacent memory.
- Analyzing how strings and integers are represented in memory.
- Exploiting buffer overflows to manipulate in-game variables.<br><br>

<b>Conclusion:</b><br>
Day 6 of Advent of Cyber 2023 provided an engaging experience with memory corruption vulnerabilities in a game environment. Participants learned about buffer overflows, string representation in memory, and the impact of memory layout on variable manipulation. The challenge combined gaming elements with practical cybersecurity concepts.

</font>