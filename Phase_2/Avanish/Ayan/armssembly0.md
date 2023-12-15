# ARMssembly 0
Here we have file which performs a variety of functions with 2 arguments, and we are asked to find the result of the code.


I didn't understand some of this code but in the main function we need to focus on the x0 registeries,


`ldr	x0, [x29, 32] ; argument0`


x0 is a 64-bit register


`add	x0, x0, 8 ; this increments the argument0 by 8bytes we call it argument1`


` ldr	x0, [x0] ; this loads the x0 value into the x0 register which is a string, x0= "4110761777" `


In the past, it runs atoi which converts ascii to integer as in it makes the string in x0 into an integer


`mov	w19, w0 ; this moves w0 into w19, w0 is the lower 32 bits of x0 (same register lower half), w19 =4110761777`


after this we are skipping forward to argument2 and we are adding 8 bytes
``` add	x0, x0, 16 ; argument2
	ldr	x0, [x0] ; x0 = (4110761777) "4004594377" , dont know if the first part in cleared or still there
	bl	atoi ; another ascii to interger
	mov	w1, w0 ; moves w0 to w1 hence now w1 = 4004594377
	mov	w0, w19 ; moves w19 to w0, we know w19 is argument1, w19 = 4110761777 so now w0 = 4110761777  
 ```
after this func1 function in called,
```
func1:
	sub	sp, sp, #16 ; creates space
	str	w0, [sp, 12] ; stores w0 to sp12, sp12 = 4110761777
	str	w1, [sp, 8] ; stores w1 to sp8, sp8 =  4004594377
	ldr	w1, [sp, 12] ; loads sp12 into w1, w1 = 4110761777
	ldr	w0, [sp, 8] ; loads sp8 into w0, w0 = 4004594377
	cmp	w1, w0 ; compares the 2
	bls	.L2 
	ldr	w0, [sp, 12] ; w0 = 4110761777
	b	.L3
 ```
then we move to L3 function which just returns and we get back to the main function

```
mov	w1, w0 ; w0=w1=4110761777
	adrp	x0, .LC0 ; adrp works like ldr but it broadens the scope by using a function her LC0
	add	x0, x0, :lo12:.LC0 ; this encodes the argument, then just prints out our integer value
	bl	printf ; Result = 4110761777
 ```
Now the rest of the code is mostly doing clean-up,
Result 4110761777 in hex is 0xf5053f31 hence flag is "picoctf{f5053f31}"
.

 
