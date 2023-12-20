# MacroHard WeakEdge 
Looking into the details of the challenge i found out the this challenge is to show us that all ppts are zip files that can e unzipped for data,

```
nayanko@Ayan:~/Desktop/MacroHard WeakEdge$ ls
'Forensics is fun.pptm'
nayanko@Ayan:~/Desktop/MacroHard WeakEdge$ unzip 'Forensics is fun.pptm'
Archive:  Forensics is fun.pptm
  inflating: [Content_Types].xml     
 ...
uznipping and all
...       
  inflating: ppt/slideMasters/hidden  
nayanko@Ayan:~/Desktop/MacroHard WeakEdge$ ls
'[Content_Types].xml'   docProps  'Forensics is fun.pptm'   ppt   _rels
nayanko@Ayan:~/Desktop/MacroHard WeakEdge$ cd ppt
nayanko@Ayan:~/Desktop/MacroHard WeakEdge/ppt$ ls
presentation.xml  presProps.xml  _rels  slideLayouts  slideMasters  slides  tableStyles.xml  theme  vbaProject.bin  viewProps.xml
nayanko@Ayan:~/Desktop/MacroHard WeakEdge/ppt$ cd slideMasters
nayanko@Ayan:~/Desktop/MacroHard WeakEdge/ppt/slideMasters$ ls
hidden  _rels  slideMaster1.xml
nayanko@Ayan:~/Desktop/MacroHard WeakEdge/ppt/slideMasters$ cat hidden
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
nayanko@Ayan:~/Desktop/MacroHard WeakEdge/ppt/slideMasters$ cat hidden | sed 's/ //g'
ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ
nayanko@Ayan:~/Desktop/MacroHard WeakEdge/ppt/slideMasters$ cat hidden | sed 's/ //g' | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
```

After a lot of file navigation, we get a hidden file after we cat that out, we get a flag which seems to be base64 encoded with spaces, we use a utility called sed which is used to replace intances of characters with other characters, start with an s which stands for substitute then / // which tells that a space is to be replaced with nothing and then g to do this globally otherwise it just does it for the first instance.
Then we base64 decode it to get out flag which is 

" picoCTF{D1d_u_kn0w_ppts_r_z1p5} "

