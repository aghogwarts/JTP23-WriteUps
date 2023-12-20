# buffer overflow 0
While just checking out the program, it asked to overflow the the stack so i randomly just spammed characters and funnily enough it gave me the flag but eh i think i need to explore the challenge too

So if the program detects a segmentation error or the program crashes it prints out the flag
```
char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
```
The program also uses gets() function

```
 printf("Input: ");
  fflush(stdout);
  char buf1[100];
  gets(buf1); 
  vuln(buf1);
  printf("The program will exit now\n");
  return 0;
```
  
  ![bo2](https://github.com/nAYANko/picoCTF/assets/147973815/02f12ef4-85a2-4810-ad35-7c5aefc9767f)

What it essentially does is that it reads the input into the buffer without checking if a buffer overflow is occuring, it keeps continuing to store characters into the buffer even after the buffer ends. This can be used to break through program security. Use fget instead. This should break after a 100 charcters.

The program uses another dangerous function called strcpy which copies a string without any bounds and hence poses a risk of buffer overflow. Use strncpy copies maximum n bytes from the source. 

```
void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
```

The maximum limit of the stack is 19 and the stack overflows at 20 characters

The flag is "picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}"

![bo1](https://github.com/nAYANko/picoCTF/assets/147973815/96e9495e-5ac5-4b83-8952-1b4fbd95cbaa)
