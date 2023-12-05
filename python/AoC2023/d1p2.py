import re
import sys

data = open(sys.argv[1])
val = 0

lookup_table = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
num_strings = lookup_table.keys()
rev_num_strings = [i[::-1] for i in num_strings]

for i in data:
    num1 = re.search(r'[0-9]' + '|' + '|'.join(num_strings),i).group()
    for k,v in lookup_table.items():
        if num1 == k:
            num1 = num1.replace(k,v)
        else:
            pass

    num2 = re.search(r'[0-9]' + '|' + '|'.join(rev_num_strings),i[::-1]).group()
    num2 = num2[::-1]
    for k,v in lookup_table.items():
        if num2 == k:
            num2 = num2.replace(k,v)
        else:
            pass

    num_cat = str(num1) + str(num2)
    num_cat = int(num_cat)
    val = val + num_cat
print(val)