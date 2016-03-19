"""
Is offense or defense a better indicator for overall ranking in the NBA?

Took the average points for and aganist a NBA team as the basis for offensive and defensive rankings.
Compared the overall ranking, determined by their season record, to the offensive and defensive rankings.
The 2014-2015 NBA statistics is provided by http://www.basketball-reference.com/leagues/NBA_2015.html
"""
import csv
import sys


results = []
with open('Overall_rank', newline='') as inputfile: # Gets input from file and parses into a 2D list
    for i in csv.reader(inputfile):
        results.append(i)

team_rank = []
temp = []
for i in results: # Adds overall rank, name, and record
    temp.append(i[0])
    temp.append(i[1])
    temp.append(i[2])
    team_rank.append(temp)
    temp = []

results.clear()
with open('Offense', newline='') as inputfile:
    for i in csv.reader(inputfile):
        results.append(i)

temp_str = ""
for i in results: # Adds Offense ranking and average points per game
    if i[1][len(i[1]) - 1] == '*': # removes askerisks from end of names (if there is one)
        tempstr = (i[1])[:len(i[1]) - 1]
    else:
        tempstr = i[1]
    for j in team_rank:
        if tempstr == j[1]:
            j.append(i[0])
            j.append(i[len(i) - 1])


results.clear()
with open('Defense', newline='') as inputfile:
    for i in csv.reader(inputfile):
        results.append(i)

for i in results: # Adds deffense ranking and average point per game aganist
    if i[1][len(i[1]) - 1] == '*':
        tempstr = (i[1])[:len(i[1]) - 1]
    else:
        tempstr = i[1]
    for j in team_rank:
        if tempstr == j[1]:
            j.append(i[0])
            j.append(i[len(i) - 1])

defense_rank_dif = 0
offense_rank_dif = 0
for i in team_rank: # calculates average differences
    defense_rank_dif += abs(int(i[0]) - int(i[5]))
    offense_rank_dif += abs(int(i[0]) - int(i[3]))
defense_rank_dif /= 30
offense_rank_dif /= 30
print('Average difference between overall ranking and offensive ranking = %s\n'
      'Average difference between overall ranking and defensive ranking = %s\n'
      % (offense_rank_dif, defense_rank_dif))

print('Rank  Name                         Record   Offensive Ranking  Points Per Game  Defensive Ranking  Points Per Game')
for i in team_rank: # prints with spacing
    sys.stdout.write(i[0])
    sys.stdout.write('     ')
    sys.stdout.write(i[1])
    length_counter = len(i[1])
    while length_counter < 30:
        sys.stdout.write(' ')
        length_counter += 1
    print(i[2], '  ', i[3], '                ', i[4], '          ', i[5], '                ', i[6])