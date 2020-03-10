import random


'''
读取记录
'''
path = "./game_one_user.txt"

f = open(path)
r_dict = {}
record = f.read()
f.close()
r_list = record.split()
# print(r_list)
r_dict['name'] = r_list[0]
r_dict['result'] = r_list[1:]
# print(r_dict)

#print(f'user {r_dict['name']} has played {r_dict['result'][0]} times, and the fastest is {r_dict['result'][1]} round, and avg {r_dict['result'][2]} round to win! \n')
print('user %s has played %d times, and the fastest is %d round, and avg %.2f round to win! \n'%(r_dict['name'],int(r_dict['result'][0]), int(r_dict['result'][1]), float(r_dict['result'][2])))

#结合记录中的成绩，赋予初始值

quit = 0

#name =input('welcome to the guess number game!!! Plz input your name:\n')
name = r_dict['name']

#game_times = 0 #游戏次数
game_times = int(r_dict['result'][0])

# sum_round = 0 #总共玩了多少轮
sum_round = int(r_dict['result'][1])

times_list = [] 
times_list.append(float(r_dict['result'][2])) #每一次游戏玩了多少轮，放在一个列表中



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
    print(f"\n-----------\nuser:\t{name}\nhas played {game_times} times in this game; \nthe fastest is {min(times_list)} round; \naverage {sum_round/game_times:.2f} times to win\n-----------\n")

    # exit the game or not?
    quit = input("Do you want to quit the game? click 'q', 'e' to exit the game!\n")

print('Game Over!')
f = open(path, "a")
f.write(result)
f.close()
