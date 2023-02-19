#!/usr/bin/python3
text = input('Enter  a text : ')
for i in text:
    if i.isnumeric():
        print('There is integer number in your text.')
        break
else:
    print('No number in your text!')