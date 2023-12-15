# miniRSA
The first thing i realised in this file since the cyphertext is much smaller than N, then decoded text has to be an even smaller number, the key is very small, and after looking up i tried to cube root the given cypher text.

Found the code to get root of a number from https://riptutorial.com/python/example/8751/computing-large-integer-roots#google_vignette 

```
def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1
```
Now assigning values... the final code to be used is,
```
# miniRSA solved
import binascii

n =29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
c =2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125 

def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

for i in range(4000):
    st = ("{:x}".format(nth_root(c+i*n,3)))
    if "7069636f" in st: # pico in hex
        print(st)
        print(binascii.unhexlify(st))
```
Here first we import binascii which is a binany to ascii converter the we assign the given values to n and c, followed by the root code, this is followed by a for loop which converts the cube root of c+i*n to hex, then we search for keyword pico in it print the hex format and then the ascii.

You can do this without binascii using an external converter.

Flag : 'picoCTF{n33d_a_lArg3r_e_606ce004}'





