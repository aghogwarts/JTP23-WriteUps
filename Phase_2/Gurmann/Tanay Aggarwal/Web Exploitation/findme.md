We launch an instance:

![image](https://github.com/itstanayhere/phase2_2/assets/147296398/d4785c47-c43b-4166-9a41-33234e1d7d5a)

We type in the given username and password.

![image](https://github.com/itstanayhere/phase2_2/assets/147296398/f11e2cfa-e843-479a-bc37-e424beb7d192)

Upon hitting the button:

![image](https://github.com/itstanayhere/phase2_2/assets/147296398/e97eec68-64d1-45dd-8271-1da53dabe974)

As a hint, it was given to look out for redirects.

![image](https://github.com/itstanayhere/phase2_2/assets/147296398/63af1b09-04e2-40dd-aed6-20c84cc1456b)

We observe that the two redirects here are in base64. All we do is decode them using base64 --decode and get our flag.

picoCTF{proxies_all_the_way_be716d8e} 

(might differ as the instances in the writeup and actual working are different)
