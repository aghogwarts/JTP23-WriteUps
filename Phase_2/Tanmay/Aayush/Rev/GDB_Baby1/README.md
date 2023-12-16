# Debugger0_a Challenge Writeup

## Challenge Overview

The Debugger0_a challenge involves reverse engineering a program using IDA Freeware to extract a flag from the disassembled code.

## Code Analysis

```assembly
; Attributes: bp-based frame

; int __fastcall main(int argc, const char **argv, const char **envp)
public main
main proc near

var_10= qword ptr -10h
var_4= dword ptr -4

; __unwind {
endbr64
push    rbp
mov     rbp, rsp
mov     [rbp+var_4], edi
mov     [rbp+var_10], rsi
mov     eax, 86342h
pop     rbp
retn
; } // starts at 1129
main endp
```

The disassembled code reveals that the value 86342h is being assigned to the eax register.Flag ExtractionConverting 86342h to decimal gives 549698. 

Therefore, the extracted flag is: `picoCTF{549698}`
