__FileName__    =  'stockVisualize.py'
__CreatedDate__ = '2021/03/30 13:09:14'
__Author__      =  'Yizhe Zhang'
__WebSite__     = 'http://ervinzhang.pythonanywhere.com/'

import pandas as pd
import mplfinance as mpf
from datetime import datetime
import matplotlib.pyplot as plt

def _dateProcess(startDate,endDate,data):
    if startDate=="":
        startDate = data.index.min()
    if endDate=="":
        endDate = data.index.max()
    if type(startDate) != pd._libs.tslibs.timestamps.Timestamp:
        startDate = datetime.strptime(startDate,'%Y-%m-%d')
    if type(endDate) != pd._libs.tslibs.timestamps.Timestamp:
        endDate = datetime.strptime(endDate,'%Y-%m-%d')
    return startDate,endDate

def plotKLine(data,movingAvg=(3,6,9),plotType="candle",startDate="",endDate=""):
    """
        data: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)
        movingAvg: (period1,period2,period3...) or period1   # 移动平均时间
        plotType: "candle" / "line" / "renko" / "pnf"
        startDate: "YYYY-MM-DD"
        endDate: "YYYY-MM-DD"
    """
    try:
        startDate,endDate = _dateProcess(startDate,endDate,data)
        data2 = data[["Open","High","Low","Close","Volume"]][startDate:endDate]
        mpf.plot(data2,type=plotType,mav=movingAvg,volume=True,show_nontrading=True)
    except KeyError:
        print("KeyError: 请检查数据是否包含Date索引+OHLCV五列")
    except ValueError:
        print("ValueError: 请检查开始、结束日期格式是否为YYYY-MM-DD")
    except TypeError:
        print('TypeError: 请检查图表类型是否为"candle" / "line" / "renko" / "pnf"')
        print('TypeError: 请检查移动平均是否为(period1,period2,period3...)或period1')
    except Exception:
        print("Something wrong with stock data")
    
def plotDoubleCross(data,priceType="Close",movingAvg=(5,40),startDate="",endDate="",returnData=False):
    """
        data: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)
        priceType: Close/Adj Close/Open/High/Low
        movingAvg: (period1,period2)  # 短期移动平均时间,中长期移动平均时间
        startDate: "YYYY-MM-DD"
        endDate: "YYYY-MM-DD"
        returnData: True/False
    """
    data2 = data.copy()

    # datatime process
    startDate,endDate = _dateProcess(startDate,endDate,data2)
    data2 = data2[startDate:endDate]
    
    # moving averages
    data2["ma1"] = data2[priceType].rolling(window=movingAvg[0]).mean()
    data2["ma2"] = data2[priceType].rolling(window=movingAvg[1]).mean()
    data2.dropna(inplace=True)
    
    # time of death cross
    sr1 = data2["ma1"]<data2["ma2"]
    sr2 = data2["ma1"]>=data2["ma2"]
    deathCross = data2[sr1 & sr2.shift(1)]
    
    # time of golden cross
    goldenCross = data2[~(sr1 | sr2.shift(1))]
    
    # plot
    data3 = data2[[priceType,"ma1","ma2"]].dropna()
    data3.plot(figsize=(15,6))
    plt.legend()
    
    print(f"Golden Cross: {[ x.strftime('%F') for x in goldenCross.index]}")
    print(f"Death Cross: {[ x.strftime('%F') for x in deathCross.index]}")
    
    if returnData:
        return goldenCross,deathCross

def plotBollingerBand(data,priceType="Close",n=2,movingAvg=40,startDate="",endDate="",returnData=False):
    """
        data: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)
        priceType: Close/Adj Close/Open/High/Low
        n: how many times of deviation 
        movingAvg: period  # 移动平均时间
        startDate: "YYYY-MM-DD"
        endDate: "YYYY-MM-DD"
        returnData: True/False
    """ 
    data2 = data.copy()
    
    # datatime process
    startDate,endDate = _dateProcess(startDate,endDate,data2)
    data2 = data2[startDate:endDate]
    
    # Bollinger Band
    # a list of every last windowShort days standard deviation

    data2["ma"] = data2[priceType].rolling(window=movingAvg).mean()
    stdList = data2[priceType].rolling(window=movingAvg).std()
    data2["upperBand"] = data2["ma"] + n * stdList
    data2["lowerBand"] = data2["ma"] - n * stdList
    
    # Buy point (MA<lowerBand)
    sr1 = data2["ma"]<data2["lowerBand"]
    sr2 = data2["ma"]>=data2["lowerBand"]
    buyPoint = data2[sr1 & sr2.shift(1)]
    
    # Sell point (MA>UpperBand)
    sr1 = data2["ma"]<data2["upperBand"]
    sr2 = data2["ma"]>=data2["upperBand"]
    sellPoint = data2[~(sr1 | sr2.shift(1))]
    
    # plot
    data3 = data2[[priceType,"ma","upperBand","lowerBand"]].dropna()
    data3.plot(figsize=(15,6))
    plt.legend()
    
    print(f"Buy Point: {[ x.strftime('%F') for x in buyPoint.index]}")
    print(f"Sell Point: {[ x.strftime('%F') for x in sellPoint.index]}")

    if returnData:
        return buyPoint,sellPoint