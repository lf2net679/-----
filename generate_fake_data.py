import pandas as pd
import numpy as np
import json

# 設置隨機種子以確保可重現性
np.random.seed(42)

# 生成 1000 筆假數據
n_samples = 1000

data = {
    'CRIM': np.random.exponential(scale=0.5, size=n_samples),
    'ZN': np.random.choice([0, 18, 25, 70, 80, 100], size=n_samples, p=[0.7, 0.05, 0.05, 0.05, 0.05, 0.1]),
    'INDUS': np.random.uniform(0, 30, n_samples),
    'CHAS': np.random.choice([0, 1], size=n_samples, p=[0.95, 0.05]),
    'NOX': np.random.uniform(0.3, 0.9, n_samples),
    'RM': np.random.normal(6, 1, n_samples),
    'AGE': np.random.uniform(0, 100, n_samples),
    'DIS': np.random.lognormal(mean=1, sigma=0.5, size=n_samples),
    'RAD': np.random.choice(range(1, 25), size=n_samples),
    'TAX': np.random.uniform(100, 800, n_samples),
    'PTRATIO': np.random.uniform(12, 22, n_samples),
    'B': np.random.uniform(0, 400, n_samples),
    'LSTAT': np.random.lognormal(mean=2, sigma=0.5, size=n_samples),
    'MEDV': np.random.lognormal(mean=3, sigma=0.4, size=n_samples) * 10
}

df = pd.DataFrame(data)

# 保存為 CSV 文件
df.to_csv('boston_fake.csv', index=False)
print("假數據已生成並保存為 boston_fake.csv")

# 保存為 JSON 文件
df.to_json('boston_fake.json', orient='records')
print("假數據已生成並保存為 boston_fake.json")

# 顯示數據的前幾行
print("\n生成的數據預覽：")
print(df.head())

# 顯示數據的基本統計信息
print("\n數據統計信息：")
print(df.describe())
