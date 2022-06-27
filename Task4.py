"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from cgitb import text
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing = []
incoming_plus = []
telemarketers = {}
for numbers in calls:
    outgoing.append(numbers[0])
    incoming_plus.append(numbers[1])
for text in texts:
    incoming_plus.append(text[0])
    incoming_plus.append(text[1])
for number in outgoing:
    if number not in incoming_plus:
        telemarketers[number] = ""
print("These numbers could be telemarketers: ")
for tele in sorted(telemarketers.keys()):
    print(tele)


