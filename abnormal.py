# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 14:10:37 2021

@author: yihsuan.liu
"""

import os
os.environ["KMP_DUPLICATE_LIB_OK"]  =  "TRUE"
import glob2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

path='C:\\Users\\yihsuan.liu\\Documents\\RQ物料資料清理\\'
df=pd.read_excel(path+'map data V1\\202007.xlsx')
Abnormal=pd.read_excel(path+'repair-parts\\Abnormal.xlsx')
Part=pd.read_excel(path+'repair-parts\\Mapping Tables.xlsx',sheet_name='Part Type')
part_type=Part.groupby('維修效益物料類別')
parts=[]
for part in list(set(Part['維修效益物料類別'])):
    tmp=','.join(Part.groupby('維修效益物料類別').get_group(part)['PART_TYPE'].unique().tolist())
    parts.append(tmp)

df = pd.concat([pd.DataFrame(list(set(Part['維修效益物料類別'])),columns=['維修效益物料類別']),pd.DataFrame(parts,columns=['PART_TYPE'])],axis=1)

df.rename(columns={ df.columns[0]: '維修效益物料類別',df.columns[1]: 'PART_TYPE' }, inplace = True)
Abnormal=Abnormal.merge(df, on='維修效益物料類別')
Abnormal.to_excel('Abnormal.xlsx',index=False)




class Split():
    def __init__(self, DF, list_of_RC,merge_columns,action = "mainRC"):
        # data_version: original: monthly raw data from RQ, updated: 經過欄位縮短&變換
        self.DF = DF                
        self.list_of_RC = list_of_RC
        self.action = action        
        self.mainRC_df = self. mainRC(self.DF,self.list_of_RC)        
        self.updated=self.Merge(self.DF,self.mapping_dict['Part Type'],self.mapping_dict['Defect Type'],self.mapping_dict['Product Type'],self.merge_columns)
        
    def mainRC(self,DF,list_of_RC):
        if self.version=='mainRC':
            DF=DF[DF['RC_ID'].isin(list_of_RC)]
            
    def Abnormal(DF,ABNORMAL):
            #刪除PART+keyword對不到parttype的data
            Ab1=DF[(DF['料號前四碼'].notna() & DF['Key Word'].notna()) & (DF['PART_TYPE'].isna())]
            DF=DF.drop(Ab1.index)
            #刪除no defect卻有用料的data
            Ab2=DF[(DF['SYMPTOM']=='No Defect') & (DF['PART_NO'].notna())]
            DF=DF.drop(Ab2.index)
            #匯入defect type 不會用到的 Parts type_20210518檢查異常資料(待補)

            return DF,AB1,AB2 