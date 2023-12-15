## babygame01
after inspecting code i realised that the flag will be pritned if i enter 'p' when @ is at -4 from the top left corner
![babygame01T](https://github.com/aghogwarts/JTP23-WriteUps/assets/107710230/1978e258-b2da-4819-b01a-b2c3f2c45377)


## bufferoverflow0

Buffer Overflow 0

In the following CTF after doing a bit of research I found that the gets function is prone to buffer overflow. If we exceed the storage capacity
of gets it will overflow into different memory location. The SIGSEGV (Segmentation function) checks if there is any overflow beyond the bounds.
If we input a large number of characters and press enter it causes buffer overflow and we get the value of the flag.
<img width="733" alt="Screenshot 2023-11-14 at 1 40 18 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/90363392-850b-4145-9d81-e4c9129599ad">


## stonks

In the following file after going through it we see that the user_buf is vulnerable. This is because we can use format specifier in the input which will prompt it to print all the value that the stack has. %x will return hex values from the stack which can help us to identify the flag.
<img width="487" alt="Screenshot 2023-11-15 at 12 43 14 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/4661e630-e270-4424-81d5-50e6495415b2">
By flooding it with %x we get the hex values.
<img width="565" alt="Screenshot 2023-11-15 at 12 45 31 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/b3cfd187-9fe0-4246-8612-657634f5e247">
After converting the hex value to ascii we get the flag however it seems to be in some reverse order. After looking it up it is in little endian. We can convert this back to big endian through an online compiler and get the flag
<img width="565" alt="Screenshot 2023-11-15 at 12 45 41 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/31cadbf7-ddfc-4082-bbff-392d84e8826c">

