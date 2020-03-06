import random

A = random.randrange(1,101,1)

# while True:
#     B = int(input("please input a integer between 1 and 100..."))
#     if A > B:
#         print("猜小了，再试试看！")
#     elif A<B:
#         print("猜大了，再试试看！")
#     else:
#         print("猜对了！"+f"数字就是{B}")
#         break

bingo = False
count = 0
while bingo == False:
    B= int( input("please input an integer between 1 and 100..\n"))
    count += 1
    if A > B:
        print("too small, try again!")
    elif A < B:
        print("too big, try again!")
    else:
        print("you are right! Congrat!")
        bingo = True
print(f"You have tried {count} times!")
