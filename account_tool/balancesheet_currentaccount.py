#-*-coding:utf-8-*-
#!/usr/bin/env python

import datetime

def query1():
    print("最近十笔交易")
    print("交易对象\t收入\t支出\t应收账款\t应付账款\t交易时间")
    with open("currentaccount.txt") as ca:
        lines = ca.readlines()
        for index,line in enumerate(lines):
            if index <= 10:
                lst = line.split()
                print("{0}\t\t{1}万\t{2}万\t{3}万\t\t{4}万\t\t{5}".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]))
    print("done!")

def query2():
    company = raw_input("请输入公司名（只需要输入名字，不需要加公司）：")
    with open("currentaccount.txt") as ca:
        lines = ca.readlines()
        string = " ".join(lines)
        count = string.count(company)
        print("\n与%s公司共有%d笔交易"%( company , count ))
        if count > 0:
            for line in lines:
                if company in line:
                    line = line.split()
                    print("交易时间：{}\n收入：{}万\n支出：{}万\n应收账款：{}万\n应出账款:{}万\n".format(line[5],line[1],line[2],line[3],line[4]))
    print('done!')

def query3():
    with open("balancesheet.txt") as bs:
        line =  bs.readline()
        line = line.split()
        print("\n最新资产：{}万\n最新负债：{}万\n最新净资产：{}万\n最后更新时间：{}".format(line[0],line[1],line[2],line[3]))
    print("done!")

def tally():
    print("记账模式")
    transObject = raw_input("交易对象：")
    income =  raw_input("收入/万：")
    outcome = raw_input("支出/万：")
    recievables = raw_input("应收款项/万：")
    payment = raw_input("应出款项/万：")
    date = datetime.date.today() # this is an object
    with open("currentaccount.txt","a") as ca:
        ca.write(transObject+" ")
        ca.write(income + " ")
        ca.write(outcome + " ")
        ca.write(recievables + " ")
        ca.write(payment + " ")
        ca.write(str(date) + "\n") # object converted to string
    with open("balancesheet.txt","w+") as bs:
        line = bs.readline()
        if not line: # if line is empty
            data = [0,0,0,0]
            data[0] += float(income) - float(outcome)
            data[1] += float(payment) - float(recievables)
            data[2] += data[0] - data[1]
        else:
            data = line.split()
            data = map(float , data)
            data[0] += float(income) - float(outcome)
            data[1] += float(payment) - float(recievables)
            data[2] += data[0] - data[1]
        data[3] = date
        data = map(str, data)
        bs.seek(0,3) # whenever read and write in the same io operate, seek function should be used in order to adjust file pointer
        bs.write(" ".join(data))
        print("交易已记录\n当前资产状况:\n最新资产:%s万\n最新负债:%s万\n最新净资产:%s万\n"%(data[0],data[1],data[2]))

if __name__ == "__main__":
    while True:
        print("\n1.查询 2.记账 ")
        print("按其他，退出")
        choice = raw_input("请选择服务：")

        if choice == "1":
            print("\n查账模式：")
            choice = raw_input("\n查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况\n请选择服务:")
            if choice == "1":
                query1()
            elif choice == "2":
                query2()
            elif choice == "3":
                query3()
            else:
                print("没有所指定的查账模式，退出！")
                break
        elif choice == "2":
            tally()
        else:
            break
print("结束！")

