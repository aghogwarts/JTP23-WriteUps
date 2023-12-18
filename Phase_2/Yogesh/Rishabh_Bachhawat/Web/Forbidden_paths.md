The flag was in a different directoy than the website so I needed to get to the home directory first. Using ../ returned a blank screen which and not 'Not authorised' which meant either this approach was wrong or the contents of 
the /html directory were hidden and not read by read.php. So I tried to go up to home level by doing ../../../../ but the output was still blank. I thought a bit and figured this was beacause there was nothing for the read.php
read in the address I had provided. So it added /flag and it worked ../../../../flag.txt.

Flag: picoCTF{7h3_p47h_70_5ucc355_6db46514}
