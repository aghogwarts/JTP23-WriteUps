# babygame01
We are given a game that takes 4 inputs to move the player, once player reaches X, they win
I used ghidra to analyse the code

In the move player function i see an unknown parameter p which instantly solves the challenge
```
  if (param_2 == 'p') {
    solve_round(param_3,param_1)
```

```
    } while (y_coordinate != 29);
  } while (x_coordinate != 89);
  puts("You win!");
  if (win_var != '\0') {
    puts("flage");
    win();
    fflush(_stdout);
```
We want the win_var to not be 0 then it will show the flag, now if we move 4 spots before the map which is probably the length of the variable, its shows " player has the flag = 64" 64 is the @ character. 


Then we use the 'p' secret command to solve the game and get the 'flage' which is "picoCTF{gamer_m0d3_enabled_6aeb6b85}"
![bg01](https://github.com/nAYANko/picoCTF/assets/147973815/06030ed8-5040-4e3b-b6ed-a2f8de6f6c6c)
![bg02](https://github.com/nAYANko/picoCTF/assets/147973815/c18cfce1-8d89-4acd-907c-db9cbcae5772)
![bg03](https://github.com/nAYANko/picoCTF/assets/147973815/a8be8299-145f-4906-92d8-9947dd0508fc)
![bg04](https://github.com/nAYANko/picoCTF/assets/147973815/a21ed421-cdc9-4ad6-a953-1d6bc435daed)





