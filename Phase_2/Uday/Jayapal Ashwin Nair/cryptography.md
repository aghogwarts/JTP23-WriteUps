### Minirsa

the ciphertext presented the following information

```
N: 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673

e: 3

ciphertext (c): 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125
```
with N bigger than M with small e,  $\normalsize  (m^e)\mod n$ will become $\normalsize m^e$ as it's smaller than n. So the cipertext will be $c = m^e$ where we can get $\LARGE m = c^\dfrac{1}{e}$ .

The M then can be converted back to ascii character
flag: picoCTF{n33d_a_lArg3r_e_606ce004}

---

### mod1/mod2

Mod1 iis starightforward, just have to apply modulo function using 37 on all numbers provided and then match them wtih aplhabet,digits and underscore.

flag: picoCTF{R0UND_N_R0UND_B6B25531}

mod2 is also pretty straightforward where we hard to find inverse modulo of given numbers and match them

flag: picoCTF{1NV3R53LY_H4RD_8A05D939}

---

### New Caesar

in the given python script it first shifts the alphabets like usual, then it takes each character at a time, converting them into binary which is split into first and last 4 bits which are then converted to decimal and used as indexing in the list aplhabet.After reversing the code we can get the flag

flag: picoCTF{et_tu?_23217b54456fb10e908b5e87c6e89156}

---
