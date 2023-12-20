cut -d ' ' -f2 access.log | sort |uniq -c
![image](https://github.com/CoderZonora/AdventOfCyber2023/assets/140229408/1d1ae0af-9925-4dd4-bebc-4aa8d4ba8441)

cut -d ' ' -f3 access.log |cut -d ':' -f1| sort | uniq | wc


cut -d ' ' -f3 access.log |cut -d ':' -f1| sort | uniq -c | sort -r followed by cat access.log | grep partnerservices.getmicrosoftkey.com

![image](https://github.com/CoderZonora/AdventOfCyber2023/assets/140229408/2d103a38-b4e1-483e-95db-7e3b60624e49)

cut -d ' ' -f3 access.log |cut -d ':' -f1| sort | uniq -c | sort 

cat access.log | grep frostlings.bigbadstash.thm

![image](https://github.com/CoderZonora/AdventOfCyber2023/assets/140229408/23ecb023-42c8-4826-ba45-554204eea98a)

cat access.log | grep frostlings.bigbadstash.thm 
![image](https://github.com/CoderZonora/AdventOfCyber2023/assets/140229408/f4d0d604-bb1b-45ea-87dd-8857d90a8795)

Extracting the text sent, converting from base64 to ascii and grep for the flag.
cat access.log | grep frostlings.bigbadstash.thm | cut -d ' ' -f5 |cut -d '=' -f2 | base64 --decode |grep THM{



Flag: THM{a_gift_for_you_awesome_analyst!}
