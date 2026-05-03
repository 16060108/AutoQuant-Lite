import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def plot_strategy(df, stock_code):
    """
    画K线、均线、买卖信号、收益曲线
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # ✅ 这里我帮你改好了窗口标题
    fig.canvas.manager.set_window_title("AutoQuant-Lite - 量化回测工具")

    # 收盘价 + 均线
    ax1.plot(df["trade_date"], df["close"], label="收盘价", color="#333333", linewidth=1.2)
    ax1.plot(df["trade_date"], df["MA5"], label="MA5", color="#ff4d4d", linewidth=1.1)
    ax1.plot(df["trade_date"], df["MA10"], label="MA10", color="#009933", linewidth=1.1)

    # 买卖点
    buy = df[df["signal"] == 1]
    sell = df[df["signal"] == 0]
    ax1.scatter(buy["trade_date"], buy["close"], label="买入", color="red", marker="^", s=60, zorder=5)
    ax1.scatter(sell["trade_date"], sell["close"], label="卖出", color="green", marker="v", s=60, zorder=5)

    ax1.set_title(f"{stock_code} 双均线策略", fontsize=14)
    ax1.legend()
    ax1.grid(alpha=0.3)

    # 收益曲线
    ax2.plot(df["trade_date"], df["cumulative_strategy"], label="策略净值", color="#ff2222", linewidth=1.5)
    ax2.plot(df["trade_date"], df["cumulative_market"], label="持有不动", color="#2222ff", linewidth=1.5)
    ax2.legend()
    ax2.grid(alpha=0.3)
    ax2.set_title("净值曲线", fontsize=14)

    plt.tight_layout()
    plt.show()