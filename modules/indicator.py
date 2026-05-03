import pandas as pd

def calculate_indicators(df):
    """计算均线、收益率等技术指标"""
    df = df.copy()
    
    # 均线
    df["MA5"] = df["close"].rolling(window=5).mean()
    df["MA10"] = df["close"].rolling(window=10).mean()
    df["MA20"] = df["close"].rolling(window=20).mean()
    
    # 日收益率
    df["daily_return"] = df["close"].pct_change()
    
    # 去除空值
    df = df.dropna()
    return df