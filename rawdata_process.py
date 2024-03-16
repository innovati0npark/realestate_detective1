import pandas as pd

# # 서울 경기 아파트 매매
# # 파일 경로

# file1 = '서울_아파트_매매\아파트(매매)_실거래가_서울_202301_202312.csv'
# file2 = '서울_아파트_매매\아파트(매매)_실거래가_서울_202201_202212.csv'
# file3 = '서울_아파트_매매\아파트(매매)_실거래가_서울_202101_202112.csv'
# file4 = '서울_아파트_매매\아파트(매매)_실거래가_서울_202001_202012.csv'
# file5 = '서울_아파트_매매\아파트(매매)_실거래가_서울_201901_201912.csv'
# file6 = '서울_아파트_매매\아파트(매매)_실거래가_경기_202301_202312.csv'
# file7 = '서울_아파트_매매\아파트(매매)_실거래가_경기_202201_202212.csv'
# file8 = '서울_아파트_매매\아파트(매매)_실거래가_경기_202101_202112.csv'
# file9 = '서울_아파트_매매\아파트(매매)_실거래가_경기_202001_202012.csv'
# file10 ='서울_아파트_매매\아파트(매매)_실거래가_경기_201901_201912.csv'

# # CSV 파일 읽기
# df1 = pd.read_csv(file1, encoding="CP949")
# df2 = pd.read_csv(file2, encoding="CP949")
# df3 = pd.read_csv(file3, encoding="CP949")
# df4 = pd.read_csv(file4, encoding="CP949")
# df5 = pd.read_csv(file5, encoding="CP949")
# df6 = pd.read_csv(file6, encoding="CP949")
# df7 = pd.read_csv(file7, encoding="CP949")
# df8 = pd.read_csv(file8, encoding="CP949")
# df9 = pd.read_csv(file9, encoding="CP949")
# df10 = pd.read_csv(file10, encoding="CP949")

# # 두 데이터프레임을 합치기
# # .conmcat함수는 리스트로 연결하려는 df를 주면되고 기본적으로 세로방향으로 연결
# # 가로로 연결하고 싶으면 axis=1 입력하면됨.
# merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])

# # 합쳐진 데이터프레임을 새로운 CSV 파일로 저장
# merged_df.to_csv('서울_아파트_매매\\apartment_seoul+ggd.csv', index=False, encoding='utf-8-sig')


# 서울 경기 아파트 전월세
# 파일 경로

file1 = '서울_아파트_전월세\아파트(전월세)_실거래가_서울_202301_202312.csv'
file2 = '서울_아파트_전월세\아파트(전월세)_실거래가_서울_202201_202212.csv'
file3 = '서울_아파트_전월세\아파트(전월세)_실거래가_서울_202101_202112.csv'
file4 = '서울_아파트_전월세\아파트(전월세)_실거래가_서울_202001_202012.csv'
file5 = '서울_아파트_전월세\아파트(전월세)_실거래가_서울_201901_201912.csv'
file6 = '서울_아파트_전월세\아파트(전월세)_실거래가_경기_202301_202312.csv'
file7 = '서울_아파트_전월세\아파트(전월세)_실거래가_경기_202201_202212.csv'
file8 = '서울_아파트_전월세\아파트(전월세)_실거래가_경기_202101_202112.csv'
file9 = '서울_아파트_전월세\아파트(전월세)_실거래가_경기_202001_202012.csv'
file10 ='서울_아파트_전월세\아파트(전월세)_실거래가_경기_201901_201912.csv'

# CSV 파일 읽기
df1 = pd.read_csv(file1, encoding="CP949")
df2 = pd.read_csv(file2, encoding="CP949")
df3 = pd.read_csv(file3, encoding="CP949")
df4 = pd.read_csv(file4, encoding="CP949")
df5 = pd.read_csv(file5, encoding="CP949")
df6 = pd.read_csv(file6, encoding="CP949")
df7 = pd.read_csv(file7, encoding="CP949")
df8 = pd.read_csv(file8, encoding="CP949")
df9 = pd.read_csv(file9, encoding="CP949")
df10 = pd.read_csv(file10, encoding="CP949")

# 두 데이터프레임을 합치기
# .conmcat함수는 리스트로 연결하려는 df를 주면되고 기본적으로 세로방향으로 연결
# 가로로 연결하고 싶으면 axis=1 입력하면됨.
merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])

# 합쳐진 데이터프레임을 새로운 CSV 파일로 저장
merged_df.to_csv('서울_아파트_전월세\\apartment2_seoul+ggd.csv', index=False, encoding='CP949')




