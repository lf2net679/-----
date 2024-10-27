import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from io import StringIO

# 設置頁面
st.set_page_config(page_title="靈活數據分析應用 by OJPT01", layout="wide")
st.title("靈活數據分析應用")
st.caption("由 OJPT01 製作")

# 文件上傳
uploaded_file = st.file_uploader("選擇一個 CSV 或 JSON 文件", type=["csv", "json"])

@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.name.endswith('.json'):
        data = pd.read_json(file)
    return data

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.success("文件上傳成功！")

    # 側邊欄
    st.sidebar.header("選擇功能")
    page = st.sidebar.radio("選擇頁面", ["數據概覽", "數據可視化", "相關性分析"])

    if page == "數據概覽":
        st.header("數據概覽")
        st.write(data.head())
        st.write("數據形狀：", data.shape)
        st.write("數據描述：")
        st.write(data.describe())

    elif page == "數據可視化":
        st.header("數據可視化")
        
        # 選擇要可視化的列
        columns = st.multiselect("選擇要可視化的列", data.columns)
        
        if columns:
            # 直方圖
            st.subheader("直方圖")
            for col in columns:
                fig, ax = plt.subplots()
                sns.histplot(data[col], kde=True, ax=ax)
                ax.set_title(f'{col} 分佈圖')
                st.pyplot(fig)

            # 箱型圖
            st.subheader("箱型圖")
            fig, ax = plt.subplots()
            sns.boxplot(data=data[columns])
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            st.pyplot(fig)

            # 散點圖矩陣
            if len(columns) > 1:
                st.subheader("散點圖矩陣")
                fig = sns.pairplot(data[columns], height=2.5)
                st.pyplot(fig)

    elif page == "相關性分析":
        st.header("相關性分析")
        
        # 相關性熱力圖
        st.subheader("相關性熱力圖")
        corr = data.corr()
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

        # 選擇要分析的列
        target = st.selectbox("選擇目標變量", data.columns)
        features = st.multiselect("選擇特徵變量", [col for col in data.columns if col != target])

        if target and features:
            st.subheader(f"{target} 與選定特徵的關係")
            for feature in features:
                fig, ax = plt.subplots()
                sns.scatterplot(data=data, x=feature, y=target, ax=ax)
                ax.set_title(f'{feature} vs {target}')
                st.pyplot(fig)

# 添加頁腳
st.sidebar.markdown("---")
st.sidebar.markdown("由 Streamlit 強力驅動")
st.sidebar.markdown("OJPT01 製作")
