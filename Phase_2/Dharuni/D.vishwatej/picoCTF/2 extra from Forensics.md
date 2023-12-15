# Wireshark twoo twooo two twoo

## GOAL
Can you find the flag?
> given a .pcapng file named shark2.pcapng

### WRITE UP

We first open the file using a software called as wireshark.

The hint suggests us to look at the traffic. We can analyse it by using the protocol hierarchy feature in the statistics tab.

This shows us the type of protocols which were of main interest by showing the precentage of packets.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/44787b05-8f6b-489e-845c-fbde8c7ae539)

We can see that the dns and http protocol have high percentages.

First we look at the HTTP protocol,

As we scroll through these, we find many of them containing info as 'GET flag'.

If we right click on those files and follow them using the HTTP stream we can find the data present in them.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/a9028995-f92c-4b1a-8712-aeb8d87445a6)


All of these consist of a flag, which are fake ones or are given for misleading.

>~~just got to know , those are called as red herrings~~

Now we look in the dns category, by applying dns as filtering criteria,

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/6c7358ae-c0f7-4ae6-a608-1c5fd828c7b8)


We can find the conversations from source 8.8.8.8 and 192.168.38.104 .

> note:- 8.8.8.8 is the google's public DNS , thus it may be a valid conversation.

 The unique DNS ip address as 18.217.1.57 seems suspicious and may contain the flag.

It randomly throws out communications with the googles DNS to mask it malicious exfiltration.

> EXFILTRATION:- The unauthorized transfer of information from an information system.

 A left click on the source tab categorises all packages from a source together.


 ![Screenshot from 2023-12-14 18-35-48](https://github.com/vishwatejD/picoCTF/assets/141154035/5393b82c-9251-406a-a600-278e27e0c0c5)

checking at the info tab and the dns query name we can figure out that it is decoded in base 64
> it has a ==

Manually taking down the unique dns query names converting the unique strings into ascii text we get the flag .

>UNIQUE STRING:- cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==


FLAG:- picoCTF{dns_3xf1l_ftw_deadbeef}

### Alternative flag retrieving method

It can be done by using a command called `$ tshark ` in the terminal.

I first used the  command tshark -h to know the options to be applied.

Then i used the command `$ tshark -r shark2.pcapng -T fields -e dns.qry.name -Y "ip.src == 18.217.1.57"`

I got the dns query names of the communications with the required ip address, but many of them were empty, to filter out the empty names we have to put the required filter under 

` -Y` in the command.

thus new command `$ tshark -r shark2.pcapng -T fields -e dns.qry.name -Y "dns.qry.name != ' ' && ip.src == 18.217.1.57"`

> NOTE:- we are mentioning that the dns.qry.name shoud not be equal to ' '. ! denotes not.


![image](https://github.com/vishwatejD/picoCTF/assets/141154035/f0eaa57f-0658-4e99-87ae-d53f09e54c3c)

Now we must isolate the required part which is after the period symbol.
Thus we can use the grep command on the output to filter it.

We use extended grep or `$ grep -oE "^[^.]*`, this specifies the command to filter out the part only before the period and print it.

Now if we apply uniq command we can eliminate the repeated outputs. 

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/e7c3708b-c9e8-426e-8dd5-32524f5f3f84)

Now apllying base64 -d command we can decrypt the output to ascii.

Thus we get the flag.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/a4709cae-41df-4db8-867b-81842fde4b91)

___

# Lookey here
## goal
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data here.
> given a file named anthem.flag .txt which contains the flag or information for the flag.

### Write up

The hint says to look up for known prefix of flag. The known prefix is picoCTF{XXXXXX}.

So we open the file and look up for the string picoCTF.

**Another method** is to use terminal to find the pattern of strings using the grep command.

We open the directory where the file is downloaded and use the following command.

`$ cat anthem.flag.txt | grep "picoCTF"`

The above command first reads the text file and then the grep command finds the picoCTF string and prints the line.

![image](https://github.com/vishwatejD/picoCTF/assets/141154035/f3234183-c1e1-4a13-b039-a887e242c668)

FLAG:- picoCTF{gr3p_15_@w3s0m3_4c479940}
