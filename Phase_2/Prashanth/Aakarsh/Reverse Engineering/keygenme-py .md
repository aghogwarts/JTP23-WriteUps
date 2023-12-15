### Approach used 
The thing which gives us a lead is this :-

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/427c2deb-00a1-4c86-9dd5-d91607a95cea)

* This shows us that we have already got half of the flag i.e `"picoCTF{1n_7h3_|<3y_of_"` and we just have to find `"xxxxxxxx"` part.
```
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```
* We can see that here the user has to input the license key and also if `check_key(user_key, bUsername_trial)` function returns true then we will get the flag.

* Next we see `    if len(key) != len(key_full_template_trial):
        return False ` which basically checks if the length of the key and our flag is same or not.
```
import hashlib
key_part_staticl_trial = "picoCTF{1n_7h3_|<3y_of_"
#key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
temp=hashlib. sha256(b"PRITCHARD") . hexdigest ()
key_part_dynamic1_trial = temp[4]+temp[5]+temp[3]+temp[6]+temp[2]+temp[7]+temp[1]+temp[8]
key_full_template_trial = key_part_staticl_trial + key_part_dynamicl_trial + key_part_static2_trial
print(key_full_template_trial)
```
A code will be written like the above one to get the flag.

### Flag
> picoCTF{1n_7h3_|<3y_of_54ef6292}
