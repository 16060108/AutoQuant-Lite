import pandas as pd
import numpy as np

def run_backtest(df):
    """
    策略回测：计算收益、回撤、胜率
    """
    df = df.copy()

    # 计算每日收益
    df["strategy_return"] = df["signal"].shift(1) * df["daily_return"]

    # 累计收益
    df["cumulative_market"] = (1 + df["daily_return"]).cumprod()
    df["cumulative_strategy"] = (1 + df["strategy_return"]).cumprod()

    # 最大回撤
    df["cum_max"] = df["cumulative_strategy"].cummax()
    df["drawdown"] = (df["cumulative_strategy"] - df["cum_max"]) / df["cum_max"]
    max_drawdown = df["drawdown"].min()

    # 总收益
    total_market = df["cumulative_market"].iloc[-1] - 1
    total_strategy = df["cumulative_strategy"].iloc[-1] - 1

    # 胜率（盈利天数占比）
    win_days = (df["strategy_return"] > 0).sum()
    total_days = (df["strategy_return"].notna()).sum()
    win_rate = win_days / total_days if total_days > 0 else 0

    # 输出回测报告
    print("\n" + "="*50)
    print("📊 双均线策略回测报告")
    print("="*50)
    print(f"📈 基准收益（持有不动）：{total_market:.2%}")
    print(f"🚀 策略收益：{total_strategy:.2%}")
    print(f"📉 最大回撤：{max_drawdown:.2%}")
    print(f"✅ 交易胜率：{win_rate:.2%}")
    print("="*50)

    return df