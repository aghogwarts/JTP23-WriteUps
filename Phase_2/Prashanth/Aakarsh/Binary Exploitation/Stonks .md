### Approach used
After observing 'vuln.c', we can only see one vulnerability which we can use to break in cause it only has 'printf(user_buf)' and no format string like '%s' or something.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/459bb8cf-afab-4dc9-853f-66c0d1b0a3ef)

Now we will use the command given in the question 'nc mercury.picoctf.net 53437' and first type 1 to buy some stonks and type any random thing in api token. We can also check 2nd option.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/131944e4-11dd-4223-ac52-d9ff8c4bde28)

This time we will choose option 1 again but in the api token we will use a format string like '%p'.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/5c9a3840-209d-4543-87bc-056f26984552)

We will get a code in the 'buying stonks with token' and now we just have to type %p many times to get the flag.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/26fe0714-ee29-4e34-ab1d-8866c5608f05)

Now we got the token but we have to decode it so for that we will go to [Cyber Chef](https://gchq.github.io/CyberChef/) and use from hex recipe and paste the token here.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/4558ba03-6fc0-4723-aaae-d4dce336172e)

We can see there something written in the form of flag so first we will remove unnecessary terms.

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/dc16d4c7-e942-418b-8e8a-f5890329c4cd)

We can see that we have almost got the flag but it is in reverse so we will use swap endianess to reverse it

![image](https://github.com/UselessAaka/picoCTF-Writeups/assets/148384618/705cc218-1af7-4cf6-bf88-d2712b80dadb)

We can see we have got the flag.

### Flag
> picoCTF{I_l05t_4ll_my_m0n3y_bdc425ea}

