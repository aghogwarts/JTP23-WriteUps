# CTF Challenge Writeup

## Challenge Overview

The challenge involves exploiting a website that functions similarly to an FTP page, where the content is printed to the user. The objective is to retrieve the contents of the `flag.txt` file, with the flag's location provided in the CTF problem.

## Exploiting the Vulnerability

By manipulating the file path and leveraging directory traversal, you successfully retrieved the flag. The provided path for the `flag.txt` file was:

```plaintext
../../../../flag.txt
```

This traversal technique allowed you to access the desired file and obtain the flag.

## Flag

The flag was printed as:

`picoCTF{7h3_p47h_70_5ucc355_6db46514}`

