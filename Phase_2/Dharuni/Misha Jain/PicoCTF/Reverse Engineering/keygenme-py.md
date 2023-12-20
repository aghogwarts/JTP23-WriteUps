<font size = '4'>
<p align = 'center'>
<b>
PicoCTF - Keygenme-py Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup details the solution to the "Keygenme-py" reverse engineering challenge from PicoCTF. The challenge involves reverse engineering a Python application to generate a valid license key.

<b>Author:</b> Misha Jain

<b>Date:</b> November 08, 2023

<b>Tools Used:</b><br>
- Python
- Text Editor

<b>Challenge Description:</b><br>
The "keygenme-py" challenge requires reverse engineering a Python program. The goal is to understand the logic of the program and generate a valid license key.

<b>Exploitation:</b><br>
1. Open the provided Python script, "keygenme.py," using a text editor or IDE. We can see that three python libraries have been imported.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Python_Libraries.png>)

</p><br>

- Hashlib:<br> The hashlib library in Python is a standard library module that provides a secure and efficient way to work with various hash functions. Hash functions are algorithms that take an input (or "message") and return a fixed-size string of characters, which is typically a hexadecimal number. Hash functions are commonly used in cryptography, data integrity verification, and various other applications.<br><br>
- Cryptography.fernet:<br> The cryptography.fernet module in Python is part of the cryptography library, which is a popular and robust library for cryptographic operations. The Fernet class within the cryptography.fernet module is designed for working with the Fernet symmetric key encryption scheme. <br><br>
- Base64:<br> The base64 module is a standard library module that provides functions to encode binary data as ASCII text and decode the encoded text back into binary data. Base64 is a binary-to-text encoding scheme that is commonly used for tasks such as encoding binary data (e.g., images, binary files) into a format that can be safely transported and stored as text, such as in email messages or within data formats that do not support binary data.<br><br>

2. Examine the script to understand its logic. The script contains our username ("PRITCHARD"), and the username but in bytes.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Username.png>)

</p><br>

3. The script contains a template for the key, including a static part ("picoCTF{1n_7h3_|<3y_of_"), a dynamic part ("xxxxxxxx"), and a closing static part ("}"). The goal is to find the correct dynamic part.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Key.png>)

</p><br>

4. The script references a dictionary called "star_db_trial" that appears to be unrelated to the key generation process. We can ignore it.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Dictionary.png>)

</p><br>

5. The menu_trial() function shows that we have four menu options - to estimate mana burn, estimate vector, enter a license key, or exit. We are interested in the "Enter License Key" option.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Menu_Trial.png>)

</p><br>

6. The "check_key" function appears to validate the license key. It first compares the length of the key inputted by the user to the length of the key template ("picoCTF{1n_7h3_|<3y_of_xxxxxxxx}"). Then, it compares the first 22 characters with the key template. Thus, our expected key follows the template.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Initial_Conditions.png>)

</p><br>

7. Create a Python script to calculate the dynamic part of the key based on the provided username. You can use the hashlib library to compute the SHA-256 hash of the username and extract the required characters to form the dynamic part.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Python_Code.png>)

</p><br>

8. Upon executing the code, we get the key to be "picoCTF{1n_7h3_|<3y_of_54ef6292}". We can check if this is correct by running the program and inputting the code.<br>

<p align = 'center'>

![](<Pictures/Keygenme-py - Key_Test.png>)

</p><br>

<b>Conclusion:</b><br>
The "Keygenme-py" challenge was a reverse engineering exercise that required understanding the logic of a Python script to generate a valid license key. It involved reverse engineering the hashing process to extract the dynamic key part and constructing a valid license key.

</font>