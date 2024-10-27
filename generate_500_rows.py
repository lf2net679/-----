import pandas as pd
import numpy as np

# 設置隨機種子以確保可重現性
np.random.seed(42)

# 生成 500 筆假數據
n_samples = 500

data = {
    '犯罪率': np.random.exponential(scale=0.5, size=n_samples),
    '大型住宅區比例': np.random.choice([0, 18, 25, 70, 80, 100], size=n_samples, p=[0.7, 0.05, 0.05, 0.05, 0.05, 0.1]),
    '非零售商業用地比例': np.random.uniform(0, 30, n_samples),
    '是否臨河': np.random.choice([0, 1], size=n_samples, p=[0.95, 0.05]),
    '一氧化氮濃度': np.random.uniform(0.3, 0.9, n_samples),
    '平均房間數': np.random.normal(6, 1, n_samples),
    '1940年前建造的房屋比例': np.random.uniform(0, 100, n_samples),
    '就業中心的加權距離': np.random.lognormal(mean=1, sigma=0.5, size=n_samples),
    '公路可達性指數': np.random.choice(range(1, 25), size=n_samples),
    '財產稅率': np.random.uniform(100, 800, n_samples),
    '師生比例': np.random.uniform(12, 22, n_samples),
    '黑人比例': np.random.uniform(0, 400, n_samples),
    '低收入人口比例': np.random.lognormal(mean=2, sigma=0.5, size=n_samples),
    '房價中位數': np.random.lognormal(mean=3, sigma=0.4, size=n_samples) * 10
}

df = pd.DataFrame(data)

# 保存為 CSV 文件
df.to_csv('boston_fake.csv', index=False)
print("500 筆假數據已生成並保存為 boston_fake.csv")

# 顯示前幾行數據
print(df.head())
