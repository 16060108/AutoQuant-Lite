# ===========================
# 🔥只需要改这里！！！
# ===========================
STOCK_CODE = "600519"     # 改股票代码
START_DATE = "20230101"   # 改开始日期
END_DATE   = "20250520"   # 改结束日期


from modules.spider import crawl_stock_data
from modules.indicator import calculate_indicators
from modules.strategy import dual_ma_strategy
from modules.backtest import run_backtest
from modules.plotter import plot_strategy

print("🚀 启动 AutoQuant-Lite 量化工具")

# 全流程自动化
df = crawl_stock_data(STOCK_CODE, START_DATE, END_DATE)
df = calculate_indicators(df)
df = dual_ma_strategy(df)
df = run_backtest(df)

# 自动保存结果（文件名自动用股票代码）
df.to_csv(f"{STOCK_CODE}_回测结果.csv", index=False, encoding="utf-8-sig")

# 自动画图（标题自动用股票代码）
plot_strategy(df, STOCK_CODE)

print(f"\n✅ 【{STOCK_CODE}】回测完成！")
