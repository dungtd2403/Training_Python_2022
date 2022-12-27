# Python program to change the
# current working directory


import os

nameCountry = input()

path = 'D:/python/week3/tas_data/' + nameCountry + '.csv'

with open(path) as f:
    for line in f:
        print(line)


