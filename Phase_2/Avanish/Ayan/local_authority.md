# local authority
The challenge is to be solved using inspector, in this site, the username and password is alphanumeric, unless correct pass is entered all it shows is login failed.
On inspecting the the login page, i see nothing special, on the login failed page, a secure.js file is imported

```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

This checks the username and pass at user end instead of server end. This is extremely unsafe as it provides the username and password to the user end. Here it being

username : admin

password : strongPassword098765

Putting in these values gives us the required flag

Flag : 'picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}'
