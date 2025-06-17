import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로 및 데이터 불러오기
df = pd.read_csv("buildings.csv", encoding="cp949")
df_cleaned = df.dropna()

# 상위 10개 자치구 추출
top10 = df_cleaned.sort_values(by="건축물총면적 (㎡)", ascending=False).head(10)

# 그래프 시각화
plt.figure(figsize=(12, 6))
plt.bar(top10["자치구별(2)"], top10["건축물총면적 (㎡)"], color="skyblue")
plt.title("건축물 연면적이 가장 큰 10개 자치구")
plt.xlabel("자치구")
plt.ylabel("건축물 총면적 (㎡)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
