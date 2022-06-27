"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


length =  {}
for numbers in calls:
    first = numbers[0]
    second = numbers[1]
    sec = int(numbers[-1])
  
    if first not in length:
        length[first] = sec
    else:
        sec1 = length.get(first)
        sum = sec1 + sec
        length.update([(first, sum)])
    if second not in length:
        length[second] = sec
    else:
        sec1 = length.get(second)
        sum = sec1 + sec
        length.update([(second, sum)])
longest_number = max(length, key=length.get)  
longest_sec = length[longest_number]
  

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_number, longest_sec)) 



