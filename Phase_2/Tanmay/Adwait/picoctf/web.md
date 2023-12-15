# CAAS
## problem 
we are given a url of a web service in which we can make a cow say whatever we want and the code for the service in javascript.

## solution
First i opened the the url and from there we are directed as to how can we use the serive to mak the cow say words.
![Screenshot from 2023-11-14 19-12-56](https://github.com/adwait3/pico/assets/148553626/78e12bb6-c4bc-462c-88a9-c03b74288ebb)
i tried saying hi 
after this i look at the js code which is given to us
![Screenshot from 2023-11-14 19-06-52](https://github.com/adwait3/pico/assets/148553626/7ea04c10-348d-4638-9644-e84cbc53b4a2)

and find out that   exec(`/usr/games/cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
command gives our message input to the command prompt and sends the commands output as a response
and that
app.listen(3000, () => {
  console.log('listening');
});
starts the server and makes it listen on the 3000 port.
this made me realise that i can type commands in the url as https://caas.mars.picoctf.net/cowsay/hi;ls;cat%20falg.txt to run the lines directly in the comand prompt and get the output 
![Screenshot from 2023-11-14 19-07-10](https://github.com/adwait3/pico/assets/148553626/d1c8dec9-963b-4d4e-ae53-9629f66cad6f)

![Screenshot from 2023-11-14 19-09-02](https://github.com/adwait3/pico/assets/148553626/e3bd85b9-9a58-4d7a-a21e-9cc6c7d34a9d)

after reading the flag.txt file we get the flag , we use %20 for space as a url cannot have spaces.

## flag
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}

# forbidden paths
## problem
Can you get the flag?
Here's the website.
We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?
## solution
 first i siply tried to go and read the file /flag.txt but i got a message saying not authorised
 in our problem statement we are told that our website is filtering absolute paths , after studying a bit more about absolute and relative paths and found out that the main difference is going from the root path to our file and directly searching our file in the current directory so i tried to read the file by 
 * /usr/share/nginx/html/flag.txt
but still i was not authorised
since the relative paths were getting filtered and our relative path /flag.txt was not authorised , i thought it was something related to hirarchy since it said not authorised and if we can more up hirarchy by relative path maybe we can get authorised to view the file withouth being filtered. so i tried ../ to move up a directory while using relative paths (as we are not specifing the directory name just using ../) we use this 4 times to move up to the parent directory and now after reading we get the flag.
![Screenshot from 2023-11-15 12-04-33](https://github.com/adwait3/pico/assets/148553626/df30132a-bbb3-4bd3-b54d-b63d1683c007)
![Screenshot from 2023-11-15 12-04-10](https://github.com/adwait3/pico/assets/148553626/49d3b958-7bb3-452f-b553-02491a49b5cf)

## flag
picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}


# Local Authority
## problem
Can you get the flag?
Go to this website and see what you can discover.
wee are given just a website 
hint
* How is the password checked on this website?

## solution
first i tried to get something from the source code of the website but couldnt find anything
![Screenshot from 2023-11-15 14-29-26](https://github.com/adwait3/pico/assets/148553626/53c80617-343a-4379-b551-06e4469cedf6)
 so i tried a random password to see what will happen, and this led me to another page stationg login failed i looked up its source code too and found intresting function "checkPassword".
 ![Screenshot from 2023-11-15 14-28-49](https://github.com/adwait3/pico/assets/148553626/cc73e65f-d210-4100-bd53-e01247b3a936)
![Screenshot from 2023-11-15 14-30-27](https://github.com/adwait3/pico/assets/148553626/8deeffba-4d3b-420e-92ce-2589dc860258)

 i also found a javascript file secure.js and opened to see what was in it and found our check password function which gave me the 
 * username = admin
 * password = strongPassword098765
![Screenshot from 2023-11-15 14-29-18](https://github.com/adwait3/pico/assets/148553626/4d825bcd-8a8f-475b-8923-ed7ef4d6aa4e)
trying this gave me the flag.
![Screenshot from 2023-11-15 14-37-01](https://github.com/adwait3/pico/assets/148553626/536d7159-fc3b-4ea0-9fb3-e34eb0c2c7b8)
## flag
picoCTF{j5_15_7r4n5p4r3n7_05df90c8}
