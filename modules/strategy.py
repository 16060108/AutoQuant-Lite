import pandas as pd

def dual_ma_strategy(df):
    """
    双均线策略：
    MA5 上穿 MA10 → 买入信号 (1)
    MA5 下穿 MA10 → 卖出信号 (0)
    """
    df = df.copy()
    df["signal"] = 0
    
    # 金叉
    df.loc[df["MA5"] > df["MA10"], "signal"] = 1
    # 死叉
    df.loc[df["MA5"] < df["MA10"], "signal"] = 0
    
    return df