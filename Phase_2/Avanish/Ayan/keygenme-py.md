# picoctf

# keygenme-py

To obtain the flag, we must determine which key_part_dynamic1_trial. Examining the code, I discovered that the check_key function selects a specific character by indexing to a specific location on the string after receiving the hexdigest of the sha256 hash of "FREEMAN".


Then use a for loop to find out the hexdigest of the sha256 hashes of b"FREEMAN" to get the characters in the given indices.
Print the final key.


```
import hashlib
import base64

username_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"


indices = [4,5,3,6,2,7,1,8]
key_part_dynamic2_trial = ""
#hashlib.sha256(username_trial).hexdigest()[4] == key_part_dynamic1_trial[0]

for i in indices:
    key_part_dynamic2_trial += hashlib.sha256(username_trial).hexdigest()[i]

key_full_template_trial = key_part_static1_trial + key_part_dynamic2_trial + key_part_static2_trial
print(key_full_template_trial)
```
