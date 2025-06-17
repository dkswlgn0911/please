import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 한글 폰트 설정 (리눅스 서버/Streamlit Cloud용)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("서울시 건축물 연면적 Top 10 자치구 시각화")

# 데이터 불러오기
df = pd.read_csv("buildings.csv", encoding="cp949").dropna()
top10 = df.sort_values(by="건축물총면적 (㎡)", ascending=False).head(10)

# 그래프 그리기
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top10["자치구별(2)"], top10["건축물총면적 (㎡)"], color="skyblue")
ax.set_title("건축물 연면적이 가장 큰 10개 자치구")
ax.set_xlabel("자치구")
ax.set_ylabel("건축물 총면적 (㎡)")
plt.xticks(rotation=45)
ax.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

st.pyplot(fig)
