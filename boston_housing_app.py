import streamlit as st
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="數據可視化工具", layout="wide")

@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.json'):
        return pd.DataFrame(json.load(file))
    else:
        st.error("不支持的文件格式。請上傳 CSV 或 JSON 文件。")
        return None

def visualize_data(df):
    st.subheader("數據預覽")
    st.write(df.head())

    st.subheader("數據統計")
    st.write(df.describe())

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("相關性熱圖")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("散點矩陣圖")
        fig = px.scatter_matrix(df)
        st.plotly_chart(fig)

    st.subheader("直方圖")
    column = st.selectbox("選擇要顯示直方圖的列", df.columns)
    fig = px.histogram(df, x=column, marginal="box")
    st.plotly_chart(fig)

    st.subheader("箱型圖")
    columns = st.multiselect("選擇要顯示箱型圖的列", df.columns, default=df.select_dtypes(include=[np.number]).columns[:5].tolist())
    fig = px.box(df, y=columns)
    st.plotly_chart(fig)

    st.subheader("散點圖")
    x_axis = st.selectbox("選擇 X 軸", df.columns)
    y_axis = st.selectbox("選擇 Y 軸", df.columns)
    color = st.selectbox("選擇顏色分類（可選）", ["None"] + df.columns.tolist())
    size = st.selectbox("選擇大小分類（可選）", ["None"] + df.columns.tolist())

    fig = px.scatter(df, x=x_axis, y=y_axis, 
                     color=None if color == "None" else color,
                     size=None if size == "None" else size,
                     hover_data=df.columns)
    st.plotly_chart(fig)

    st.subheader("時間序列圖")
    date_columns = df.select_dtypes(include=['datetime64']).columns
    if len(date_columns) > 0:
        date_column = st.selectbox("選擇日期列", date_columns)
        value_column = st.selectbox("選擇值列", df.select_dtypes(include=[np.number]).columns)
        fig = px.line(df, x=date_column, y=value_column)
        st.plotly_chart(fig)
    else:
        st.write("沒有檢測到日期列，無法繪製時間序列圖。")

def main():
    st.title("CSV 和 JSON 數據可視化工具")

    uploaded_file = st.file_uploader("選擇一個 CSV 或 JSON 文件", type=["csv", "json"])
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            visualize_data(df)

if __name__ == "__main__":
    main()