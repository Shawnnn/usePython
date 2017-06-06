#-*-coding:utf-8-*-
#!/usr/bin/env python

f=open('wordsList.txt','r')
words=str(f.read())
wordsList=words.split()
print "wordList:"
for word in wordsList:
    print word
print

# for i in f.readlines():
#     print i
test='从前明月光，疑似地上霜。\nShawn hello goodbye\nstudent HKU'
raw_test=raw_input("please input test words: ")
print raw_test
if raw_test!='': #if raw_input only get enter pressed, then return none instead of '\n'
    test=raw_test

testList=test.split()
print testList

print "testList:"
for test in testList:
    print test
print

for index,test in enumerate(testList):
    for word in wordsList:
        if test==word:
            testList[index]="*"
print "result:"
for test in testList:
    print test

