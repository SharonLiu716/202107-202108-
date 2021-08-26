# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 16:57:21 2021

@author: 懿萱
"""
from itertools import combinations
from operator import itemgetter
    
class Test:
    def __init__(self,list1):
        self.list1=list1        
        
    def detail_of_commodity(self,list2):
        return dict(zip(self.list1, list2))
        
    def show_combine(self,tt1,tt2,number):
       all_result = list(combinations(self.list1,number))
       for i in range(len(all_result)): 
           tmp=all_result[i] ##第i個組合的結果    
           no_result_i=[0]*len(tmp)
           price_result_i=[0]*len(tmp)
           
           for j in range(len(tmp)): #抓第i個結果的編號與價錢
               no_result_i[j]=tt1[tmp[j]]
               price_result_i[j]=tt2[tmp[j]]        
           total=sum( price_result_i)    
           dict_result_i=dict(zip(list(tmp),no_result_i))
           dict_result_i=dict(sorted(dict_result_i.items(), key=itemgetter(1), reverse=False)) 
           print(dict_result_i,'=> $',total)
          
        
name_of_commodity=['球','筆','紙','卡','刀']
price_of_commodity=[20,10,15,30,25]
no_of_commodity=[4,2,3,5,1]
c=Test(name_of_commodity)
d1=c.detail_of_commodity(price_of_commodity)
d2=c.detail_of_commodity(no_of_commodity)
print('物品對價位 ',d1)
print('物品對編號 ',d2)

for k in range(len(name_of_commodity)):
    print("5取",k,"所有組合數如下")     
    c.show_combine(d2,d1,k)
#sw 1: OK~
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
##2
#考拉茲臆測函數

import statistics 
class Part1:
    detail_1=['數列長度：','數列平均值：','數列中位數：','數列標準差：']
    
    def collatz(number):
        serie_of_collatz=[number]
        while number != 1:
            if number % 2 == 0:              # 偶數
                number /= 2
                
            elif number % 2 == 1:            # 奇數
                number = number * 3 + 1
            serie_of_collatz.append(number)
        return serie_of_collatz
    
    
    def stat(serie):
        len_s=len(serie)
        mean_of_s=statistics.mean(serie)
        median_of_s=statistics.median(serie)
        std_of_s=statistics.stdev(serie)
        detail_2=[len_s,mean_of_s,median_of_s,std_of_s]
        for i in range(len(Part1.detail_1)):
            print(Part1.detail_1[i],detail_2[i])

class Part2(Part1):
    detail_3=['數列奇偶比：','數列奇偶差：']
    def odd_even(series):
        i=0
        list_odd=[]
        list_even=[]
        while i<len(s):
            if s[i]%2==0:
                list_even.append(s[i])
            else:
                list_odd.append(s[i])
            i=i+1
        ratio=len(list_odd)/len(list_even)
        diff=sum(list_odd)-sum(list_even)
        detail_4=[ratio,diff]
        for j in range(len(Part2.detail_3)):
            print(Part2.detail_3[j],detail_4[j])
    
s=Part1.collatz(5)
print("考拉茲數列：",*s)
Part2.stat(s)
Part2.odd_even(s)

# sw 2：
# class Part1():
    
#     def __init__(self, number):
#         self.number = number
#         self.serie = self.collatz()
        
#     def collatz(self):
#         num = self.number
#         serie_of_collatz=[num]
#         while num != 1:
#             if num % 2 == 0:              # 偶數
#                num /= 2
                
#             elif num % 2 == 1:            # 奇數
#                 num = num * 3 + 1
#             serie_of_collatz.append(num)
#         return serie_of_collatz
    
#     def stat(self):
#         detail_1=['數列長度：','數列平均值：','數列中位數：','數列標準差：']
    
#         len_s=len(self.serie)
#         mean_of_s=statistics.mean(self.serie)
#         median_of_s=statistics.median(self.serie)
#         std_of_s=statistics.stdev(self.serie)
#         detail_2=[len_s,mean_of_s,median_of_s,std_of_s]
#         for i in range(len(detail_1)):
#             print(detail_1[i],detail_2[i])

# class Part2(Part1):
    
#     def __init__(self, number):
#         Part1.__init__(self, number)
        
#     def odd_even(series):
#         detail_3=['數列奇偶比：','數列奇偶差：']
#         i=0
#         list_odd=[]
#         list_even=[]
#         while i<len(s):
#             if s[i]%2==0:
#                 list_even.append(s[i])
#             else:
#                 list_odd.append(s[i])
#             i=i+1
#         ratio=len(list_odd)/len(list_even)
#         diff=sum(list_odd)-sum(list_even)
#         detail_4=[ratio,diff]
#         for j in range(len(detail_3)):
#             print(detail_3[j],detail_4[j])
            
# a = Part2(5)
# print("考拉茲數列：",*s)
# a.collatz()
# a.stat()
# a.odd_even()
