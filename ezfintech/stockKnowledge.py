__FileName__    =  'stockKnowledge.py'
__CreatedDate__ = '2021/03/08 17:24:34'
__Author__      =  'Yizhe Zhang'
__WebSite__     = 'http://ervinzhang.pythonanywhere.com/'

def getStockKnowledge():
    return """
    股票:凭证
    作用: 证明+分红
    上市/IPO: 企业通过证券交易所公开向社会发股票募集资金
    按业绩分类: 蓝筹股/绩优股/ST股
    按上市地区分类: A股(人民币,T+1,涨跌10%)、B股(外币,交割T+1,收益T+3)、H股(香港,T+0,无涨跌限制)、N股(纽约)、S股(新加坡)
    股票市场构成: 上市公司、投资者、证监会、证券业协会、交易所、证券中介机构
    交易所: 上证所(主板-沪指)、深证所(主板-深成指,中小板,创业板)
    股价影响因素: 公司自身因素、行业因素、市场因素、心理因素、经济因素、政治因素
    A股股票买卖:
        在券商开户委托购买
        交易日(1-5)
        交易时间:
            9:15-9:25开盘集合竞价
            9:30-11:30前市，连续竞价时间
            13:00-15:00后市，连续竞价时间
            14:57-15:00深交所收盘集合竞价时间
        T+1交易
        涨跌限制10%
    """

def getFinanceAnalysisKnowledge():
    return """
    基本面分析
        宏观经济分析: 国家财政政策、货币政策
        行业分析
        公司分析: 财务数据、业绩报告等
    技术面分析
        K线
            红柱(涨):阳线(柱顶部收盘价，柱下部开盘价，线顶部最高价，线底部最低价)
            绿柱(跌):阴线(柱顶部开盘价，柱下部收盘价，线顶部最高价，线底部最低价)
        MA(均线)
        KDJ(随机指标)
        MACD(指数平滑移动平均线)
    """

def getQuantitativeInvestmentKnowledge():
    return """
        概念
            量化投资: 数学模型实现投资策略
            优势: 客观、多角度、跟踪市场发现新模型、决定策略后可回测验证
            量化策略: 固定逻辑分析/判断/决策，自动化交易
            策略周期: 产生想法/学习知识->python实现->回测/模拟交易->实盘交易->优化策略/放弃策略
            输入(行情数据+财务数据+自定义数据+投资经验)
            策略(选股->择时->仓位管理->止盈止损)
            输出(买入信号+卖出信号+交易费用+收益)
        工具
            平台: 聚宽、优矿、米筐、quantopian
            框架: RQAlpha、QUANTAXIS
        ipython
            tab补全
            ?内省
            ！执行系统命令
            %run执行，%paste执行剪贴板，%timeit运行时间，%pdb自动调试
    """