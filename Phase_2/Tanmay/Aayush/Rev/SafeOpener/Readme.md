# Safe Opener Challenge Writeup

## Analyzing SafeOpener.java

In the pursuit of solving the Safe Opener challenge, my attention was drawn to the `SafeOpener.java` file. Within this file, a method named `openSafe` caught my eye, specifically the comparison of the input password with the encoded key:

```java
public static boolean openSafe(String password) {
    String encodedKey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";

    if (password.equals(encodedKey)) {
        System.out.println("Sesame open");
        return true;
    }
}

```

Decoding the Encoded KeyUpon further inspection, I recognized that the encodedKey string was base64-encoded. Utilizing this insight, I decoded the string and revealed the actual key:
```plaintext 
pl3as3_l3t_m3_1nt0_th3_saf3
```
FlagThe decoded key, formatted as the flag, is: `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`