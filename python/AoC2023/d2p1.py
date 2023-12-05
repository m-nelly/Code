import re 
import sys

data = open(sys.argv[1])
possible_games = [0]

for i in data:
    split = re.split('[:;]',i)
    game_id = re.search(r'\d+',split[0]).group()
    
    games = [re.split(',',i) for i in split[1:]]
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
        
        possible = True
        
        if red > 12:
            possible = False
        elif green > 13:
            possible = False
        elif blue > 14:
            possible = False
        else:
            pass
        
        if possible == False:
            break
        
    print(game_id, possible)
        
    if possible == True:
        possible_games.append(int(game_id))
    else: 
        pass

print(sum(possible_games))


    
    