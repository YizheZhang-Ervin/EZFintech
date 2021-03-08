# ezfintech
沪深股票数据API:
- 数据  
    日数据(当日、4日数据)  
    年数据(一年的数据)  
    周期数据(日/周/月数据)  
    区间数据(起止日期内的数据)  
    实时数据(未开发)  
    多只股票合表数据(未开发)  
- 数据来源包括: Netease,Sohu,StockStar  
  
## 使用方式
### 安装  
python pip install ezfintech  
  
### 导入   
import ezfintech.stockData as ez    
  
### 日数据  
ez.getStockByDay(stockCode,day="today",source="126")  
stockCode:"XXXXXXX"
day: "today" / "4d"  
source: "126"  
  
## 年数据  
ez.getStockByYear(stockCode,year="2020",adjust="klinederc",source="126")  
stockCode:"XXXXXXX"
year: "YYYY"   
adjust: "kline" / "klinederc"    
source: "126"  
  
### 周期数据  
ez.getStockByPeriod(stockCode,period="week",adjust="klinederc",source="126")  
stockCode:"XXXXXXX"
period: "day" / "week" / "month"  
adjust: "kline" / "klinederc"   
source: "126" / "stockstar"  
  
### 区间数据  
ez.getStockByTwoDate(stockCode,startDate="20210301",endDate="20210308",source="sohu")  
stockCode:"XXXXXX"
startDate: "YYYYMMDD"  
endDate: "YYYYMMDD"  
source: "sohu"  
  