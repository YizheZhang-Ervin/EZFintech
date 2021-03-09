__FileName__    =  'stockAnalysis.py'
__CreatedDate__ = '2021/03/08 16:20:12'
__Author__      =  'Yizhe Zhang'
__WebSite__     = 'http://ervinzhang.pythonanywhere.com/'

import pandas as pd
import mplfinance as mpf
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def dateProcess(startDate,endDate,data):
    if startDate=="":
        startDate = data.index.min()
    if endDate=="":
        endDate = data.index.max()
    if type(startDate) != pd._libs.tslibs.timestamps.Timestamp:
        startDate = datetime.strptime(startDate,'%Y-%m-%d')
    if type(endDate) != pd._libs.tslibs.timestamps.Timestamp:
        endDate = datetime.strptime(endDate,'%Y-%m-%d')
    return startDate,endDate

def dataConcat(stock1,stock2):
    data = pd.concat([stock1["Close"],stock2["Close"]],axis=1)
    data.columns = ["stock1","stock2"]
    return data

def plotKLine(data,movingAvg=(3,6,9),plotType="candle",startDate="",endDate=""):
    """
        data: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)
        movingAvg: (period1,period2,period3...) or period1   # 移动平均时间
        plotType: "candle" / "line" / "renko" / "pnf"
        startDate: "YYYY-MM-DD"
        endDate: "YYYY-MM-DD"
    """
    try:
        startDate,endDate = dateProcess(startDate,endDate,data)
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

def regressionAnalysis(stock1,stock2,startDate="",endDate="",regressDeg=1):
    """
        stock1/stock2: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)
        startDate: "YYYY-MM-DD"
        endDate: "YYYY-MM-DD"
        regressDeg: num  # 线性回归的次方
    """

    # 数据合并
    data = dataConcat(stock1,stock2)
    # 日期处理
    startDate,endDate = dateProcess(startDate,endDate,data)
    # 数据趋势图
    print("(1)数据趋势图")
    data.loc[startDate:endDate].plot(secondary_y="stock2",figsize=(10,6))
    plt.show()
    # 股票之间变化情况
    rst = np.log(data/data.shift(1))
    # kde图
    print("(2)散点图/KDE图")
    pd.plotting.scatter_matrix(rst,alpha=0.2,diagonal="kde",figsize=(10,6))
    plt.show()
    # 回归方程(一次函数)
    # 去除NaN
    rst.dropna(inplace=True)
    # 求回归系数
    reg = np.polyfit(rst["stock1"],rst["stock2"],deg=regressDeg)
    # 散点图
    ax = rst.plot(kind="scatter",x='stock1',y='stock2',figsize=(10,6))
    # 直线一次函数
    print("(3)线性回归图")
    ax.plot(rst["stock1"],np.polyval(reg,rst["stock1"]),"r")
    plt.show()

def correlationAnalysis(stock1,stock2,startDate="",endDate="",movingAvg=5):
    """
        stock1/stock2: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)
        startDate: "YYYY-MM-DD"
        endDate: "YYYY-MM-DD"
        movingAvg: num
    """

    if movingAvg>len(stock1)-1:
        return "Moving Average Exceed!"
    # 数据合并
    data = dataConcat(stock1,stock2)
    # 日期处理
    startDate,endDate = dateProcess(startDate,endDate,data)
    # 数据与前一天相除
    rst = np.log(data/data.shift(1))
    # 去除NaN
    rst.dropna(inplace=True)
    # 相关系数
    print("(1)相关系数")
    print(rst.corr())
    # 随年份变化，计算相关系数的变化情况
    print("(2)相关系数随年份变化的情况")
    rst["stock1"].rolling(movingAvg).corr(rst["stock2"]).plot(figsize=(10,6))
    plt.show()