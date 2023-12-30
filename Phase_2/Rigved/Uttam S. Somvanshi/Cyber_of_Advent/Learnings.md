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
## Day 7 Log Analysis  
- A log file is a record of important events, actions, errors, or information as they happen in a computer or software application. It's structure is as follows:-  
``<Source IP Address> <Timestamp> <HTTP Request> <Status Code> <User Agent>``  
- A proxy server is an intermediary between your computer or device and the internet.  
- Understanding the  functions of ``cat``, ``less``, ``head``, ``tail``, ``nl``, ``wc`` and ``cut`` commands.  
- Piping the grep command(used to reach for exact texts in a file) with head.  
## Day 8 Disk forensics  
- FTK Imager is a forensics tool that allows forensic specialists to acquire computer data and perform analysis without affecting the original evidence, preserving its authenticity, integrity, and validity for presentation during a trial in a court of law.
## Day 9 Malware Analysis  
- A sandbox is like a pretend computer setup that acts like a real one. It's a safe place for experts to test malware and see how it behaves without any danger.  
- .NET binaries are compiled files containing code written in languages compatible with the .NET framework, such as C#, VB.NET, F#, or managed C++. These binaries are executable files (with the .exe extension) or dynamic link libraries (DLLs with the .dll extension). They can also be assemblies that contain multiple types and resources.
- Compared to other programming languages like C or C++, languages that use .NET, such as C#, don't directly translate the code into machine code after compilation. Instead, they use an intermediate language (IL), like a pseudocode, and translate it into native machine code during runtime via a Common Language Runtime (CLR) environment.
- In simple terms, it's only possible to analyse a C or C++ compiled binary by reading its assembly instructions (low-level). Meanwhile, a C# binary can be decompiled and its source code retrieved since the intermediate language contains metadata that can be reconverted to its source code form.
- C2, or command and control, refers to a centralised system or infrastructure that malicious actors use to remotely manage and control compromised devices or systems. It serves as a channel through which attackers issue commands to compromised entities, enabling them to carry out various activities, such as data theft, surveillance, or further malware propagation.
- Malware with C2 capabilities typically exhibits the following behaviours:-
   1. HTTP requests: C2 servers often communicate with compromised assets using HTTP(s) requests. These requests can be used to send commands or receive data.  
   2. Command execution: This behaviour is the most common, allowing attackers to execute OS commands inside the machine.  
   3. Sleep or delay: To evade detection and maintain stealth, threat actors typically instruct the running malware to enter a sleep or delay for a specific period. During this time, the malware won't do anything; it will only connect back to the C2 server once the timer completes
- dnSpy is an open-source .NET assembly (C#) debugger and editor. It is typically used for reverse engineering .NET applications and analysing their code and is primarily designed for examining and modifying .NET assemblies in a user-friendly, interactive way. It's also capable of modifying the retrieved source code (editing), setting breakpoints, or running through the code one step at a time (debugging).
## Day 10 SQL Injection  
- SQL provides a rigid way to query, insert, update, and delete the data stored in these tables, allowing you to retrieve and alter databases as needed. A website or application that relies on a database must dynamically generate SQL queries and send them to the database engine to fetch or update the necessary data. The syntax of SQL queries is based on English and consists of structured commands using keywords like SELECT, FROM, WHERE, and JOIN to express operations in a natural, language-like way.
- PHP is a server-side scripting language that enables developers to create dynamic and interactive websites by generating HTML content on the server and delivering it to the client's web browser.
- The most common way for PHP to connect to SQL databases is using the PHP Data Objects (PDO) extension or specific database server drivers like mysqli for MySQL or sqlsrv for Microsoft SQL Server (MSSQL). The connection is typically established by providing parameters such as the host, username, password, and database name.
- GET Parameters are an important too for interactive web aplications as they allow users to interact with the database by dynamically generating queries.
- Stacked queries enable attackers to terminate the original (intended) query and execute additional SQL statements in a single injection, potentially leading to more severe consequences such as data modification and calls to stored procedures or functions.
- xp_cmdshell is a system-extended stored procedure in Microsoft SQL Server that enables the execution of operating system commands and programs from within SQL Server. It provides a mechanism for SQL Server to interact directly with the host operating system's command shell. While it can be a powerful administrative tool, it can also be a security risk if not used cautiously when enabled.  
- MSFvenom is a command-line payload generation tool. It's part of the Metasploit Framework, a widely used penetration testing and ethical hacking set of utilities. MSFvenom is explicitly designed for payload generation and can be used to generate a Windows executable that, when executed, will make a reverse shell connection back.
## Day 11 Active Directory  
- Active Directory (AD) is a system mainly used by businesses in Windows environments. It's a centralised authentication system. The Domain Controller (DC) is at the heart of AD and typically manages data storage, authentication, and authorisation within a domain.  
- Microsoft introduced Windows Hello for Business (WHfB) as a modern and secure way to replace conventional password-based authentication. Instead of relying on traditional passwords, WHfB utilises cryptographic keys for user verification. Users on the Active Directory domain can access the AD using a PIN or biometrics connected to a pair of cryptographic keys: public and private. Those keys help to prove the identity of the entity to which they belong.  
- The ``msDS-KeyCredentialLink`` is an attribute used by the Domain Controller to store the public key in WHfB for enrolling a new user device
- Here's the procedure to store a new pair of certificates with WHfB:  
  1. Trusted Platform Module (TPM) public-private key pair generation: The TPM creates a public-private key pair for the user's account when they enrol. It's crucial to remember that the private key never leaves the TPM and is never disclosed.
  2. Client certificate request: The client initiates a certificate request to receive a trustworthy certificate. The organisation's certificate issuing authority (CA) receives this request and provides a valid certificate.
  3. Key storage: The user account's ``msDS-KeyCredentialLink`` attribute will be set.
- Authentication Process:  
  1. Authorisation: The Domain Controller decrypts the client's pre-authentication data using the raw public key stored in the msDS-KeyCredentialLink attribute of the user's account.  
  2. Certificate generation: The certificate is created for the user by the Domain Controller and can be sent back to the client.  
  3. Authentication: After that, the client can log in to the Active Directory domain using the certificate.  
## Day 12 Defence in Depth  
- One of the best practices of hardening operations is to follow the principle of least priviledge where a user is only given the permissions that are necessary.
- Purely text based authentication is no secure enough.
- Strong Passwords practices should be followed including proper storage of passwords.
- In order to avoid outside access, platforms should be accessible only to necessary users.
## Day 13 Intrusion Detection  
- Intrusion detection and prevention is a critical component of cyber security aimed at identifying and mitigating threats.
- The Diamond Model is a security analysis framework that seasoned professionals use to unravel the mysteries of adversary operations and identify the elements used in an intrusion. It comprises four core facets, interconnected to form a well-orchestrated blueprint of the attacker's plans:  
  1. Adversary
  2. Victim
  3. Infrastructure
  4. Capability (phishing, malware, exploiting vulnerabilties, social engineering, DOS, Insider Threat)
- Defensive Capability  
  1. Threat hunting is a proactive and iterative process, led by skilled security professionals, to actively search for signs of malicious activities or security weaknesses within the organisation's network and systems. Threat hunters analyse behavioural patterns, identify advanced threats, and improve incident response. Developing predefined hunting playbooks and fostering collaboration among teams ensures a systematic and efficient approach to threat hunting.
  2. Vulnerability management is a structured process of identifying, assessing, prioritising, mitigating, and monitoring vulnerabilities in an organisation's systems and applications.
- Firewalls come in many forms, including hardware, software, or a combination. Their presence is vital, a cornerstone of any cyber security defence strategy. The following are the common types of firewalls that exist:  
  1. Stateless/packet-filtering filters network packets based on a set of rules(IP,Ports,Protocols.
  2. Stateful inspection is used to track the state of network connections and use this information to make filtering decisions
  3. Proxy service protects the network by filtering messages at the application layer, providing deep packet inspection and more granular control over traffic content.
  4. Web application firewall (WAF) blocks common web attacks such as SQL injection, cross-site scripting, and denial-of-service attacks.
  5. Next-generation firewall combines the functionalities of the stateless, stateful, and proxy firewalls with features such as intrusion detection and prevention and content filtering.
- Honeypots are designed to mimic legitimate targets, yet they are under the watchful control of the defender. Honeypots can be classified into two main types:
  1. Low–interaction honeypots: These honeypots artfully mimic simple systems like web servers or databases. They gather intelligence on attacker behaviour and detect new attack techniques.
  2. High–interaction honeypots: These honeypots take deception to new heights, emulating complex systems like operating systems and networks. They collect meticulous details on attacker behaviour and study their techniques to exploit vulnerabilities.
- PenTBox is a tool used to setup Honeypots.  
## Day 14 Machine Learning  
- ML refers to the process used to create a system that can mimic the behaviour we see in real life. This is because there is intelligence in real life and its structures. For examples:
  1. Genetic algorithm: This ML structure aims to mimic the process of natural selection and evolution. By using rounds of offspring and mutations based on the criteria provided, the structure aims to create the "strongest children" through "survival of the fittest".
  2. Particle swarm: This ML structure aims to mimic the process of how birds flock and group together at specific points. By creating a swarm of particles, the structure aims to move all the particles to the optimal answer's grouping point.
  3. Neural networks: This ML structure aims to mimic the process of how neurons work in the brain. These neurons receive various inputs that are then transformed before being sent to the next neuron. These neurons can then be "trained" to perform the correct transformations to provide the correct final answer.
- Learning Styles for neural networks include:-
  1. Supervised learning: In this learning style, we guide the neural network to the answers we want it to provide. We ask the neural network to give us an answer and then provide it with feedback on how close it was to the correct answer. In this way, we are supervising the neural network as it learns. However, to use this learning style, we need a dataset where we know the correct answers. This is called a labelled dataset, as we have a label for what the correct answer should be, given the input.
  2. Unsupervised learning: In this learning style, we take a bit more of a hands-off approach and let the neural network do its own thing. While this sounds very strange, the main goal is to have the neural network identify "interesting things". Humans are quite good at most classification tasks – for example, simply looking at an image and being able to tell what colour it is. But if someone were to ask you, "Why is it that colour?" you would have a hard time explaining the reason. Humans can see up to three dimensions, whereas neural networks have the ability to work in far greater dimensions to see patterns. Unsupervised learning is often used to allow neural networks to learn interesting features that humans can't comprehend that can be used for classification. A very popular example of this is the restricted Boltzmann machine.
- Basic structure of neural networks consists of various different nodes (neurons) that are connected. The neural networks have 3 layers called Input, Output and Hidden layers.
- Feed Forward loop is how we send data through the network and get an answer on the other side. Once our network has been trained, this is the only step we perform. At this point, we stop training and simply want an answer from the network.  
- Back Propagation : When we are training our network, the feed-forward loop is only half of the process. Once we receive the answers from our network, we need to tell it how close it was to the correct answer.  
- Overtraining is a big problem with neural networks. We are training them with data where we know the answers, so it's possible for the network to simply learn the answers, not how to calculate the answer. To combat this, we need to validate that our neural network is learning the process and not the answers. This validation also tells us when we need to stop our learning process. To perform this validation, we have to split our dataset into the three datasets below:
  1. Training data
  2. Validation data: After each training round, we send this data through our network to determine its performance. If the performance starts to decline, we know we're starting to overtrain and should stop the process
  3. Testing data: This dataset is used to calculate the final performance of the network.
- The reason for the fluctuation in accuracy is that neural networks have randomness built into them. The weights for each of the inputs to the nodes are randomised at the start, meaning that two neural networks are never exactly the same – similar to how different brains might learn the same data differently. To truly determine the accuracy of your neural network, you would have to train it several times and calculate the average accuracy across all networks.
- An ML structure is only as good as the quality of the data used to train it. Without good data, we wouldn't be able to receive any accurate output. GIGO (Garbage in garbage out)
## Day 15 Machine Learning  
- A Machine Learning pipeline refers to the series of steps involved in building and deploying an ML model. These steps ensure that data flows efficiently from its raw form to predictions and insights.
- A typical pipeline would include **collecting** data from different sources in different forms, **preprocessing** it and performing feature extraction from the data, **splitting** the data into testing and training data, and then applying Machine Learning **models** and **predictions**.
- CountVectorizer is a class provided by the scikit-learn library in Python is used to convert text into a token (word) count matrix.
## Day 16 Machine Learning  
- CNNs are normal neural networks that simply have the feature-extraction process as part of the network itself i.e, they have the ability to extract features that can be used to train a neural network.
- We can divide our CNN into three main components:
   1. Feature extraction  
   2. Fully connected layers  
   3. Classification
## Day 17 Traffic Analysis  
- The Network Traffic data flow offers invaluable network management(Monitoring network performance, identifying bandwidth bottlenecks, and ensuring resource allocation and quality of service), troubleshooting(Identifying network issues), incident response, and threat-hunting insights(Proactive analysis for signs of suspicious and malicious patterns).
- Network flow data is a lightweight alternative to PCAPs. It's commonly used in NetFlow format, a telemetry protocol developed by Cisco that focuses on the metadata part of the traffic. In other words, it provides only the "summary" of the traffic.
![Screenshot 2023-12-30 194023](https://github.com/Azure9733/JTP23-WriteUps/assets/143328010/a70708e3-7134-40eb-83dc-62e413edfb1d)  
![Screenshot 2023-12-30 194123](https://github.com/Azure9733/JTP23-WriteUps/assets/143328010/344ca876-bd0e-49e3-a423-c61cf7df9c7a)  
- SiLK, or the System for Internet Level Knowledge tool suite, was developed by the CERT Situational Awareness group at Carnegie Mellon University's Software Engineering Institute. It contains various tools and binaries that allow users to collect, parse, filter, and analyse network traffic data.
- One of the top five actions in packet and flow analysis is overviewing the file info. SiLK suite has a tool ``rwfileinfo`` that makes this possible.
- ``Rwcut`` reads binary flow records and prints those selected by the user in text format. It works like a reading and filtering tool.
- ``rwfilter`` is an essential part of the SiLK suite. It comes with multiple filters for each column in the sample you're working on and is vital for conducting impactful flow analysis. However, even though ``rwfilter`` is essential and powerful, it has a tricky detail: it requires its output to be post-processed. This means that it doesn't display the result on the terminal, and as such, it's most commonly used with ``rwcut`` to view the output.
## Day 18
- The ``top`` command shows us a list of processes in real time with their usage. It's a dynamic list, meaning it changes with the resource usage of each process.  
- Cronjobs are tasks that we ask the computer to perform on our behalf at a fixed interval. Often, that's where we can find traces of auto-starting processes.  
- We use the ``systemctl list-unit-files`` to list all services. Since the service we are looking for must be enabled to respawn the process, we use ``grep`` to give us only those services that are enabled.  
