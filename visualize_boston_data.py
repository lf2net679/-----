import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取數據
data = pd.read_csv('boston.csv')

# 設置圖表風格
plt.style.use('seaborn')
sns.set_palette("deep")

# 創建一個函數來保存圖表
def save_plot(fig, filename):
    fig.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)

# 1. 繪製目標變量（MEDV）的分佈圖
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data['MEDV'], kde=True, ax=ax)
ax.set_title('房價分佈圖')
ax.set_xlabel('房價（千美元）')
ax.set_ylabel('頻率')
save_plot(fig, 'house_price_distribution.png')

# 2. 繪製相關性熱力圖
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('特徵相關性熱力圖')
save_plot(fig, 'correlation_heatmap.png')

# 3. 繪製散點圖矩陣
fig = sns.pairplot(data, vars=['MEDV', 'RM', 'LSTAT', 'PTRATIO'], height=2.5)
fig.fig.suptitle('主要特徵散點圖矩陣', y=1.02)
save_plot(fig.fig, 'scatter_matrix.png')

# 4. 繪製箱型圖
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=data, ax=ax)
ax.set_title('特徵箱型圖')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
save_plot(fig, 'boxplot.png')

# 5. 繪製房價與重要特徵的關係圖
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.scatterplot(data=data, x='RM', y='MEDV', ax=axes[0, 0])
axes[0, 0].set_title('房間數量與房價關係')
sns.scatterplot(data=data, x='LSTAT', y='MEDV', ax=axes[0, 1])
axes[0, 1].set_title('低收入人群比例與房價關係')
sns.scatterplot(data=data, x='PTRATIO', y='MEDV', ax=axes[1, 0])
axes[1, 0].set_title('學生教師比例與房價關係')
sns.scatterplot(data=data, x='DIS', y='MEDV', ax=axes[1, 1])
axes[1, 1].set_title('就業中心距離與房價關係')
fig.suptitle('房價與重要特徵的關係', fontsize=16)
save_plot(fig, 'price_vs_features.png')

print("所有圖表已保存為PNG文件。")
