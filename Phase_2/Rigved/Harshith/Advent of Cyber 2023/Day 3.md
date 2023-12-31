# Brute Forcing

In this challenge we'll try brute force the password to a lockpad which takes 3 characters from the character set **0123456789ABCDEF**. We'll be learnig how to use **_crunch_** to create all possible number of character combiations and use **_hyra_** to run all those combinations.
We'll first crunch all the possible password combinations into a **3digit.txt** text file as 
- **`crunch 3 3 0123456789ABCDEF -o 3digits.txt`**
  - The first **3** in the line specifies the minimum length of the combination
  - The second **3** in the line specifies the maximum length of the combination
  - **0123456789ABCDEF** specifies the character set to be used to form the combinations
  - **`-o 3digits.txt`** takes the possible combination and stores it in the **3digit.txt** file.
![Screenshot (77)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/ca2665d6-e74c-4eb5-a93e-92bc4ae7291b)

Now before using hydra to try out the combinations, we need to know the necessary arguements to set hydra. We'll view the page source of the website and these three pieces of information, **post** , **/login.php** , and **pin**, are necessary to set the arguments for Hydra. On checking out the reading material from the challenge description, We can use hydra as 
- **`hydra -l '' -P 3digits.txt -f -v MACHINE_IP http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000`**
  - **`-l ''`** indicates that the login name is blank as the security lock only requires a password
  - **`-P 3 digits.txt`** specifies the password file to be used.
  - **`-f`** stops Hydra after finding a working password
  - **`MACHINE_IP`** is the IP address of the target
  - **`http-post-form`** specifies the HTTP method to use which we got to know while viewing the page source of the website.
  - **`/login.php`** is the page where the PIN code is submitted
  - **`pin=^PASS^`** will replace ^PASS^ with values from the password list
  - **`Access denied`** indicates that invalid passwords will lead to a page that contains the text “Access denied”
  - **`-s 8000`** indicates the port number on the target

![Screenshot (78)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/e533060f-e3a1-404a-a9f2-4bf2f23de27e)
![Screenshot (79)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/1c5a899e-7e41-452e-848c-30c2352a0452)

After getting several errors for some password combination we get the final correct password which is **6F5**.
  We'll ue this password to get our flag from the website.
![Screenshot (80)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/bbc8422a-4223-44d8-b3e9-69ac002eb557)
  **The flag - `THM{pin-code-brute-force}`**




