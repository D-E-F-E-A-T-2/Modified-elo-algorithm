#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

def Probability(rating1, rating2): 
  return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 
  

def EloRating(Ra, Rb, K, Sa, Sb, name1, name2):

    # To calculate the Winning Probability of Player B 
    Pb = Probability(Ra, Rb) 
  
    # To calculate the Winning Probability of Player A 
    Pa = Probability(Rb, Ra)

    P1=Sa/(Sa+Sb)
    P2=Sb/(Sa+Sb)

    oRa = Ra
    oRb = Rb
    
    # Case -1 When Player A wins 
    # Updating the Elo Ratings 
    if (Sa>Sb) : 
        Ra = round(Ra + K * P1*(1 - Pa), 2) 
        Rb = round(Rb + K * P2*(0 - Pb), 2)
      
  
    # Case -2 When Player B wins 
    # Updating the Elo Ratings 
    else : 
        Ra = round(Ra + K * P1*(0 - Pa), 2) 
        Rb = round(Rb + K * P2*(1 - Pb), 2)
 

    if Ra<1200:
      league_a = 'Unranked'
    elif 1200<Ra<2400:
      league_a = 'Gold'
    elif 2400<Ra<3500:
      league_a = 'Diamond'
    elif Ra>3500:
      league_a = 'Master'

    if Rb<1200:
      league_b = 'Unranked'
    elif 1200<Rb<2400:
      league_b = 'Gold'
    elif 2400<Rb<3500:
      league_b = 'Diamond'
    elif Rb>3500:
      league_b = 'Master'
    Sa, Sb, Ra, Rb, oRa, oRb = list(map(str, [Sa, Sb, Ra, Rb, oRa, oRb]))
    
    print("Player\tScore\tOld Rating\tNew Rating\tNew League")
    print(name1+"\t"+Sa+"\t"+oRa+"         "+Ra+"         "+league_a)
    print(name2+"\t"+Sb+"\t"+oRb+"         "+Rb+"         "+league_b)
    print("Winner:\t"+name1 if Sa>Sb else "Winner:\t"+name2)

    


array=[] #Data-set storage

for x in range(10000): #Makes a data-set
	array.append(['p'+str(x+1), round(random.uniform(800, 5000), 2)])

for x in range(len(array)): # Giving players their leagues
	if array[x][1]>3500:
		array[x].append('Master')
	elif 2400<array[x][1]<3500:
		array[x].append('Diamond')
	elif 1200<array[x][1]<2400:
		array[x].append('Gold')
	elif 800<array[x][1]<1200:
		array[x].append('unranked')

n = int(input("Number of online players: "))
print()
online = [array[random.randint(0, 9999)][0] for x in range(n)]
print("Online players list:")
for x in online:
  print(x, end='\t')
print()
print()
Master = []
Diamond = []
Gold = []
unranked = []
waiting = []
dict_ = {x[0]:[x[1], x[2]] for x in array}

for x in online:
    if dict_.get(x)[1]=='Master':
        Master.append([x, *dict_.get(x)])
    elif dict_.get(x)[1]=='Gold':
        Gold.append([x, *dict_.get(x)])
    elif dict_.get(x)[1]=='Diamond':
        Diamond.append([x, *dict_.get(x)])
    elif dict_.get(x)[1]=='unranked':
        unranked.append([x, *dict_.get(x)])

leagues = [Master, Diamond, Gold, unranked]

for x in leagues:
    if len(x)==1:
        waiting.append("Waiting: "+str(x[0][0])+"\tLeague: "+str(x[0][2]))
    elif len(x)==0:
        pass
    else:
        if len(x)&1:
            waiting.append("Waiting: "+str(x[len(x)-1][0])+"\tLeague: "+str(x[len(x)-1][2]))
            x.pop(len(x)-1)
        for y in range(0, len(x), 2):
            score_a = (int(str(x[y][0])[1:]))%10
            score_b = 10-score_a
            EloRating(x[y][1], x[y+1][1], 30, score_a, score_b,x[y][0], x[y+1][0])
            print()

print()
for x in waiting:
  print(x)
input("Hit any key to exit.")
