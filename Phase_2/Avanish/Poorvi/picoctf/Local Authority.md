Hint tells us to look at how the password input is being taken
Viewing page source of the website we get the following:
![la1](https://github.com/poorvi1910/Cryptonite/assets/146640913/7fadface-22bc-4b55-ab32-5306ad917ecd)

Clicking on style.css we get the following code

We get nothing useful here. So we go back to the website and enter any random username and password and as expected the login fails.But if we view the source of the log in failed page we get the following: 
![la2](https://github.com/poorvi1910/Cryptonite/assets/146640913/9debdaa2-2dfc-405a-9a82-c04178e5c443)

We can see a javascript file ‘secure.js’ here. Clicking on it we get the below code:
![la3](https://github.com/poorvi1910/Cryptonite/assets/146640913/d5203fc1-7300-4567-8e78-2613af096613)

Hence we now have our login username and password.Entering these in the website, we get the following flag:
picoCTF{j5_15_7r4n5p4r3n7_05df90c8}
