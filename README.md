# EZFintech
Pypi: ezfintech  
  
## 1. Introduction  
沪深股票数据  
- 数据来源包括: Netease,Sohu,StockStar  
- 数据API(ezfintech.stockData)  
    - 日数据(当日、4日数据)  
    - 年数据(一年的数据)  
    - 周期数据(日/周/月数据)  
    - 区间数据(起止日期内的数据)  
    - 实时数据(未开发)  
    - 多只股票合表数据(未开发)  
- 数据可视化(ezfintech.stockVisualization)  
    - K线图
    - 金叉死叉  
    - 布林带  
- 数据分析(ezfintech.stockAnalysis)  
    - 回归分析
    - 相关性分析  
- 股票金融相关知识(ezfintech.stockKnowledge)  
- 股票模型(ezfintech.stockAlgorithms.EZLSTM)
  
## 2. 依赖包  
numpy,pandas,matplotlib,requests,mplfinance,pandas_datareader  
  
## 3. 使用方式
### 3.1 安装  
python pip install ezfintech  
  
### 3.2 导入   
import ezfintech.stockData as ezd    
import ezfintech.stockAnalysis as eza  
import ezfintech.stockVisualization as ezv  
import ezfintech.stockKnowledge as ezk    
import ezfintech.stockModels.EZLSTM as ezm    
  
### 3.3 使用

#### (1) 获取股票数据
_____
  
- 日数据  
```
ezd.getStockByDay(stockCode,day="today",source="126")  
stockCode:"XXXXXXX"
day: "today" / "4d"  
source: "126"  
```
  
- 年数据  
```
ezd.getStockByYear(stockCode,year="2020",adjust="klinederc",source="126")  
stockCode:"XXXXXXX"
year: "YYYY"   
adjust: "kline" / "klinederc"    
source: "126"  
```
  
- 周期数据  
```
ezd.getStockByPeriod(stockCode,period="week",adjust="klinederc",source="126")  
stockCode:"XXXXXXX"
period: "day" / "week" / "month"  
adjust: "kline" / "klinederc"   
source: "126" / "stockstar"  
```
  
- 区间数据  
```
ezd.getStockByTwoDate(stockCode,startDate="20210301",endDate="20210308",source="sohu")  
stockCode:"XXXXXX"
startDate: "YYYYMMDD"  
endDate: "YYYYMMDD"  
source: "sohu"  
```
  
- 获取FamaFrench因子数据  
```
ezd.getFamaFrenchFactors(ffType="3factors",startDate="",endDate="")  
ffType: 3factors/5factors  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
```
  
#### (2) 股票数据可视化
_____
  
- K线图  
```
ezv.plotKLine(data,movingAvg=(3,6,9),plotType="candle",startDate="",endDate="")  
data: pd.Dataframe  
movingAvg: (X1,X2,X3) or X1    
plotType: "candle" / "line" / "renko" / "pnf"  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
```
  
- 金叉死叉  
```
ezv.plotDoubleCross(data,priceType="Close",movingAvg=(5,40),startDate="",endDate="",returnData=False)  
data: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)  
priceType: Close/Adj Close/Open/High/Low  
movingAvg: (period1,period2)  
startDate: "YYYY-MM-DD"   
endDate: "YYYY-MM-DD"  
returnData: True/False  
```  
  
- 布林带  
```
ezv.plotBollingerBand(data,priceType="Close",n=2,movingAvg=40,startDate="",endDate="",returnData=False)  
data: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)  
priceType: Close/Adj Close/Open/High/Low  
n: how many times of deviation   
movingAvg: period  # 移动平均时间  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
returnData: True/False  
```
  
#### (3) 股票数据分析
_____  
  
- 双股票回归分析   
```  
eza.regression2Stocks(stock1,stock2,startDate="",endDate="",regressDeg=1)  
stock1/stock2: pd.DataFrame with Date(index), Open/High/Low/Close/Volume(Columns)  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
regressDeg: num  # 线性回归的次方  
```  
  
- 自定义OLS分析   
```  
eza.OLS(X,Y)  
Y: T x 1  
X: T x N  
```  
  
- 双股票相关性分析  
```  
eza.correlation2Stocks(stock1,stock2,startDate="",endDate="")  
stock1/stock2: pd.DataFrame  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
regressDeg: num  
```
  
#### (4) 股票知识
_____
  
- 股票知识  
```
ezk.getStockKnowledge()  
```
  
-  金融分析知识   
```
ezk.getFinanceAnalysisKnowledge()  
```
  
- 量化投资知识  
```
ezk.getQuantitativeInvestmentKnowledge()  
```
  
#### (4) 股票模型  
_____
  
- LSTM  
```  
ezm.EZLSTM(outputSize, returnSequence)  
outputsize: XX   # 数字  
returnSequence: False/True  
```  