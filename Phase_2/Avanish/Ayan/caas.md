# caas
So in this one, the given website just shows whatever replaces the {message} part at the end of the URL, there is nothing that stands out in the given site so i looked at the index.js file provided to find out that this site works using the GET method which is unsafe as it makes it vulnerable to command line injection.

We can put a semicolon after given message followed by the command in order to run the command
`https://caas.mars.picoctf.net/cowsay/nayanko;%20ls`

Spaces breaks the url so they are replaced by %20, the browser did that automatically in my case. We see a file falg.txt which seems to be the required file.

`https://caas.mars.picoctf.net/cowsay/nayanko;%20cat%20falg.txt`

We get the flag : 'picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}'
