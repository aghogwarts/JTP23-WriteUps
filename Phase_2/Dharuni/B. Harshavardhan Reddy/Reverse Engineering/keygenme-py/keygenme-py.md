### Description

[keygenme-trial.py](./keygenme-trial.py)

### Approach

Open the file `cat keygenme-trail.py` and read the python script

We already got half of the flag from this part of code.
```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
we need to find the key_part_dynamic1_trial of 8 len string in form of "xxxxxxxx".to complete picoCTF{1n_7h3_|<3y_of_xxxxxxxx}

Check this part of py code. It has exact 8 parts of similar code. if statements in the below where x is in the order 45362718.

```python
  # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

```

As the amount of if statements is equal to the remaining characters needed to find, I found the values that key[i] needs to be equal to using the code from vivian-dai [writeup](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/a6e0f9affc9a105c107abf820aff75e445046799/Reverse%20Engineering/keygenme-py/keygenme-py.md)

```python
import hashlib
username_trial = "SCHOFIELD"
bUsername_trial = b"SCHOFIELD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

#I used bUsername_trial because enter_liscence used it as well but after testing afterwards, they output the same answer
print(hashlib.sha256(bUsername_trial).hexdigest()[4]) 
print(hashlib.sha256(bUsername_trial).hexdigest()[5])
print(hashlib.sha256(bUsername_trial).hexdigest()[3])
print(hashlib.sha256(bUsername_trial).hexdigest()[6])
print(hashlib.sha256(bUsername_trial).hexdigest()[2])
print(hashlib.sha256(bUsername_trial).hexdigest()[7])
print(hashlib.sha256(bUsername_trial).hexdigest()[1])
print(hashlib.sha256(bUsername_trial).hexdigest()[8])
```
write the above script in .py [file](./dynamicpart.py) using nano in terminal: `nano dynamicpart.py`

run the script using python3: `python3 dynamicpart.py`

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/db531b2f-2412-42c7-b6fe-695524e6ad4c)

run the [keygenme-trial.py](./keygenme-trial.py) script: `python3 keygenme-trial.py` to check the if the key is correct.

![image](https://github.com/Harsha-creates/PicoCTF/assets/68886253/d3bbd894-9970-47ed-8504-860bcb128d8d)

**Flag:** picoCTF{1n_7h3_|<3y_of_e584b363}






