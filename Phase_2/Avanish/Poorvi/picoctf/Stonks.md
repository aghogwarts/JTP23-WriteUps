The vuln.c file gives us a menu driven program which can display your stocks or buy new stocks depending on the option chosen. When we look at the ‘buy stocks’ function, it asks us to give an API token and uses an algorithm to buy random stocks. The hint tells us the API key might help us. Hence looking at the buy stocks function    from the code: 

![s1](https://github.com/poorvi1910/Cryptonite/assets/146640913/4d66db64-2b90-4c6d-8d42-7461c1aa2950)

What does this do?
The function checks if the provided Portfolio pointer p is valid. If it's NULL, the function returns an error code (1).It then opens a file named "api" and reads its content into the api_buf array. If the file is not found, it prints an error message and exits the program with an error code. It simulates buying stonks by repeatedly generating random shares using the pick_symbol_with_AI function and updating the linked list of stocks in the portfolio. The function dynamically allocates memory for a buffer (user_buf) to store the user's API token. It then prompts the user to enter their API token using scanf.
It then prints the entered API token to the console. This part is marked as a placeholder and is meant to be replaced with actual interaction with an API using the token.
Finally, it calls the view_portfolio function to display the updated portfolio.

We can see the small part of the code which is concerned with the API token:

![s2](https://github.com/poorvi1910/Cryptonite/assets/146640913/e716bf2e-5317-4c68-baec-4bfde55af5c3)

The syntax for printf() is : printf [format] [argument]
With that syntax in mind, if two arguments are given, the first argument will define the second argument’s data type. For instance, strings will be defined as %s, decimals will be defined as %d.
However, if one argument is given, we will either be printing out the argument or defining the format. As we can put whatever we want, we can put %s or %x. When we provide the data format, printf() wil try to find the second argument, and when it can’t find anything, it will start printing data from the stack.

For more context read up:
https://owasp.org/www-community/attacks/Format_string_attack

With this in mind if we try to put ‘%x’ for the token placeholder, we get the following:

![s3](https://github.com/poorvi1910/Cryptonite/assets/146640913/2d0721bf-c583-45ff-91c9-736707cb73a6)

Hence to get more data we can use multiple ‘%x’:

![s4](https://github.com/poorvi1910/Cryptonite/assets/146640913/4bb0c674-81cb-42c4-9abc-bffec0d695bb)

Since this is a hex value, we need to convert it:

![s5](https://github.com/poorvi1910/Cryptonite/assets/146640913/e82a7c26-1fd8-484f-b920-433b0ce35115)

We can see the flag but it looks messed up.In computing, endianness is the order or sequence of bytes of a word of digital data in computer memory or data communication which is identified by describing the impact of the "first" bytes, meaning at the smallest address or sent first.The endianess determines how data is transferred into memory. For our case, the program probably is in little-endian, where what is display is reversed.

![s6](https://github.com/poorvi1910/Cryptonite/assets/146640913/ab1b7649-8e77-411d-9975-345fb8580125)

However, by converting the data from little endian to big endian, the flag still doesn’t look right.maybe one byte can affect the next byte’s values. I started to remove hex values starting from the beginnning.Doing so:

![s7](https://github.com/poorvi1910/Cryptonite/assets/146640913/68e1730e-3842-456d-b120-ddb66270d475)

Hence the flag is: picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}
