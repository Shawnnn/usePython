import random

# while True:
#     B = int(input("please input a integer between 1 and 100..."))
#     if A > B:
#         print("猜小了，再试试看！")
#     elif A<B:
#         print("猜大了，再试试看！")
#     else:
#         print("猜对了！"+f"数字就是{B}")
#         break
quit = 0
while quit not in ['q','e']: 
    bingo = False
    times = 0

    print('welcome to the guess number game!!!')
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
    print(f"You have tried {times} times!")
    quit = input("Do you want to quit the game? click 'q', 'e' to exit the game!\n")
print('Game Over!')
