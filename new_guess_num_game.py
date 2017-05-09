#!/usr/bin/env python

import random
round_total=3
round_cnt=0
count=0
min_val=1
max_val=10
max_guess=3
right_cnt=0
def print_guessed_num(x):
    print 'The number is %d'%x
while round_cnt<round_total:
    round_cnt+=1
    count=0
    print 'round %d'%round_cnt
    guessed_number=random.randint(1,10)
    print 'initializing a guess number...'
    while count<max_guess:
        count+=1
        print('round {0}, count {1}'.format(round_cnt,count))
        guess=input('guess a number :')
        if guess<guessed_number:
            print 'guess is too smaller'
            if count==max_guess:
                print 'This round ends!'
                print_guessed_num(guessed_number)
            else:
                print 'Guess again!'
        elif guess>guessed_number:
            print "guess is too bigger"
            if count==max_guess:
                print_guessed_num(guessed_number)
                print 'This round ends!'
            else:
                print 'Guess again!'
        else:
            print 'You are right!'
            right_cnt+=count
            if round_cnt<round_total:
                print 'Next round!'
            break

print 'Game over! You need to guess %.2f times for bingo in average each round'%(right_cnt/3.0)