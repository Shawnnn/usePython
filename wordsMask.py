#-*-coding:utf-8-*-
#!/usr/bin/env python

'''
6/15/2017 shawn
rewrite reference code 
'''
def load_blocked():
    global words
    with open("words.txt") as f:
        words=f.readlines()
        if not words:
            print "empty file!"
            return -1
        words=[w.strip() for w in words if w]
        print words

def text_blocked(text, charset="utf-8", symbol="*"):
    for w in words:
        text=text.replace(w, symbol*len(w.decode(charset)))#  attention: return a text
    return text

if __name__=='__main__':
    load_blocked()
    while True:
        text=raw_input("please input text to be blocked, clicking enter directly to exit\n")
        if not text:
            break
        print text_blocked(text)
        
'''
my own incomplete version
'''
# f=open('wordsList.txt','r')
# words=str(f.read())
# wordsList=words.split()
# print "wordList:"
# for word in wordsList:
#     print word
# print

# # for i in f.readlines():
# #     print i
# test='从前明月光，疑似地上霜。\nShawn hello goodbye\nstudent HKU'
# raw_test=raw_input("please input test words: ")
# print raw_test
# if raw_test!='': #if raw_input only get enter pressed, then return none instead of '\n'
#     test=raw_test

# testList=test.split()
# print testList

# print "testList:"
# for test in testList:
#     print test
# print

# for index,test in enumerate(testList):
#     for word in wordsList:
#         if test==word:
#             testList[index]="*"
# print "result:"
# for test in testList:
#     print test

