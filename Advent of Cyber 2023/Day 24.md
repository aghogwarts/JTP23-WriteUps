# Mobile Analysis

We'll be learning a bit about digital forensics and the use of Autopsy Digital Forensics tool. Acquisiton of digital evidence will be the key to this challenge. We'll first open the **McGreedy.aut** file on Autopsy and try answering the challenge questions.

## One of the photos contains a flag. What is it?

We can go look for the image in the listings from the **Images** section in **By Extension**. There are a ton of images but there were 3 images with texts written on black board. One of those images had the flag.

![Screenshot (120)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/37db5eb8-655e-4ddb-a935-8a4aaf16f1e5)

**Ans- `THM{DIGITAL_FORENSICS}`**

## What name does Tracy use to save Detective Frost-eau’s phone number?

This can be found in contacts listings from **Communication Accounts**.

**Ans- `Detective Carrot-Nose`**

## One SMS exchanged with Van Sprinkles contains a password. What is it?

We need to first identify Van Sprinkles contact number which can be found in the contacts listing. The number is **+299 40 68 54**. Now we'll go to the messages listing to look for the SMS exchange containing the password. Scrolling through the texts, we can see that Van Sprinkles says that he is about to send a password and does so as shown below.

![Screenshot (121)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/fccc99e8-6501-46c4-a0f1-92305603c0df)


**Ans- `chee7AQu`**


Since learning about this tool in the challenge description, I downloaded it since it would be of great use in solving future challenges.
