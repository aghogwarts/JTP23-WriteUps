## Day 1 Machine Learning
- Prompt injection attacks manipulate a chatbot's responses by inserting specific queries, tricking it into unexpected reactions. These attacks could range from extracting sensitive info to spewing out misleading responses.  
- Natural Language Processing is a sub-field of Artificial Intelligence dedicated to enabling machines to understand and respond to human language. One of the core mechanisms in NLP involves predicting the next possible word in a sequence based on the context provided by the preceding words. With the training data fed into it, NLP analyses the patterns in the data to understand the relationships between words and make educated guesses on what word should come next based on the context.  
- Security measures are put in place to avoid prompt injection but loopholes can be used to by pass them like accessing information under the name of another person authorized to have that information provided no verification is put in place or by disengaging the security measures by telling the chatbot it is in maintainence mode.  
- Another AI is set up in a chatbot to intercept user messages and check for malicious input before sending them to the chatbot. It can be continuously trained on malicious inputs. The more people use and attack it, the smarter it becomes and the better it can detect malicious input. This, combined with a properly constructed system prompt, would increase the security of the chatbot.  
## Day 2 Log Analysis  
- Correlating the uses of Data Science to Cybersecurity.  
- Working with Jupyter Notebooks.  
- Basics about Python. Data Types (``int,float,string,boolean``). Variables are used to store data, given a name in order to be accessed later (``Label = Data``). Lists are used to store a collection of values as a variable (``transport = ["Car", "Plane", "Train"] age = ["22", "19", "35"]``). A library is a collection of code that can be imported into the application.
- Pandas is a Python library that allows us to manipulate, process, and structure data. In pandas, a series is similar to a singular column in a table. It uses a key-value pair. The key is the index number, and the value is the data we wish to store. Example: ``transportation_series = pd.Series(transportation)`` then ``print(transportation_series)``. DataFrames extend a series because they are a grouping of series. In this case, they can be compared to a spreadsheet or database because they can be thought of as a table with rows and columns. Example: Provide each row with data``data = [['Ben', 24, 'United Kingdom'], ['Jacob', 32, 'United States of America'], ['Alice', 19, 'Germany']]`` then specify the columns ``df = pd.DataFrame(data, columns=['Name', 'Age', 'Country of Residence'])``.
- Matplotlib allows us to quickly create a large variety of plots. ``plt.plot(['January', 'February', 'March', 'April' ],[8,14,23,40])`` is an example.  
## Day 3 Brute Forcing  
- Brute Forcing a password involves trying out all the different possible combinations of characters possible until the correct password is found.  
- Limitations involve excessively long durations for strong passwords, timeout functionality in locks for incorrect password inputs, etc.  
- Generating Password: We can generate passwords by using the ``crunch`` command. The structure is as follows:-  
``crunch`` ``3``(minimum length of password) ``3``(max. length of password) ``ABCDEF``(character set to be used to generate) ``-o password.txt``(saves output in password.txt file)  
- Using Hydra to try out the passwords on a website requires 3 pieces of information. The **method** in which the input is sent, the **URL** or server **where** the input is sent and the **name** of the input value. The structure of the hydra commant is as follow:-  
``hydra -l ''``(indicates that the login name is blank as the security lock only requires a password) ``-P 3digits.txt``(Specifies the password file to use) ``-f``(stops Hydra after finding a working password) ``-v``(provides verbose output and is helpful for catching errors) ``MACHINE_IP``(IP address of the target) ``http-post-form``(specifies the HTTP method to use) ``"/login.php:``(the page where the PIN code is submitted) ``pin=^PASS^:``(will replace ^PASS^ with values from the password list) ``Access denied"``(indicates that invalid passwords will lead to a page that contains the text “Access denied”) ``-s 8000``(the port number on the target)
## Day 4 Brute Forcing  
- CeWL (pronounced "cool") is a custom word list generator tool that spiders websites to create word lists based on the site's content. Spidering, in the context of web security and penetration testing, refers to the process of automatically navigating and cataloguing a website's content, often to retrieve the site structure, content, and other relevant details. This capability makes CeWL especially valuable to penetration testers aiming to brute-force login pages or uncover hidden directories using organisation-specific terminology. Beyond simple wordlist generation, CeWL can also compile a list of email addresses or usernames identified in team members' page links. Such data can then serve as potential usernames in brute-force operations.
- Wfuzz is a tool designed for brute-forcing web applications. It can be used to find resources not linked directories, servlets, scripts, etc, brute-force GET and POST parameters for checking different kinds of injections (SQL, XSS, LDAP), brute-force forms parameters (user/password) and fuzzing. 
## Day 5 Reverse Engineering  
- The Disk Operating System was a dominant operating system during the early days of personal computing. Microsoft tweaked a DOS variant and rebranded it as MS-DOS, which later served as the groundwork for their graphical extension, the initial version of Windows OS. The fundamentals of file management, directory structures, and command syntax in DOS have stood the test of time and can be found in the command prompt and PowerShell of modern-day Windows systems.
- Common DOS commands and Utilities:  
CD	Change Directory  
DIR	Lists all files and directories in the current directory  
TYPE	Displays the contents of a text file  
CLS	Clears the screen  
HELP	Provides help information for DOS commands  
EDIT	The MS-DOS Editor
- File signatures, commonly referred to as "magic bytes", are specific byte sequences at the beginning of a file that identify or verify its content type and format. These bytes often have corresponding ASCII characters, allowing for easier human readability when inspected. The identification process helps software applications quickly determine whether a file is in a format they can handle, aiding operational functionality and security measures.
- list of some of the most common files and their magic:  
File Format	-> Magic Bytes -> ASCII representation  
PNG image file -> 89 50 4E 47 0D 0A 1A 0A -> %PNG  
GIF image file -> 47 49 46 38 -> GIF8  
Windows and DOS executables	-> 4D 5A -> MZ  
Linux ELF executables	7F 45 4C 46 -> .ELF  
MP3 audio file -> 49 44 33 -> ID3  
## Day 6 Memory Corruption  
- Buffer overflow is a memory vulnerability in which the value of a particular variable exceeds the allocated memory and goes into the allocation of another variable.
- Buffer overflows occur in some programming languages, mostly C and C++, where the variables' boundaries aren't strict.
- Integers in C++ are stored in a very particular way in memory. First, integers have a fixed memory space of 4 bytes. Secondly, an integer's bytes are stored in reverse order in most desktop machines. This is known as the ``little-endian`` byte order.
