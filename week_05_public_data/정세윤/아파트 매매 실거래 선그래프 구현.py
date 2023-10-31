import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_location = r'c:/Windows/Fonts/malgun.ttf'  # Windows\Fonts 폴더
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name, size=8)  # 맑은 고딕으로 설정

df = pd.read_csv("아파트_매매_실거래_평균가격.csv", encoding="UTF-8")
df=df.replace("-",0)
# 고유한 행정구역(시도) 목록
unique_regions = df["행정구역별(2)"].unique()

# 모든 행정구역에 대한 데이터프레임 생성
dfs = []
for region in unique_regions:
    region_df = df[df["행정구역별(2)"] == region]
    region_df = region_df[region_df.columns[2:]]
    region_df = region_df.T.reset_index()
    region_df["index"] = region_df["index"].str[0:4]
    region_df = region_df.astype("float")
    region_df = region_df.groupby(by="index").sum()
    region_df.columns = [region]
    
    if not region_df.empty:  # 데이터프레임이 비어있지 않은 경우에만 추가
        dfs.append(region_df)

if dfs:  # 최소한 하나의 데이터프레임이 있을 때만 합침
    merged_df = pd.concat(dfs, axis=1)
    
    plt.figure(dpi=100)
    plt.title('아파트 매매 실거래 평균가격', size=16)
    plt.grid(linestyle=':')
    merged_df.plot(ax=plt.gca())  # 모든 데이터를 하나의 그래프로 그림
    plt.legend(unique_regions)
    plt.xlabel('년도')
    plt.ylabel('매매가격')
    plt.show()
