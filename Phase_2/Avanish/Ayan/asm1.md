# asm1
We are given an assembly code and we need to put in 0x2e0 (=736) and find whats the result, I have explained my calculations in comments,
```
asm1:
	<+0>:	push   ebp ; 0x2e0 = 736
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb ; 0x3fb = 1019 
	<+10>:	jg     0x512 <asm1+37> ; jump if 736>1019 which is false
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x280 ; 0x280 = 640
	<+19>:	jne    0x50a <asm1+29> ; jump if 736 != 640 which is true
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xa
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8] ; eax = 736 ; store 736 to eax register
	<+32>:	sub    eax,0xa ; = 726 ; 736-10
	<+35>:	jmp    0x529 <asm1+60> ; jump to asm1+60 which is the pop statement
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x559
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xa
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xa
	<+60>:	pop    ebp  ; 726 = 0x2d6
	<+61>:	ret    
```

Flag : 0x2d6
