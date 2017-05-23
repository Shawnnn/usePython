#-*-coding:utf-8-*-
#!/usr/bin/env python

'''


'''
import random

raw_lst=['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','J ',"Q ","K "]
temp_lst=[]
for i in raw_lst:
    for type in ['spade','heart','club','diamond']:
        temp_lst.append(i+type)
temp_lst.append('Little Joker')
temp_lst.append('Big Joker')
print temp_lst
random.shuffle(temp_lst)
print "All Cards are: ",str(temp_lst)
hidden_lst=[]
for i in range(1,4):
    hidden=random.choice(temp_lst)
    temp_lst.remove(hidden)
    hidden_lst.append(hidden)
print 'Hidden Cards are: ',str(hidden_lst)
player_A=temp_lst[:17]
player_B=temp_lst[17:34]
player_C=temp_lst[34:]
print 'player_A',str(player_A)
print 'player_B',str(player_B)
print 'player_C',str(player_C)