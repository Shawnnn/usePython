#-*-coding:utf-8-*-
#!/usr/bin/env python

'''
input a key word
in a specific file path, list:
    1, all the files whose file name contains the key word
    2, all the files whose file content contains the key word

'''



'''
reference to answer code: http://git.oschina.net/crossin/crossincode/blob/master/findfile/findfile.py
'''
import os

def keywordMatch(keyword, path = "."):
    keywordList = []
    for dirpath, dirnames, filenames in os.walk(path):
        print "searching in %s ..."%(dirpath)
        for filename in filenames:
            full_name = dirpath + '/' + filename
            if keyword in filename:
                keywordList.append(full_name)
            with open(dirpath+'\\'+filename) as f:
                line = f.readline()
                if keyword in line:
                    keywordList.append(dirpath+'\\'+filename+" : "+line)
    return keywordList

if __name__ == "__main__":
    keyword = raw_input("search key word:\t")
    path = raw_input('in file path:\t')
    if not path.strip():
        path = '.'
    results = keywordMatch(keyword, path)
    print "\n printing result..............\n"
    print(results)
'''
my own version
6/15/2017
description:
1,os.walk() function reads tree directory, returning three-element tuple
issue:
1,keyword cannot be chinese words
2,cannot open user-defined file path
'''
# import os
# def keywordMatch( keyWord):
#     # with open(r'C:\Users\Shawn Yan\Desktop\hku-learning\Interesting\PDF') as f:
#     filenameList = []
#     for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#         for filename in filenames:
#             if keyWord in filename:
#                 filenameList.append(filename)
#             with open(os.path.join(dirpath,filename)) as f:
#                 line = f.readline()
#                 if keyWord in line:
#                     filenameList.append(filename)
#     return filenameList
#
# if __name__ == "__main__":
#     while True:
#         keyWord = raw_input("please input the key word or Enter to exit!\n")
#         if not keyWord:
#             break
#         filenameList = keywordMatch(keyWord)
#         if not filenameList:
#             print("nothing match your key word: %s"%(keyWord))
#         else:
#             print(filenameList)

'''
my own version
6/15/2017
issue:
1,keyword cannot be chinese words
2,cannot open user-defined file path
3, cannot handle the directory in the current work directory
4, can ONLY handle the files in the cwd, while subdirectories are not allowed
'''
# import os
# def keywordMatch( keyWord):
#     filenameList = []
#     for filename in os.listdir(os.getcwd()+"\\test"):
#         if keyWord in filename:
#             filenameList.append(filename)
#         with open(filename) as f:
#             line = f.readline()
#             if keyWord in line:
#                 filenameList.append(filename)
#     return filenameList
#
# if __name__ == "__main__":
#     while True:
#         keyWord = raw_input("please input the key word or Enter to exit!\n")
#         if not keyWord:
#             break
#         filenameList = keywordMatch(keyWord)
#         if not filenameList:
#             print("nothing match your key word: %s"%(keyWord))
#         else:
#             print(filenameList)