# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:33:03 2021

@author: yihsuan.liu
"""

import numpy as np
import random

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
##1 樂透
lottery_number =sorted(random.sample(range(1, 49), 6)) 
lottery_number_special = random.randint(1, 49)
print('大樂透開獎：',*lottery_number, lottery_number_special)

num=list()
i=len(num)
while i<6:
    u=eval(input('請輸入大樂透號碼；'))
    if u>49 or u<1:
        print('請輸入介於1到49的整數')                
    elif u in num:
        print('號碼重複輸入')        
    else:
        num.append(u)
    i=len(num)
 
s1=set(lottery_number)
s2=set(num)
#n1：前六個號碼，n2：特別號
n1=len(list(s1&s2))
n2=lottery_number_special in s2
if n1==6:
    print('恭喜中大樂透頭獎^^')
elif n1==5 and n2==True:
    print('恭喜中大樂透二獎^^')
elif n1==5:
    print('恭喜中大樂透三獎^^')
elif n1==4 and n2==True:
    print('恭喜中大樂透四獎^^')
elif n1==4:
    print('恭喜中大樂透五獎^^')
elif n1==3 and n2==True:
    print('恭喜中大樂透六獎^^')
elif n1==2 and n2==True:
    print('恭喜中大樂透七獎^^')
elif n1==3:
    print('恭喜中大樂透普獎^^')
else:
    print('銘謝惠顧><')
# sw 1: n2 == True --> n2
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
##2 AB遊戲
##A：數字正確，位置正確；B：數字正確，位置不正確
def inputError(guess):
    if len(guess)==4 :
        if guess.isdigit()==True:
            if len(set(guess))==len(guess):                
                if set(guess).isdisjoint(set('0')):
                    check=True
                else:
                    check=False
                    print('猜測數字由1到9組成!!')
            else:
                check=False                
                print('猜測數字不可包含重複數字!!')
        else:            
            check=False
            print('猜測數字不可包含其他字元!!')
    else:        
        check=False
        print('猜測數字長度必須為4位數!!')
    return check
   
def result(guess_list):
    A=0
    B=0
    i=0
    j=0
    for i in range(4):
        if guess_list[i]==true_answer[i]:
            A+=1
        else:
            for j in range(4):
                if guess_list[i]==true_answer[j]:
                    B+=1
    return A,B

true_answer=random.sample(range(1, 9), 4)
print('正確答案：',*true_answer,sep='')
flag=True
while flag:
    guess=input('請輸入猜測數字：')
    error_check=inputError(guess)
    if error_check==True:
        guess_list=list(map(int,guess))
        r=result(guess_list)
        print('猜測狀態：%dA%dB'%(r[0],r[1]))        
        if r[0]==4:
            flag=False
            print('恭喜你猜對了!') 
    elif error_check==False:
        flag=True
    else:
        flag=False
        print('恭喜你猜對了!')
        
# sw 2: 
# def inputError建議不要太多層, 會混亂 
# def result裡的 true_answer比main code早, 建議不要這麼帶，可能會出現error
# result 裡 guess_list 位子猜錯了，就可以直接找set
# if error_check本身為true的話，就不用再 ==True
# while flag: flag 有兩種可能，if else就好，else時flag沒有改變，仍然是True,依然可以跑while loop
 
# def inputError(guess):
#     check = False
#     if guess.isalnum() == False: 
#         print("猜測數字不包含其他字元!!")
#     elif len(guess) > 4 or len(guess) < 4:
#         print("猜測數字長度必須為4位數!!")
#     elif "0" in guess:
#         print("猜測數字由1到9所組成!!")
#     elif len(set(guess))!=4:
#         print("猜測數字不可包含重複數字!!")
#     else:
#         check = True
#     return check

# def result(guess_list, true_answer):
#     A=0; B=0; i=0
#     for i in range(4):
#         if guess_list[i]==true_answer[i]:
#             A += 1
#         elif guess_list[i] in true_answer:
#             B += 1
#     return A,B

# true_answer=random.sample(range(1, 9), 4)
# print('正確答案：',*true_answer,sep='')
# flag=True
# while flag:
#     guess=input('請輸入猜測數字：')
#     error_check=inputError(guess)
#     if error_check:
#         guess_list=list(map(int,guess))
#         r=result(guess_list, true_answer)
#         print('猜測狀態：%dA%dB'%(r[0],r[1]))        
#         if r[0]==4:
#             flag=False
#             print('恭喜你猜對了!') 
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

        
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
##3 利用餘弦相似度公式計算任兩項量的相似度(未完成)
v1=np.array(eval(input('向量1：')))
v2=np.array(eval(input('向量2：')))
dot=sum(v1*v2)
norm=(sum(v1*v1))**0.5*(sum(v2*v2))**0.5
ans=dot/norm
print('向量1與向量2的相似度為{:.3f}'.format(ans))
# sw 3: OK