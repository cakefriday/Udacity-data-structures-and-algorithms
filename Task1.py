"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def find_different(list):
    different_numbers = []
    for numbers in list:
        if numbers[0] not in different_numbers:
            different_numbers.append(numbers[0])
        if numbers[1] not in different_numbers:
            different_numbers.append(numbers[1])
    return different_numbers

all_different = len(find_different(calls)) + len(find_different(texts))
print("There are {} different telephone numbers in the records.".format(all_different))