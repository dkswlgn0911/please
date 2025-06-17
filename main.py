import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv("buildings.csv", encoding="cp949").dropna()
top10 = df.sort_values(by="건축물총면적 (㎡)", ascending=False).head(10)

# 시각화
plt.figure(figsize=(12, 6))
plt.bar(top10["자치구별(2)"], top10["건축물총면적 (㎡)"], color="skyblue")
plt.title("건축물 연면적이 가장 큰 10개 자치구")
plt.xlabel("자치구")
plt.ylabel("건축물 총면적 (㎡)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# 흰 화면 문제 방지: 이미지로 저장
plt.savefig("top10_building_area.png", dpi=300)
plt.show()
