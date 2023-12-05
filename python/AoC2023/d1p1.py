import re
import sys

data = open(sys.argv[1])
val = 0

for i in data:
    num1 = re.search(r'[0-9]',i).group()
    num2 = re.search(r'[0-9]',i[::-1]).group()

    num_cat = str(num1) + str(num2)
    num_cat = int(num_cat)
    val = val + num_cat
print(val)