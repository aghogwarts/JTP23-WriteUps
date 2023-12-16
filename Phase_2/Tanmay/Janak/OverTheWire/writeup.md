# OverTheWire

## Task 1

### Level 0
Use the credentials to ssh into the server
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

### Level 0-1
Use cat command to get readme contents (```cat readme.md```)

### Level 1-2
1. use cd .. to go into home directory
2. ``find -name "-"`` to get file with name "-"
3. then use cat command to get contents of file. regular ``cat -`` will not work. use ``cat < -``. Because it is a dashed filename, it causes the terminal to confuse the hyphen with stdin and expect input.

### Level 2-3
navigate to /home parent and use find command  (``find /home -name "spaces in this filename"``). then use cat to get contents.

### Level 3-4
Just enter ``find`` with no parameters/options. this gives ALL filepaths in the directory. Then perform cat on the revealed filepath ``./.hidden``.

### Level 4-5
Navigate to /inhere and perform cat on all files until you get human readable one
Edit: could have used ``grep text data.txt`` or ``strings data.txt`` instead of finding it manually

### Level 5-6
Use ``du -all -b`` to get sizes of all(-a) files in bytes(-b). Find the file with 1033 byte size. Check contents for human readability. 
Edit: could have used ``find -size 1033`` instead of finding 1033 byte file manually. 

### Level 6-7
1. ``find ./* -user <user_owner> -group <group_owner> -size <size>`` in highest directory
2. perform ``cat``

### Level 7-8
Refer grep docs. Option -w returns line with matching expression. 
```
grep -w "millionth" data.txt
```

### Level 8-9
Use pipe character to pipe command output to another command
pipe from cat to sort to uniq -u
```
cat data.txt | sort | uniq -u
```

### Level 9-10
1. Extract human readable part (text) using strings command
2. pipe the strings output into the ``grep -w "="`` command
```
strings data.txt | grep -w "="
```

### Level 10-11
pipe cat into base64 -d
```
cat data.txt | base64 -d
```

### Level 11-12
use tr for text rotation. google syntax.
1. pipe cat into tr once for lower case character rotation
2. pipe once again for upper case character rotation
```
cat data.txt | tr [a-z] [n-za-m] | tr [A-Z] [N-ZA-M]
```
**Password to enter level 12-13:** ``JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv``


## Task 2

### Level 12-13
#### Steps -
0. Copied and pasted files to writable tmp dir
   ```
   mkdir tmp/mything
   cp /home/bandit12/data.txt tmp/mything/
   ```
2. Reverted hexdump using ``xxd``
   ```
   xxd -revert data.txt data2.txt
   ```
4. Used ``file`` to determine file details (compression details)
5. Decompressed with appropriate library (depending on compression type).
   ```gzip
   mv data.txt data.txt.gz
   gzip -r -d data.txt.gz
   ```
   ```bzip2
   bzip2 -d data.txt
   ```
   ```tar POSIX
   tar -xvf data.txt
   ```
   Note: In the case of gzip, had to rename decompressed files from data.txt to data.txt.gz before decompressing them. \
Order of compression discovered: gzip > POSIX tar > bzip2 > POSIX tar > POSIX tar > gzip > bzip2 > gzip

#### References -
1. man page of gzip, tar, bzip2
2. online docs for file, xxd
   
#### Screenshots -
1. Reversal of hexdump
   ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/59fed786-7da4-4d7d-8d33-6cfd81b5357f)

2. Some decompressions
    1. A gzip decompression
       \
       ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/a552e307-26cb-4f9a-b72d-f17fcb5ee151)
    3. A bzip2 decompression
       \
       ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/b028402d-02a1-4289-99c5-6cb926dcd4e8)
    5. A POSIX tar decompression
       \
       ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/8a7404c9-5c05-44f7-8a7b-4b3e5adaef98)
3. Final password
   \
   ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/a8c8ea4a-130f-4ec4-a63f-eec3ad5073e5)
#### Password of next level
``wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw``

### Level 13-14
```
ssh -i sshkey.private -p 2220 bandit14@localhost
```

### Level 14-15
#### Steps -
1. Password for this level was given in the previous level's desc. - ``fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq``
2. Sending the password to localhost port 30000 -
```
nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
```
#### References - 
netcat docs

#### Screenshot -
![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/9f78d34a-c6b6-48ff-9e99-45c6033f2c32)

#### Password of next level
``jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt``

### Level 15-16
#### Steps - 
1. Send openssl connection request
   ```
   openssl s_client -ign_eof -connect localhost:30001 
   ```
   Then paste password of this level in. 
#### References
openssl s_client docs

#### Password of next level
``JQttfApK4SeyHwDlI9SXGR50qclOAil1``
### Level 16-17
#### Steps
1. Find open ports
   ```
   netstat -tulpn | grep LISTEN
   ```
   or
   ```
   netstat -lntu
   ```
   This shows several open ports, of which only ``31790`` and ``31518`` are in between 31000 and 32000.
3. Send SSL connection request to each of the ports, checking for response. On sending to 31790, we obtain the SSH private key for the next level.
   ```
   openssl s_client localhost:31790
   ```
   Key obtained -
   ```
   MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
   imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
   Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
   DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
   JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
   x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
   KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
   J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
   d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
   YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
   vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
   +TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
   8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
   SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
   HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
   SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
   R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
   Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
   R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
   L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
   blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
   YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
   77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
   dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
   vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
   -----END RSA PRIVATE KEY-----
   ```
4. Logout and write the SSH private key to a file and SSH into the next level.
   ```
   echo "<key>" > sshkey.private
   ssh -i sshkey.private -p 2220 bandit17@localhost
   ```
### Level 17-18
#### Steps -
1. Find differences between the 2 files -
```diff passwords.old passwords.new```
#### References -
man diff
#### Screenshots -
![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/738a77fa-bfc0-4a3f-8f37-c70102edb4cd)
#### Password of next level 
``hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg``

### Level 18-19
#### Steps
1. SSH without using bashrc
```
ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh
```
2.
```
cat readme
```
#### References
googled ssh without using bashrc
#### Password of next level
``awhqfNnAbc1naukrpqDYcF95h7HoMTrC``

### Level 19-20
#### Steps
1. Ran setuid. Library was not present.
2. Looked around in directory. Found `./bandit20-do`.
3. Ran ``file ./bandit20-do`` and found it was an executable.
4. ```
   ./bandit20-do
   ```
Apparently running the file gives you access as user bandit20.
5. 
```
./bandit20-do cat /etc/bandit_pass/bandit20
```

#### Screenshots
1. 
![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/5ddd46dd-139b-4acd-aad9-3df5dd706cd6) \
2. \
![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/12a2f10c-c892-4ea5-a9a5-eca4f3d27774)
#### Password of next level
``VxCazJaVykI6W36BkBU0mJTCM8rR95XT``


### Level 20-21
#### Steps
1. Set up a local port to listen and send data and log the data received.. As this is process will occupy the terminal, we should create another terminal first, using ``screen``
```
screen
```
```
echo "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | netcat -l localhost 42010 | cat
```
2.  Use ``Ctrl+A``>``Ctrl+C`` to switch to a new screen terminal. Then -
```
./suconnect 42010
```
Switch to the other terminal using ``Ctrl+A``>``Ctrl+A``.

#### References
- stackoverflow - how to open new terminal in ssh
- stackoverflow - sending messages via netcat
- man netcat

#### Screenshots
1. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/dbc1ff06-2b95-4974-bd9d-b37ac78ba859)
2. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/dca74c52-1ca7-4994-8840-7fff30966e9f)
3. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/11c05ec3-4995-45bc-9506-18e204ee36ba)
4. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/bca0a675-1845-4a21-981c-a9c89de0b6f6)

#### Password of next level
``NvEJF7oVjkddltPSrdKEFOllh9V1IBcq``

### Level 21-22
#### Steps
1. Look in ``/etc/cron.d/``
   ```
   find /etc/cron.d/
   ```
3. Read ``/etc/cron.d/cronjob_bandit22``
   ```
   cat /etc/cron.d/cronjob_bandit22
   ```
4. Read the script the cron job is running
   ```
   cat /usr/bin/cronjob_bandit22.sh
   ```
   Apparently the cron job is to cat the password of user ``bandit22`` to another file. It can do this as it has perms.
5. Read the file the cron job wrote to.
   ```
   cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   ```

#### References
man cron

#### Screenshots
1. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/e718b598-658e-4e60-a61a-59aa91130856)
2. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/9b0826c3-26d2-40e4-99a3-6def83bd66b9)
3. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/b247045a-355d-4fe8-9e4a-5dd70cbff873)
4. ![image](https://github.com/codegallivant/cryptonite-taskphase/assets/27366422/3e9502a5-cf9b-408f-b804-67ad76ace682)




#### Password of next level
``WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff``
