## additional writeups

### Forensics

#### sleuthkit intro 

opened the challenge     
downloaded the file using `wget` command         
used `cat disk.img.gz` . Didn't work       
used `nc saturn.picoctf.net 64605 ` . It started asking about length of linux partition        
went through the primer for help        
learnt that you have to use the mmls command     
used `mmls disk.image.gz` . Didn't work      
used `mmls disk.image` . Gave data      
used `nc saturn.picoctf.net 64605` . Entered the length of the linux distribution given     
got the flag    
```  
flag - picoCTF{mm15_f7w!}  
```

#### sleuthkit apprentice

opened the challenge     
downloaded the file using `wget`      
extracted the file using `gunzip`      
used `mmls` command       
found the fourth partition to be the most lengthiest      
read through the basics of disk analysis in primer      
used `fls -o 360448 disk.flag.img `        
used `fls -o 360448 disk.flag.img 1995` to enter root directory     
used `fls -o 360448 disk.flag.img 2371` to enter my_folder directory      
used `icat -o 360448 disk.flag.img 2371` to read the data in my_folder     
got the flag     
```
flag - picoCTF{by73_5urf3r_adac6cb4}
```

#### disk,disk,sleuth! ||

opened the challenge    
downloaded the file using `wget` command    
extracted the file using `gunzip` command    
used `mmls ` command       
found the lengthiest file and used `fls` command     
used `fls ` command to enter root directory since it has the highest probability of flag    
used `icat ` command to read the content in the root directory     
got the flag     
```
flag - picoCTF{f0r3ns1c4t0r_n0v1c3_ff27f139}
```

### cryptography

#### Mod 26

opened the challenge   
created a file name hello using `touch hello`   
used `cat > hello << EOF    
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}    
EOF`   
used `cat hello | tr 'A-Za-z' 'N-ZA-Mn-za-m`     
got the flag     
```
flag - picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}
```

#### The Numbers 

opened the challenge    
the numbers are in a substitution cipher  
converted them   
got the flag   
```
flag -PicoCTF{THENUMBERSMASON}
```

#### 13

openrd the challenge   
created a file named hello using `touch hello`  
used `cat > hello << EOF    
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}   
EOF`    
used `cat hello | tr 'A-Za-z' 'N-ZA-Mn-za-m`
got the flag   
```
flag - picoCTF{not_too_bad_of_a_problem} 
```
