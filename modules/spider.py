import akshare as ak
import pandas as pd

def crawl_stock_data(stock_code, start_date, end_date):
    """
    通用股票数据爬虫（不写死任何参数！）
    """
    df = ak.stock_zh_a_hist(
        symbol=stock_code,
        period="daily",
        start_date=start_date,
        end_date=end_date,
        adjust="qfq"
    )
    
    # 统一列名
    df = df[["日期", "开盘", "最高", "最低", "收盘", "成交量"]]
    df.columns = ["trade_date", "open", "high", "low", "close", "volume"]
    
    print(f"✅ 成功获取【{stock_code}】数据，共 {len(df)} 条")
    return df