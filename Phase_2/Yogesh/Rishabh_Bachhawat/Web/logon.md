Tried Joe with blank but that did not work.
Tried other common passwords and found that all of them worked, i.e. it was accepting all the passwords to login but did not display the flag. 
Read through the page source to get some hint
After that tried inspect element and while going through its different tabs both before and after logging in under the storage tab saw 
that there was a cookie with one tab called admin as false. Rewrote its value as True and reloded the page to get the flag.



Flag: picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}
