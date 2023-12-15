We have been given  python code which basically is a menu driven program that works as an arcane calculator and theres a key you need to input to get access to the full version. 

We are checking the input key against the predefined key character by character.We have been give the static part of the key that is "picoCTF{1n_7h3_|<3y_of_" and the third part “}”.

To find dynamic part:

![kg1](https://github.com/poorvi1910/Cryptonite/assets/146640913/92bc1160-def8-475a-9927-e990bf3ebcd2)

hashlib.sha256(username_trial).hexdigest():
1) hashlib.sha256 is a function from the hashlib module in Python that applies the SHA-256 hashing algorithm to the provided input.
2) username_trial is a string representing the username.
3) .hexdigest() converts the hash object to a hexadecimal representation.
  
The result of the hash is a string of characters (hexadecimal).
[4] is used to access the character at index 4 of the hexadecimal string. This is a specific character of the hash.
Hence the line is checking whether the i-th character of the key string is not equal to the character at index 4 of the hexadecimal representation of the SHA-256 hash of the username.	
So to get the key we can just print what the hashlib function does 

![kg2](https://github.com/poorvi1910/Cryptonite/assets/146640913/9175e0ef-7144-4e3b-8af8-6a9ba55e823b)

Combining all the key parts we get the flag:
picoCTF{1n_7h3_|<3y_of_e584b363}
