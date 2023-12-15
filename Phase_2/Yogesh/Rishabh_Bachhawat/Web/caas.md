The message box was executed using `exec` so I tried to directly run `$ls` but that returned a blank screen. Tried `$echo test` and it echoed to output.
After trying many things the top answer on this thread showed a possible approach.
https://unix.stackexchange.com/questions/63648/how-to-send-many-commands-to-shell-and-wait-for-the-command-behind-ends
So tried https://caas.mars.picoctf.net/cowsay/echo%20e;ls and it worked. 

![image](https://github.com/CoderZonora/picoCTF/assets/140229408/a1c90793-e539-432b-8e00-711bffd34195)

![image](https://github.com/CoderZonora/picoCTF/assets/140229408/1a5c13f0-34a8-47b3-8e11-b240fb097b05)


Flag : picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
