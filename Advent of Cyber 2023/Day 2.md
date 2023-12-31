# Log Analysis

In this challenge, we get a small glimpse of how Data Science can play a role in Cyber Security. We'll learn about Jupiter Notebooks and the use the 2 python libraries namely **Pandas** and **Matplotlib**. Learning from the available material in the challenge description, it can be said that Jupiter notebooks uses python to arrange data in manner which makes it easy to be analysed. The pandas library helps in arrange as set of data in series or as in a data frame. Matplotlib library allows to create a large varity of plots.

## 1
We can know the number of packets captured by the code below. As Pandas libary can read CSV(Comma Seperated Files) text files, we'll use **read_csv** to read the **_network_traffic.csv_** file into variable **df** to arrange the comma seperated text in a data frame and use count function to count the number of times an object appears in the list.
**Ans- `100`**
![Screenshot (74)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/c2d919c7-0808-4599-9681-5589583deba8)

## 2
What IP address sent the most amount of traffic during the packet capture? The code below demonstrates how it can be done. Same as before, we'll read the CSV file into the variable **df** as a data frame and then use the groupby operation from the Pandas library which further arrange data into sections of informating that we require. I only came to know about the groupby operation after searching on how I can arrange data as per IP addresses in the Pandas library. After learning a bit about this operation, as we are looking for the IP address with the most amount of traffic during packet capture, we'll group the  data by **Source** and **size**. This will gives us the answer.
**Ans- `10.10.1.4`**
![Screenshot (75)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/eecfe7d0-0556-4588-85a4-1b4d55af43d7)

## 3
For this, We'll just modify the previous grouby operation to arrange the data by **Protocol** and **size** and then sort those values.
**`Ans - ICMP`**
![Screenshot (76)](https://github.com/Wixter07/HARSHITH-JTP-2/assets/150792650/e8f282f4-8ad9-4efd-ac9b-aba01142b9ee)

The reading material on Pandas library terminologies from **codecadamey** was really helpful.




