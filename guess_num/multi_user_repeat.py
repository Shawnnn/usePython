import random

path = './game_many_user.txt'
f = open(path, 'r', encoding = 'utf-8')
records = {} # 建立空字典B
lines = f.readlines() #读取成绩记录，每条成绩是一个列表
f.close()
for line in lines: # line 是小列表A， lines是大列表B
    data = line.split(' ')
    #print('data[0]',data[0],'\n','data[1:]',data[1:],'\n')
    records[data[0]] = data[1:]  # 小列表A中用户名做键， 成绩作为值， 存入字典B
#print(records)

name = input('plz input your name:\t')
times_list = []
if records.get(name):
    game_times = int(records.get(name)[0])
    times_list.append(int(records.get(name)[1]))
    sum_round = int(records.get(name)[2].strip())
    avg_times = sum_round / game_times
    print(f'{name} 已经玩了{game_times}次; 最快是{int(records.get(name)[1])}轮猜出来； 平均是{avg_times:.2f}轮\n')
else:
    game_times = 0
    sum_round = 0
    avg_times = 0
    print(f'{name} 已经玩了 0 次; 最快是 0 轮猜出来； 平均是 0 轮\n')


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

    result = f"{name} " + f"{game_times} " + f"{min(times_list)} " + f"{sum_round}\n"
    print(f"\n-----------\nuser:\t{name}\nhas played {game_times} times in this game; \nthe fastest is {min(times_list)} round; \naverage {sum_round/game_times:.2f} times to win\n-----------\n")

    # exit the game or not?
    quit = input("Do you want to quit the game? click 'q', 'e' to exit the game!\n")

print('Game Over!')

records[name] = [f"{game_times}", f"{min(times_list)}", f"{sum_round}\n"]

print(records)
list_record = []
for r_name in records:
    r_string = f"{r_name} "+ " ".join(records[r_name])
    list_record.append(r_string)

list_join = ""
for l in list_record:
    list_join += l
list_join += "\n"

f = open(path, "w", encoding = 'utf-8')
f.writelines(list_join)
f.close()
