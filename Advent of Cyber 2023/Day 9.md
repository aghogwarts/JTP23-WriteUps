# Malware Analysis 

We'll be using **dn.Spy** tool to analyse the file. This tool is userd for analysing **.NET** application and analysing their code. Malware means Malicious Software and we'll be testing the .NET file for the presence of any malware. So dnSpy is a great malware analysis toolfor .NET files as  we can use it to debug the files and be analysed either statically or dynamically by setting breakpoint.
Well it seems that the answers we're looking for are present in different function of the C# assembly. Let's answer them

## What HTTP User-Agent was used by the malware for its connection requests to the C2 server?

The user agent can be found in the **Postit** function.

![Screenshot (105)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/2aaef296-d801-4730-ada1-5ed7cd7a7476)

**Ans- `Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15`**

## What is the HTTP method used to submit the command execution output?
This can be answered by going through the reading material present in the challenge description
**`Ans- POST`**

## What key is used by the malware to encrypt or decrypt the C2 data?
The answer for this can be found in the **Encryptor** function.

![Screenshot (108)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/1fc00948-1ff4-4cac-9ded-209b18396733)


**Ans- `youcanthackthissupersecurec2keys`**

## What is the first HTTP URL used by the malware?

The answer can be found can be found in the **main** function. Since the http had McGreedy's name in it,  it's a give out that this is the answer.

![Screenshot (109)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/73c6d5f1-1b9f-463d-80f3-643adc6a9a81)


**Ans- `http://mcgreedysecretc2.thm/reg`**

## How many seconds is the hardcoded value used by the sleep function?

The answer can be found from the **int count** variable in the **main** function. This can be understood because the count variable is being used in the Sleeper definition.

![Screenshot (110)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/bd9d46f8-a517-4f9f-8b5d-dd91177de57c)


**Ans- `15`**

## What is the C2 command the attacker uses to execute commands via cmd.exe?

The attacker uses shell command to execute the commands via cmd.exe

**Ans- `shell`**

## What is the domain used by the malware to download another binary?

This can be answered when we look in the main function where **http://stash.mcgreedy.thm/spykit.exe** is being used with **Implant** function.This functiont accepts a URL string as its argument, initiates an HTTP request to the URL argument, and decodes it with Base64.

![Screenshot (111)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/4dd0dbe1-53c7-442b-8f2f-ef80cfc3f241)


**Ans- `stash.mcgreedy.thm`**


