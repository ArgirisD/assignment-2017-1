import sys

input_file = sys.argv[1]
#input_file = "example_graph_3.txt"

matches_list = []
#reading the file
with open(input_file,'r') as f:
        for line in f:
            z = line.rstrip()
            parts_of_line = z.split()
            parts_int = [str(x) for x in parts_of_line]
            matches_list.append(parts_int)


days = 0

players = {}
players1 = {}
matches = {}

while (len(matches_list) > 0):
    #creating a list with all the players
    for i in matches_list:
        if i[0] not in players1:
            players1[i[0]] = 0
        elif i[1] not in players1:
            players1[i[1]] = 0
    #players.sort()
    for key in sorted(players1):
        players[key] = 0
    #print(players)
    
    #main_algorithm
    for j in range(0,len(players)+1):
        for key, value in players.items():
            players[key] = 0
        for i in matches_list:
            i.sort()
            if players[i[0]] == 0 and players[i[1]] == 0:
                matches[i[0]+", "+i[1]] = days
                players[i[0]] = 1
                players[i[1]] = 1
                matches_list.remove(i)
        days = days + 1
    
    #sorting the results
    final = {}
    for key, value in sorted(matches.items()):
        final[key] = value
        
    for k in final.keys():
        print("("+k+") " + str(final[k]))