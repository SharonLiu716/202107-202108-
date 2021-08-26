# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:44:01 2021

@author: yihsuan.liu
"""

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
##1 猜數字
import numpy as np
import random

a=random.randint(1, 99)
g=int(input('請猜一個介於1到99的整數'))
while a!=g:
    if a<g:
        print('你猜的數字大於正確答案')
        g=int(input('請猜一個介於1到99的整數：'))
    elif a>g:
        print('你猜的數字小於正確答案')
        g=int(input('請猜一個介於1到99的整數'))
        
print('恭喜你，答對囉^^')

# sw 1: 
# g 可以寫一次就好，如寫在if elif 外
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
##2 使用迴圈輸出高度為 N 的直角三角形
h=eval(input('請輸入三角形的高度：'))
print(h)
for i in range(h):
    for j in range(h-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    print('\n',end='')  

# sw 2： 
# while True:
#     N = int(input("請輸入三角形高度："))
#     for i in range(1,N+1):
#         print(' '*(N-i)+"*"*i)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#3 判斷是否為三角形，若是三角形計算其面積，否則輸出非三角形(未完成)
#三角形任二邊長和大於第三邊 三角形任二邊長差小於第三邊
aa=eval(input('請輸入三角形的第一個邊長：'))
bb=eval(input('請輸入三角形的第二個邊長：'))
cc=eval(input('請輸入三角形的第三個邊長：'))
sum_of_side_length=[aa+bb,aa+cc,bb+cc]
lst=[aa-bb,aa-cc,bb-cc]
diff_of_side_length=[abs(x) for x in lst]
side_length=[cc,bb,aa]
r1=list()
r2=list()

# for l in range(3):
#     r1.append(sum_of_side_length[i]>side_length[i])
#     r2.append(diff_of_side_length[i]<side_length[i])
    
for i in range(3):
    r1.append(sum_of_side_length[i]>side_length[i])
    r2.append(diff_of_side_length[i]<side_length[i])
if r1==r2:
    ss = (aa + bb + cc) / 2
    area = (ss*(ss-aa)*(ss-bb)*(ss-cc)) ** 0.5
    print('三角形面積為：' ,area)
else:
    print('此三邊長不可構成三角形')

# sw 3:
# for 迴圈 index錯了
# while True:
#     first = float(input("請輸入三角形的第一個邊長："))
#     second = float(input("請輸入三角形的第二個邊長："))
#     third = float(input("請輸入三角形的第三個邊長："))
#     if (first+second>third and first+third>second and second+third>first)==0:
#         print("此三邊長不可構成三角形")
#     else:
#         periMeter = (first + second + third)*0.5
#         area = (periMeter*(periMeter-first)*(periMeter-second)*(periMeter-third))**0.5
#         print("三角形面積為：",area)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#4 輸出所有 1 到 N 的整數，但數字不可包含有 3 及 3 的倍數
num=eval(input('請輸入一個整數：'))
for t in range(num+1):
    u=t%3
    if u!=0:
        print(t,end=' ')
        
# sw 4: 輸入14 --> 輸出有13
# num=eval(input('請輸入一個整數：'))
# for t in range(num+1):
#     u = t%3
#     if (u!=0) and ('3' not in str(t)):
#         print(t,end=' ')
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#5 隨機亂數產生一物品單價 N，使得 1≦N≦100。使用者可投幣的幣值為 1 元、 5 元、10 元及 50 元，請模擬販賣機的投幣行為
p=random.randint(1, 100)
print('物品金額:',p)
v=[1,5,10,50]

while p>0:
    m=eval(input('請投遞錢幣：'))
    if m in v:
        p=p-m
        print('剩餘差額：',p)
    else:
        print('幣值錯誤，請重新投幣!!')
   
        
