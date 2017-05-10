#-*-coding:utf8-*-
#!/usr/bin/env python

def print_rect(length=5,width=5,sign='*'):
    for w in range(1,width+1):
        for l in range(1,length+1):
            print sign,
            if l== length:
                print '' # print 空字符，然后换行； 若是print "\n" 则是print 换行，再换行

print_rect(sign='!')
print_rect(3,3)
print_rect(4,5,'a')
print_rect(length=3,width=7,sign='~')