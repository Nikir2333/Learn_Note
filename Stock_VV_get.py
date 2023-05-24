# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:20:11 2023

@author: Administrator
"""
##CHina Stock value-volume analyse tool

import pandas as pd
import efinance as ef # API:https://efinance.readthedocs.io/en/latest/api/#efinance.stock.get_latest_quote

def get_VV(stock_code,start_time,end_time):
    '''
    Parameters
    ----------
    stock_number : str or list['str']=stock nunber
    beg : str ='19000101'(^Default)
    end : str ='20500101'(^Default)
    klt : str = 1(min);5(5min);15(15min);30(30min);60(60min);101(1day-^Default);102(1week);103(1month)
    fqt : int = 1(Adjust Right-^Default)   
    Returns DataFrame or dict['str'] 
    -------
    None.

    '''
    code = str(stock_code)
    start_time = str(start_time)
    end_time =str(end_time)
    stock_data = ef.stock.get_quote_history(code,start_time,end_time) #get_stock_date_data
    data0 = stock_data.rename(columns = {stock_data.columns[2]:'date',stock_data.columns[3]:'open',
                                 stock_data.columns[4]:'close',stock_data.columns[5]:'high',
                                 stock_data.columns[6]:'low',stock_data.columns[8]:'volume',
                                 stock_data.columns[-1]:'turnover_rate'})
    
    data1=data0[['date','open','close','high','low','volume','turnover_rate']] #get new dataframe
    pd.DataFrame(data1['volume'])
    data1['volume']=data1['volume'].astype(float).astype(int)/10000
    pd.DataFrame(data1['volume'])
    data1['volume']=data1['volume'].round(2)#数据组的重新确认，以免值域不对
    data1['date']=pd.to_datetime(data1['date'])
    data2=data1.set_index('date',drop=True)
    data2.to_excel(code + '_Date.xlsx')    
    
    return print(data2)


        
if __name__ == "__main__" :
    stock_code=301071
    start_time=20230101
    end_time=202305023
    get_VV(stock_code,start_time,end_time)
    