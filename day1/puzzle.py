from aocd.models import Puzzle
from aocd import get_data
import pathlib
import sys

data = get_data(year=2022, day=1)


data = data.splitlines()

max1 = 0
max2 = 0
max3 = 0
count = 0
for i in data:
    if i == '':
        count = 0
    else: 
        num = int(i)
        count += num

    if count > max1:
        max3 = max2
        max2 = max1
        max1 = count
    elif count > max2:
        max3 = max2
        max2 = count
    elif count > max3:
        max3 = count
    

print(max1)
print(max2+max1+max3)

