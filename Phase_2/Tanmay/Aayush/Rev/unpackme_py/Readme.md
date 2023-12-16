# UnpackMe Challenge Writeup

## Unpacking the Flag

While examining the `unpackme.flag.py` file, my focus was on the `payload` and `key_str`. The payload, encoded in base64 and decrypted with the Fernet symmetric encryption, revealed the following plain string:

```python
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_85f5d0ac}')
else:
  print('That password is incorrect.')
```

# Unveiling the Flag

By altering the code to print the plain string, 

I obtained the flag: `picoCTF{175_chr157m45_85f5d0ac}`