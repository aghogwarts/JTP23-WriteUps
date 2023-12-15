## ARMssembly

According to the hint given in the question the hex values of the given number will be the flag. I did not understand the assembly code so i converted the numbers to their hex values through an online converter and tried them as flags. The second number proved to be the flag.


<img width="374" alt="Screenshot 2023-11-14 at 11 15 37 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/e7e1d8da-ae22-4b24-8a89-e5a8b659ec36">

<img width="374" alt="Screenshot 2023-11-14 at 11 15 46 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/feb7ad99-bdbc-41b9-aa97-cefd6b1753c7">

## GDB babysteps1

First installed GDB on to the machine. The file was a ELF 64bit LSB pie executable which is used to store binaries in linux. After some reading online i used the lay next command to interact with the file. We can see the value assigned to eax is 0x86342 which is in hex. Converting this to decimal we get the flag.


<img width="956" alt="Screenshot 2023-11-15 at 11 16 56 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/c415e245-2532-473e-939a-0ae2078ac018">
<img width="946" alt="Screenshot 2023-11-15 at 11 17 35 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/e676dbfc-718c-46ac-905a-f2c0ed3f2a29">
<img width="1187" alt="Screenshot 2023-11-15 at 11 17 11 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/5409c1c2-4162-4efa-a0a3-25fbe42440b8">
<img width="494" alt="Screenshot 2023-11-15 at 11 38 10 PM" src="https://github.com/nsjss1207/Crypto/assets/107710230/8cd3bf04-13d4-46ac-a101-04bd1be682ad">

## keygenme-py
In the given code the check_key() function checks whether the redacted key is correct or not.So if we are able to reverse engineer that portion we will get the key value. What that function checks is if the key value is equal to the SHA256 of the character of the username of the specified index by converting it into hex.

<img width="582" alt="Screenshot 2023-11-16 at 12 48 59 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/1a0db75b-db29-47b3-a4b2-1cbf973fbdd6">

(consulted on how to write the reverse engineered script)
<img width="793" alt="Screenshot 2023-11-16 at 12 47 27 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/578dba5c-2e42-4f3d-8c3e-bc294bfbdfdd">

<img width="167" alt="Screenshot 2023-11-16 at 12 21 44 AM" src="https://github.com/nsjss1207/Crypto/assets/107710230/cce2df5f-d45f-46bb-8bd7-a83dd0690ba4">

