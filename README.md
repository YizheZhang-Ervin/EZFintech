# ezfintech
_____
  
## Introduction  
沪深股票数据API:
- 数据  
    日数据(当日、4日数据)  
    年数据(一年的数据)  
    周期数据(日/周/月数据)  
    区间数据(起止日期内的数据)  
    实时数据(未开发)  
    多只股票合表数据(未开发)  
- 数据来源包括: Netease,Sohu,StockStar  
- 数据可视化: K线图,回归分析,相关性分析  
- 股票金融相关知识    
  
_____
  
## 依赖包  
pandas,requests,mplfinance  
  
_____
  
## 使用方式
### 安装  
python pip install ezfintech  
  
### 导入   
import ezfintech.stockData as ezd    
import ezfintech.stockAnalysis as eza  
import ezfintech.stockKnowledge as ezk    
  
_____
  
### 日数据  
ezd.getStockByDay(stockCode,day="today",source="126")  
stockCode:"XXXXXXX"
day: "today" / "4d"  
source: "126"  
  
## 年数据  
ezd.getStockByYear(stockCode,year="2020",adjust="klinederc",source="126")  
stockCode:"XXXXXXX"
year: "YYYY"   
adjust: "kline" / "klinederc"    
source: "126"  
  
### 周期数据  
ezd.getStockByPeriod(stockCode,period="week",adjust="klinederc",source="126")  
stockCode:"XXXXXXX"
period: "day" / "week" / "month"  
adjust: "kline" / "klinederc"   
source: "126" / "stockstar"  
  
### 区间数据  
ezd.getStockByTwoDate(stockCode,startDate="20210301",endDate="20210308",source="sohu")  
stockCode:"XXXXXX"
startDate: "YYYYMMDD"  
endDate: "YYYYMMDD"  
source: "sohu"  
  
_____
  
### K线图  
eza.plotKLine(data,movingAvg=(3,6,9),plotType="candle",startDate="",endDate="")  
data: pd.Dataframe  
movingAvg: (X1,X2,X3) or X1    
plotType: "candle" / "line" / "renko" / "pnf"  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
  
### 回归分析  
eza.plotKLine(data,movingAvg=(3,6,9),plotType="candle",startDate="",endDate="")  
data: pd.Dataframe  
movingAvg: (period1,period2,period3...) or period1  
plotType: "candle" / "line" / "renko" / "pnf"  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
  
### 相关性分析  
eza.regressionAnalysis(stock1,stock2,startDate="",endDate=""):
stock1/stock2: pd.DataFrame  
startDate: "YYYY-MM-DD"  
endDate: "YYYY-MM-DD"  
regressDeg: num  
  
_____
  
### 股票知识
ezk.getStockKnowledge()  
  
### 金融分析知识  
ezk.getFinanceAnalysisKnowledge()  
  
### 量化投资知识  
ezk.getQuantitativeInvestmentKnowledge()  
  