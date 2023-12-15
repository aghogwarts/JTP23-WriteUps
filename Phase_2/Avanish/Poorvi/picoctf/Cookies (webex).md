When we click on the website and inspect the cookies on the site, it shows value of ‘-1’ for the ‘name’ field. If we change the value to something, say ‘2’, the page shows ‘I love oatmeal raisin cookies!’. Hence we realise that we need to keep changing the values to get our flag. If the web page matches a valid ‘cookie name’, it redirects the browser to “http://mercury.picoctf.net:<port>/check” and changes the cookie.The web page checks the cookie set previously and, based on the cookie, it generates a custom message.

 When we get to 18, our flag gets printed:

picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}
