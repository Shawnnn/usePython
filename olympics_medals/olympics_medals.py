#!/usr/bin/env python
#-*-coding:utf-8-*-

class Medals(object):
    def __init__(self):
        self.countries = ["China", "America", "Russia"]
        self.gold = [10,8,6]
        self.silver = [1,2,15]
        self.bronze = [11,13,15]
        self.info_dict = {}
        for i in range(0, len(self.countries)):
            self.info_dict[self.countries[i]] = [self.gold[i], self.silver[i], self.bronze[i]]
        for c in self.countries:
            print("Initiating medals info for {}".format(c))
        print

    def add(self, country, gold = 0, silver = 0, bronze = 0):
        self.countries.append(country)
        self.gold.append(gold)
        self.silver.append(silver)
        self.bronze.append(bronze)
        self.info_dict[country] = [gold, silver, bronze]
        print "\n{} adds {} gold, {} silver, {} bronze".format(country, gold, silver, bronze)

    def print_info(self, msg, sorted_info):
        print "\n" + msg
        for i in sorted_info:
            print("{}:\tgold {};\tsilver {};\tbronze {}".format(i[0], i[1][0], i[1][1], i[1][2]))

    def gold_info(self):
        gold_sorted = sorted(self.info_dict.items(), key=lambda x:x[1], reverse= True)
        # print gold_sorted
        msg = "Gold medals ranking board:"
        self.print_info(msg, gold_sorted)

    def total_info(self):
        total_sorted = sorted(self.info_dict.items(), key=lambda x: sum(x[1]), reverse=True)
        # print total_sorted
        msg = "Total medals ranking board:"
        self.print_info(msg, total_sorted)


if __name__ == "__main__":
    medals = Medals()
    medals.add("Japan",1,1,1)
    medals.gold_info()
    medals.total_info()