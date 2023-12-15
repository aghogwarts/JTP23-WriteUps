When we click on the website link we get the following:
![c1](https://github.com/poorvi1910/Cryptonite/assets/146640913/215e0649-dae5-4ec0-a2a2-c4184b49602a)

Displaying the javascript file, we can see the below code:
![c2](https://github.com/poorvi1910/Cryptonite/assets/146640913/c7efa968-505c-4116-a53c-9856f5308404)

The code is a simple Node.js application using the Express framework. This application serves static files from the "public" directory and has a single route that allows you to trigger the "cowsay" command with a message and return the output as plain text.

Here's a breakdown of the code:

1. First, it imports the necessary modules: `express` for creating a web server, and `child_process` to run shell commands.

2. An Express application is created using `express()` and stored in the `app` variable.

3. The `express.static` middleware is used to serve static files from the "public" directory. This means that any files in the "public" directory will be accessible via the web server.

4. The `app.get` method defines a route for handling GET requests to "/cowsay/:message". It uses a parameter ":message" to capture the message you want to pass to the "cowsay" command. When a request is made to this route, it uses the `exec` function to run the "cowsay" command with the provided message. The `{timeout: 5000}` option specifies a timeout of 5 seconds for the command execution. If an error occurs during command execution, it responds with a 500 status code. If the command executes successfully, it sets the response content type to plain text and sends the output from the "cowsay" command as the response.

5. Finally, the Express application listens on port 3000, and a message is logged to the console when the server starts.

To use this application, you can navigate to http://localhost:3000/cowsay/YourMessage in your web browser, replacing "YourMessage" with the message you want the cow to say. The "cowsay" command is executed with your message, and the cow's response is displayed in plain text in your browser.

Using curl command(curl is a command-line tool to transfer data to or from a server, using any of the supported protocols (HTTP, FTP, IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP, or FILE):
![c3](https://github.com/poorvi1910/Cryptonite/assets/146640913/65e1ad83-6db0-41cf-b2e1-7d3602fcea78)


Curl is a command-line tool that can send and receive HTTP requests and responses
Since curl is specifically developed for HTTP requests it already uses the appropriate line-endings when making HTTP requests. However, netcat is a more general purpose program.

We now need to perform OS command injection to obtain the files we need

OS command injection is also known as shell injection. It allows an attacker to execute operating system (OS) commands on the server that is running an application, and typically fully compromise the application and its data.
![c4](https://github.com/poorvi1910/Cryptonite/assets/146640913/58d77708-777e-4eac-9698-25f6e12adb3c)

The file ‘falg.txt’ looks like our desired file. So we can cat it out and check
Initially i put the injected command ‘cat flag.txt’ but it the following error:
![c5](https://github.com/poorvi1910/Cryptonite/assets/146640913/d70ce10a-5e2f-4395-a99e-e1165b52ad75)

This is because URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20.Doing that:
![c6](https://github.com/poorvi1910/Cryptonite/assets/146640913/7d4d2b5c-eeb1-4b66-bd7a-7fdeb2dccd34)


We get the flag:
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}

What is OS command injection:
https://portswigger.net/web-security/os-command-injection
