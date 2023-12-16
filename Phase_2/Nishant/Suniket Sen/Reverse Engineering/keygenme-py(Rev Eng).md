# keygenme-py  
So for this on all I did was just read the code thorughly.  
I learnt a bit about hashlib, hexdigest, fernet and all to comprehend and try to understand what to do...  
So in the *check_code* function, we were given a bunch of indices which we had to extract from our sha256 hash objects converted to hex strings using print function and that ended up being the missing part of the flag.  
I replaced the x's with the hex digits and got the flag!  

The flag is _picoCTF{1n_7h3_|<3y_of_f911a486}_  
