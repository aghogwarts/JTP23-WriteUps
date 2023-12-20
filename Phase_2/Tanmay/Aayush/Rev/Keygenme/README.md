# Keygen Challenge Writeup

## Challenge Overview

The keygen challenge involves cracking a key generation algorithm to obtain the flag. The key is divided into three parts, with the middle part being dynamic and dependent on the sha256 hash of a given username.

## Code Snippet Analysis

```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

username_trial = "PRITCHARD"
bUsername_trial = b"PRITCHARD"
```

The code snippet above defines the static and dynamic parts of the key and the username used for key generation.
Key Generation LogicThe check_key function compares the entered license with three key parts linearly. The dynamic key part is checked against the sha256 encoded bUsername_trial in a random order, while keeping the key array index increasing linearly.Solution Script

```python
import hashlib

username_trial = b"PRITCHARD"
dynamic_key_part = (
    hashlib.sha256(username_trial).hexdigest()[4] +
    hashlib.sha256(username_trial).hexdigest()[5] +
    hashlib.sha256(username_trial).hexdigest()[3] +
    hashlib.sha256(username_trial).hexdigest()[6] +
    hashlib.sha256(username_trial).hexdigest()[2] +
    hashlib.sha256(username_trial).hexdigest()[7] +
    hashlib.sha256(username_trial).hexdigest()[1] +
    hashlib.sha256(username_trial).hexdigest()[8]
)

key = key_part_static1_trial + dynamic_key_part + key_part_static2_trial

print(key)
```

The solution script extracts the dynamic key part by rearranging characters from the sha256 hash of bUsername_trial. Concatenating all key parts yields the final flag.
