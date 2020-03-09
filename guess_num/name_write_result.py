import random

quit = 0
game_times = 0
sum_round = 0
times_list = []

path = "./game_one_user.txt"

name =input('welcome to the guess number game!!! Plz input your name:\n')
print(f"Nice to meet you {name}, let's get started!")

while quit not in ['q','e']: 

    bingo = False
    times = 0

    A = random.randrange(1,101,1) # generate a integer number between [1,100]

    while bingo == False:
        B= int( input("please input an integer between 1 and 100..\n"))
        times += 1
        if A > B:
            print("too small, try again!")
        elif A < B:
            print("too big, try again!")
        else:
            print("you are right! Congrat!")
            bingo = True
    print(f"Bingo, you have tried {times} times in this round!")

    #count how many round in total
    sum_round += times

    # a list of times of each games in order to get the minimum later
    times_list.append(times)

    # count how mnay times of game you have played
    game_times += 1

    #result = f"user:\t{name}\nhas played {game_times} times in this game; \nthe fastest is {min(times_list)} round; \naverage {sum_round/game_times:.2f} times to win\n-----------\n"
    result = f"{name} " + f"{game_times} " + f"{min(times_list)} " + f"{sum_round/game_times:.2f}\n"
    print(f"user:\t{name}\nhas played {game_times} times in this game; \nthe fastest is {min(times_list)} round; \naverage {sum_round/game_times:.2f} times to win\n-----------\n")

    # exit the game or not?
    quit = input("Do you want to quit the game? click 'q', 'e' to exit the game!\n")

print('Game Over!')
f = open(path, "a")
f.write(result)
f.close()
