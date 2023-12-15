#### caas
i went to https://www.youtube.com/watch?v=lkIFF4maKMU
i did the message thing, cow saying words is the funniest thing.
i downloaded the js file. First thing was that i don't know shit about js! so i watched  a basic video about it 
https://www.youtube.com/watch?v=lkIFF4maKMU
I UNDERSTOOD PARTS OF IT, BUT NOTHING USEFUL
so i googled how to run a js file on terminal
![Screenshot from 2023-11-09 18-55-27](https://github.com/s4twik/picoctf/assets/147993943/a60f10e5-0e23-48f4-b743-2da2ffc32ac0)
i did this, got a lot of errors, still no leads!
so i decided to reach out for help the GOD youtube.
i looked up a video and stopped as soon as i got a clue
it was pretty straight forward tbh if one knows JS
https://caas.mars.picoctf.net/cowsay/{message};cat falg.txt
i got the flag
![Screenshot from 2023-11-09 19-27-42](https://github.com/s4twik/picoctf/assets/147993943/994afd99-426c-4968-8271-65f8d3d999af)
#### Forbidden Paths

i opened the website, and tried the same thing i figured out with last problem. 
![image](https://github.com/s4twik/picoctf/assets/147993943/3c6fe2db-f31d-4810-9b07-63e723406154)
this was supposed to take me to the home directory
but it didn't
so i tried putting flag.txt in search box![image](https://github.com/s4twik/picoctf/assets/147993943/25aee2f4-6db1-420f-83d7-8b9f895f40d6)
nothing happened, so i tried putting `../` to go to home directory in the search bar.
it didn't show any error like before, i got the direction i had to look into.
i read the question again, it said that the website files are stored in different directory than the flag.txt file
so i copied the path of the website file and `usr/share/nginx/html/` and in place of all the name of directory i put `..` which will take me to the directory where the flag.txt is saved so my final command was `../../../../file.txt`.
![image](https://github.com/s4twik/picoctf/assets/147993943/d0aacfad-34e3-4b9e-9b7c-e8fd46db5e90)
![image](https://github.com/s4twik/picoctf/assets/147993943/4dd3d551-46f0-4860-8c45-15bb811eacd5)

#### Local Authority
i check what does loccal authority mean on google, nothing in particular
i tried of all the ways i used in last questions
i thought of the classic old way to check source code
i get a file called `login.php` i check it out
![image](https://github.com/s4twik/picoctf/assets/147993943/942af5fb-6f6f-467b-af8b-903efdb58465)
i again check different files available
i get this js file called `secure.js` i check it out
![image](https://github.com/s4twik/picoctf/assets/147993943/4761a4d2-4707-45f7-8427-5a4c412a4cc0)
![image](https://github.com/s4twik/picoctf/assets/147993943/36a22c2b-f822-4c76-8bd2-3b88583a352b)


