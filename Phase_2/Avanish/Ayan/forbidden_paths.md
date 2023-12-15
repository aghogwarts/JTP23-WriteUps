# forbidden-paths
(consists of converting absolute paths to relative paths)
The given site shows 3 files and i tried command line injection again and it does not work. When i put /flag.txt, its shoes 'not authorized', while for file.txt it shows 'file does not exist', so the site is filtering slashes.

Putting in the absolute path for an existing file `/usr/share/nginx/html/oliver-twist.txt` shows not authorized while using relative path `./oliver-twist.txt` works.

Now instead of ./ we use ../ to traverse working directory, this makes us to move up a directory, using quite a few of these will get us the final flag as intead of `/usr/share/nginx/html/flag.txt` we use `../../../../../flag.txt`
Flag : 'picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}'
