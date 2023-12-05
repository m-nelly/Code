import re 
import sys

data = open(sys.argv[1])
final = []

for i in data:
    split = re.split('[:;]',i)
    game_id = re.search(r'\d+',split[0]).group()
    games = [re.split(',',i) for i in split[1:]]

    list_red=[]
    list_green=[]
    list_blue=[]
    
    for i in games:
        color = [re.search(r'red|blue|green',e).group() for e in i]
        number = [re.search(r'\d+',e).group() for e in i]
        red,blue,green = 0,0,0

        for c, n in zip(color, number):
            if c == 'red':
                red+=int(n)
            elif c == 'green':
                green+=int(n)
            else:
                blue+=int(n)
        list_red.append(red)
        list_green.append(green)
        list_blue.append(blue)
    min_red = max(list_red)
    min_green = max(list_green)
    min_blue = max(list_blue)

    power = min_red*min_green*min_blue
    final.append(power)

print(sum(final))
    
    