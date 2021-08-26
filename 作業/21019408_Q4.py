# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:34:52 2021

@author: 懿萱
"""

##第一題
import pandas as pd
import numpy as np
import os
from datetime import datetime

os.getcwd()
os.chdir('C:\\Users\\sweewei.law\\Desktop\\實習生\\作業3&4')
  
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
df=pd.read_excel("ArticleInfo.xlsx")
#將keywordlist中的每個關鍵字轉串列  df.at[1,"ArticleTitle"]
key=[0]*len(df.index)
keyword_list,list_season=[],[]
i=0
#關鍵字轉換
def Keyword_trans(index):
    key[index]=df.at[index,'KeyWordList']
    tmp_list= key[index].split("|")
    keyword_list.append(tmp_list)
    df.at[index,"KeyWordList"]=keyword_list[index]   
     
#利用PubDate建構YearSeason，Q1：1-3、Q2：4-6、Q3：7-9、Q4：10-12
#例如PubDate = 2018/5/20，轉換後新增一欄位YearSeason = 2018_Q2
def YearSeason_construct(index):
    date=df.at[index,'PubDate']
    y=date.year
    m=date.month    
    if m>=1 and m<=3:
        season='Q1'
    elif m>=4 and m<=6:
        season='Q2'
    elif m>=7 and m<=9:
        season='Q3'
    else:
        season='Q4'
    yearseason=str(y)+"_"+season
    return yearseason    
#在標題後面加上有<key>標籤的關鍵字們
def articlekey(index):
    article_with_key=[]
    keyword_list[index]='<Key>'+'</Key><Key>'.join(keyword_list[index])+'</Key>'
    article_with_key=df.at[index,"ArticleTitle"]+keyword_list[index]
   
#更新dataframe    
for i in range(len(df.index)):  
    Keyword_trans(i)
    y=YearSeason_construct(i)
    list_season.append(y)
    
df['YearSeason'] = list_season
df['PubDate']  = df['PubDate'].astype(str)
df.to_json("ArticleInfo.json",orient = 'records',lines=True)

# sw 1: function 內有function外變數
# Yearmonth 判斷式可精簡
# articlekey沒有執行

# def Keyword_trans(key):
#     tmp_list= key.split("|")
#     return tmp_list

# def YearSeason_construct(date = df.at[i, 'PubDate']):
#     y=date.year
#     m=date.month    
#     if m<=3: season = 'Q1'
#     elif m<=6: season = 'Q2'
#     elif m<=9: season = 'Q3'
#     else: season ='Q4'
#     yearseason = str(y) + "_" + season
#     return yearseason

# def articlekey(art, key):
#     for k in key:
#         temp = re.findall(k, art, re.IGNORECASE)
#         if len(temp) != 0:
#             matchInfo = re.search(k, art, re.IGNORECASE)
#             place = matchInfo.span()
#             art = art[:place[0]] + "<key>" + art[place[0]:place[1]] + \
#                 "</Key>" + art[place[1]:]
#     return art
    
# df=pd.read_excel("ArticleInfo.xlsx")

# for i in range(len(df.index)):
#     df.at[i, "KeyWordList"] = Keyword_trans(df.at[i, "KeyWordList"])
#     df.at[i, 'YearSeason'] = YearSeason_construct(df.at[i, 'PubDate'])
#     df.at[i,"ArticleTitle"] = articlekey(df.at[i,"ArticleTitle"], df.at[i, "KeyWordList"])
# df['PubDate'] = df['PubDate'].astype(str)
# df.to_json("ArticleInfo1.json",orient = 'records',lines=True)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#第二題
import xml.etree.ElementTree as ET
import nltk
class DataProcess:        
        
    #從檔案中找到標題與摘要標籤，並回傳該文件的標題與摘要    
    def xmlAccess(inFile):        
        tree=ET.parse(inFile)
        root=tree.getroot()
        article=root.find('PubmedArticle').find('MedlineCitation').find('Article')
        article_title=article.find('ArticleTitle').text           
        abstract_text=article.find('Abstract').find('AbstractText').text       
        return article_title,abstract_text
    def Number_of_characters_blankinclude(text):
        
        #計算字元數
        num_char_blank=len(text)
        
        #計算空格        
        count = 0
        for i in text:
            if i == " ":
                count += 1
        #不包含空格的字元數
        num_char_noblank=len(text)-count
        
        #所有字數
        number_char=len(text.split())
        
        #計算句數
        import nltk
        nltk.download('punkt')
        from nltk.tokenize import sent_tokenize        
        number_of_sentences =len(sent_tokenize(text))
        
        return num_char_blank,num_char_noblank,number_char,number_of_sentences
        #篩選出文章的相同字，並計算兩篇文章相同字數
        #步驟：文章分詞->選出相同字->計算相同字數
        #將字串全部變成小寫，並去除標點符號  
    def trans(text):
            return ''.join([c.lower() if c.isalpha() else ' ' for c in text])
        #選出兩文章相同字並計算字數
    def extra_same_elem(list1, list2):
             set1 = set(list1)
             set2 = set(list2)
             iset = set1.intersection(set2)
             return list(iset), len(list(iset))


file_name=['PubmedArticle1.xml','PubmedArticle2.xml','PubmedArticle3.xml','PubmedArticle4.xml']
no=['一','二','三','四']
i=0
t,a=[0]*len(file_name),[0]*len(file_name)
c,text_trans,r1,r2,r3,r4=[],[],[],[],[],[]
path = 'output.txt'
 
#用迴圈每個檔案的標題、摘要、統計字詞等
for i in range(len(file_name)): 
    t[i],a[i]=DataProcess.xmlAccess(file_name[i]) #所有檔案的標題與摘要list
    c.append(t[i]+' '+a[i])
    ra,rb,rc,rd=DataProcess.Number_of_characters_blankinclude(c[i])
    r1.append(ra),r2.append(rb),r3.append(rc),r4.append(rd)
    text_trans.append(DataProcess.trans(c[i]).split())
j=0
k=0
path = 'output.txt'        
with open(path, 'w') as f:
    for j in range(len(file_name)):
        #f.write('第%s篇文章統計資訊如下\n'%(no[j]))
        #f.write("================================\n")
        #f.write('包含空白字元的所有字元數:%d\n'%(r1[j]))
        #f.write('不包含空白字元的所有字元數：%d\n'%(r2[j]))
        #f.write('所有字數：%d\n'%(r3[j]))
        #f.write('所有句數：%d\n'%(r4[j]))        
        #f.write("================================\n\n")
        for k in range(len(file_name)-j-1):
            f.write('第%s篇文章統計資訊如下\n'%(no[k+j+1]))
            f.write("================================\n")
            f.write('包含空白字元的所有字元數:%d\n'%(r1[k+j+1]))
            f.write('不包含空白字元的所有字元數：%d\n'%(r2[k+j+1]))
            f.write('所有字數：%d\n'%(r3[k+j+1]))
            f.write('所有句數：%d\n'%(r4[k+j+1]))        
            f.write("================================\n\n")
            sameword_list,count_sameword= DataProcess.extra_same_elem(text_trans[j], text_trans[k+j+1])
            f.write('第%s篇與第%s篇文章交叉比對資訊如下:\n'%(no[j],no[k+j+1]))
            f.write("================================\n")
            f.write('兩篇文章相同字數:%d\n'%(count_sameword))
            f.write('相同字：%s\n'%sameword_list)
            f.write("================================\n\n")    
    
    

        #f.write('第%s篇文章統計資訊如下\n'%(no[i]))
        #f.write("================================\n")
        
        print('包含空白字元的所有字元數:%d\n'%r1[i])
        print('不包含空白字元的所有字元數：%d\n'%r2[i])
        print('所有字數：%d\n'%r3[i])
        print('所有句數：%d\n'%r4[i])        
        print("================================\n\n")
        text_trans.append(DataProcess.trans(c[i]).split())
        for k in range(len(file_name)-j):            
            sameword_list,count_sameword= DataProcess.extra_same_elem(text_trans[j], text_trans[k+j])
        print('第%s篇與第%s篇文章交叉比對資訊如下:'%(no[j],no[k+j]))
        print("================================")
        print('兩篇文章相同字數:',count_sameword)
        print('相同字：',sameword_list)
        print("================================",end='\n\n')

#比對with open(path, 'w') as f: 
for j in range(len(file_name)):    
    for k in range(len(file_name)-j):                
        sameword_list,count_sameword= DataProcess.extra_same_elem(text_trans[j], text_trans[k+j])
        print('第%s篇與第%s篇文章交叉比對資訊如下:'%(no[j],no[k+j]))
        print("================================")
        print('兩篇文章相同字數:',count_sameword)
        print('相同字：',sameword_list)
        print("================================",end='\n\n')
              
         

         

        lst = extra_same_elem(test, con)
        lst.sort() #对结果排一下序，方便查看
        print(lst)
        len(lst)
       
        
        
       
         
        
      
         tt1= trans(t1) 
         tt2=trans(t2)
         print(article) #測試印出轉換後的字串
         test=tt1.split()
         con=tt2.split()
         #找出相同字
         def extra_same_elem(list1, list2):
             set1 = set(list1)
             set2 = set(list2)
             iset = set1.intersection(set2)
             return list(iset)
         
        lst = extra_same_elem(test, con)
        lst.sort() #对结果排一下序，方便查看
        print(lst)
        len(lst)



    t,a=xmlAccess('PubmedArticle1.xml') #所有檔案的標題與摘要list
    print(t,a)
content=t+a       
print(len(number_of_sentences))
        
    
file_name=['PubmedArticle1.xml','PubmedArticle2.xml','PubmedArticle3.xml','PubmedArticle4.xml']
i=0
#用迴圈每個檔案的標題、摘要、統計字詞等
for i in range(len(file_name)): 
    
    t,a=xmlAccess(file_name[i]) #所有檔案的標題與摘要list
    content=t+' '+a
    print(t,a)
    
    
# sw 2: function 縮排問題
# function 內有 import，一般寫在外面
    
# from bs4 import BeautifulSoup
# import os

# os.getcwd()
# os.chdir("C:\\Users\\sweewei.law\\Desktop\\Python Programming")

# class wordProcess(object):
#     def __init__(self,data1,data2):
#         self.data1 = data1
#         self.data2 = data2
        
#     def deleteString(self,string,deleteWord):
#         string = str(string)
#         outputString = string.strip(deleteWord)  
#         return outputString
    
#     def statisticResult(self,string, word):
#         a = "包含空白字元的所有字元數：" + str(len(string))
#         b = "不包含空白字元的所有字元數：" + str(len(string.replace(' ', '')))
#         c = "所有字數：" + str(len(string.split(" ")))     
#         d = "所有句數：" + str(string.count("."))
#         outputString = "第" + word + "篇文章統計資訊如下\n" + \
#                        "================================\n" +\
#                        a + "\n" + b + "\n" + c + "\n" + d + "\n" +\
#                        "================================\n\n"
#         return outputString

#     def sameInfo(self,string1,string2):
#         set1 = set(string1.lower().split(" "))
#         set2 = set(string2.lower().split(" "))
#         same = set1.intersection(set2)
#         outputString = "兩篇文章交叉比對資訊如下\n" + \
#                        "================================\n" +\
#                        "兩篇文章相同字數：" + str(len(same)) + "\n" +\
#                        "相同字：" + str(same) + "\n" +\
#                        "================================\n\n"
#         return outputString
                            

# with open("PubmedArticle1.xml") as f:
#     pubmedArticle1 = BeautifulSoup(f, 'xml')
# with open("PubmedArticle2.xml") as f:
#     pubmedArticle2 = BeautifulSoup(f, 'xml')

# s1 = wordProcess(pubmedArticle1, pubmedArticle2)
# pubmedArticle1.ArticleTitle.text
# articleTitle1 = s1.deleteString( pubmedArticle1.ArticleTitle, "<ArticleTitle></ArticleTitle>")
# articleTitle2 = s1.deleteString( pubmedArticle2.ArticleTitle, "<ArticleTitle></ArticleTitle>")
# abstract1 = s1.deleteString( pubmedArticle1.AbstractText, "<AbstractText></AbstractText>")
# abstract2 = s1.deleteString( pubmedArticle2.AbstractText, "<AbstractText></AbstractText>")

# Info1 = s1.statisticResult(abstract1, "一")
# print(Info1)

# Info2 = s1.statisticResult(abstract2, "二")
# print(Info2)

# Info3 = s1.sameInfo(abstract1, abstract2)
# print(Info3)

# Info = Info1 + Info2 + Info3
# fp = open("ArticleStatistic.txt", "w")
# fp.write(Info)
# fp.close() 