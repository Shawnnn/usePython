#-*-coding:utf-8-*-
#!/usr/bin/env python

'''
generate 200 coupons
each consists of 8 letters(upper or lower case is fine)
'''

import string
import random
# letters=string.letters
# lst=[]
# coupon=[]
# for i in range(1,201):
#     for j in range(1,9):
#         coupon.append(random.choice(letters))
#         coupon_str=''.join(coupon)
#     print coupon_str
#     lst.append(coupon_str)
#     del coupon[:]

coupon_lst=[]
for i in range(1,201):
    letter_lst=list(string.ascii_letters)
    random.shuffle(letter_lst)
    string_lst=''.join(letter_lst)
    coupon=string_lst[:8]
    # print coupon
    coupon_lst.append(coupon)

print('\n'.join('{1}'.format(*k) for k in enumerate(coupon_lst))) # 列表解析式生成的“generator object”

# print(['{1}'.format(*k) for k in enumerate(coupon_lst)])
# print(list('{1}'.format(*k) for k in enumerate(coupon_lst))) # 同上
# print(coupon_lst) #同上