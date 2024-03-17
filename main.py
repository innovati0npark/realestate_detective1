import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home", "Apartment", "연립/다세대", "단독/다가구", "오피스텔", "분양/입주권", "상업/사무용", "토지", "공장/창고" , "Ranking"],
    icons = ["house", "rocket","map", "door" ,"prize"],
    menu_icon = "cast",
    default_index = 0,

  )
st.title("Korea realestate_Detective")


#한글 폰트 설정
plt.rc('font', family='D2Coding')



if selected=="Home":
    st.header(":house: Home")
    st.write("내가 알고싶은 유형의 집 시세를 알아 보기")
    st.write("이 서비스는 국토교통부의 부동산 실거래가 데이터를 기반으로 합니다.")
    st.write("RawData출처: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=")
    st.write("아파트, 연립/다세대, 단독/다가구, 오피스텔은 매매와 전월세 정보를 제공합니다.")
    st.write("나머지 유형은 매매만 있습니다.")

elif selected=="Apartment":
    with st.sidebar:
        page = st.radio('페이지 선택', ['매매동향', '전월세동향'])

    if page == "매매동향":
        st.header(":house: Apartment")
        st.sidebar.title('Apartment')  # 왼쪽 탭 이름 설정
        # 메뉴 안 그래프 title
        st.title('서울-경기 아파트 매매동향')

        # 데이터 불러오기, 데이터 형 변환.
        # df = pd.read_csv('서울_아파트_매매\\apartment_seoul+ggd.csv', encoding="CP949")
        df['계약년월'] = pd.to_datetime(df['계약년월'], format='%Y%m')  # 날짜 형식으로 변환
        # df['계약년월'] = pd.to_numeric(df['계약년월'], errors='coerce')
        df['전용면적(㎡)'] = pd.to_numeric(df['전용면적(㎡)'], errors='coerce')  # 전용면적을 숫자로 변환
        df['거래금액(만원)'] = pd.to_numeric(df['거래금액(만원)'], errors='coerce') # 거래금액을 숫자로 변환 / 엑셀에서 통화로 표시된 유형을 일반으로 바꿔줘야함 !!


        # 필터 옵션 설정1_ 연도(기간), 시군구
        selected_year = st.sidebar.slider('년도 선택', min_value=2019, max_value=2023, value=(2019, 2023), step=1)

        # 시군구는 필터내에서 검색할 수 있도록 수정.(multiselect로 수정)
        selected_district = st.sidebar.multiselect('시군구 선택', df['시군구'].unique(), default="경기도 의정부시 고산동")
        if selected_district:
            filtered_df = df[(df['계약년월'].dt.year.between(selected_year[0], selected_year[1])) & (df['시군구'].isin(selected_district))]
        else:
            filtered_df = df[(df['계약년월'].dt.year.between(selected_year[0], selected_year[1]))]

        # 필터 옵션 설정2_ 아파트 전용면적별(multiselect로 수정)

        selected_areas = st.sidebar.multiselect('전용면적(㎡) 선택', ['40이하', '40-60', '60-74', '74-85', '85~101', '101-124', '124-140', '140이상'])

        area_conditions = []            #사용자가 선택한 각 전용면적 범위 조건이 담김.

        for selected_area in selected_areas:
            if selected_area == '40이하':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 0) & (filtered_df['전용면적(㎡)'] <= 40))
            elif selected_area == '40-60':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 40) & (filtered_df['전용면적(㎡)'] <= 60))
            elif selected_area == '60-74':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 60) & (filtered_df['전용면적(㎡)'] <= 74))
            elif selected_area == '74-85':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 74) & (filtered_df['전용면적(㎡)'] <= 85))
            elif selected_area == '85~101':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 85) & (filtered_df['전용면적(㎡)'] <= 101))
            elif selected_area == '101-124':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 101) & (filtered_df['전용면적(㎡)'] <= 124))
            elif selected_area == '124-140':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 125) & (filtered_df['전용면적(㎡)'] <= 140))
            elif selected_area == '140이상':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 140))

        if area_conditions:             # 여러개 조건을 결합하는 부분.
            combined_area_condition = area_conditions[0]
            for condition in area_conditions[1:]:
                combined_area_condition |= condition  # OR 연산자를 사용하여 조건들을 결합

            filtered_df = filtered_df[combined_area_condition]    


            

        # 필터링된 데이터로 그래프 그리기
        filtered_df = filtered_df.sort_values('계약년월')  # 계약년월을 기준으로 데이터 정렬


        average_prices = filtered_df.groupby('계약년월')['거래금액(만원)'].mean()


        # 그래프 그리기
        plt.figure(figsize=(10, 6))
        plt.plot(average_prices.index, average_prices.values, marker='o', linestyle='-')
        plt.xlabel('년도')
        plt.ylabel('평균 거래금액(만원)')
        plt.title(f'{selected_district} 아파트 시세 - 시간별')
        plt.xticks(rotation=45)
        st.pyplot(plt)




    elif page == '전월세동향':
        st.title('서울 아파트 전월세 동향')
        st.sidebar.title('lease')  # 왼쪽 탭 이름 설정
        
        st.header(":house: Apartment")
        st.sidebar.title('Apartment')  # 왼쪽 탭 이름 설정
        # 메뉴 안 그래프 title
        st.title('서울-경기 아파트 전월세동향')

        # 데이터 불러오기, 데이터 형 변환.
        # df = pd.read_csv('서울_아파트_전월세\\apartment2_seoul+ggd.csv', encoding="CP949")
        df['계약년월'] = pd.to_datetime(df['계약년월'], format='%Y%m')  # 날짜 형식으로 변환
        # df['계약년월'] = pd.to_numeric(df['계약년월'], errors='coerce')
        df['전용면적(㎡)'] = pd.to_numeric(df['전용면적(㎡)'], errors='coerce')  # 전용면적을 숫자로 변환
        
        # 금액을 숫자로 변환 / 엑셀에서 통화로 표시된 유형을 일반으로 바꿔줘야함 !!
        df['보증금(만원)'] = pd.to_numeric(df['보증금(만원)'], errors='coerce')
        df['월세금(만원)'] = pd.to_numeric(df['월세금(만원)'], errors='coerce')
        # df['전월세구분']

        # 필터 옵션 설정1_ 연도(기간), 시군구
        selected_year = st.sidebar.slider('년도 선택', min_value=2019, max_value=2023, value=(2019, 2023), step=1)

        # 시군구는 필터내에서 검색할 수 있도록 수정.(multiselect로 수정)
        selected_district = st.sidebar.multiselect('시군구 선택', df['시군구'].unique(), default="경기도 의정부시 고산동")
        if selected_district:
            filtered_df = df[(df['계약년월'].dt.year.between(selected_year[0], selected_year[1])) & (df['시군구'].isin(selected_district))]
        else:
            filtered_df = df[(df['계약년월'].dt.year.between(selected_year[0], selected_year[1]))]

        # 필터 옵션 설정2_ 전월세 안에서도 전세와 월세 선택.
        lease_type = st.sidebar.radio('전세/월세 선택', ['전세', '월세'])

        if lease_type == '전세':
            filtered_df = filtered_df[filtered_df['전월세구분'] == '전세']
        else:
            filtered_df = filtered_df[filtered_df['전월세구분'] == '월세']
        
        # 필터 옵션 설정3_ 아파트 전용면적별(multiselect로 수정)

        selected_areas = st.sidebar.multiselect('전용면적(㎡) 선택', ['40이하', '40-60', '60-74', '74-85', '85~101', '101-124', '124-140', '140이상'])

        area_conditions = []            #사용자가 선택한 각 전용면적 범위 조건이 담김.

        for selected_area in selected_areas:
            if selected_area == '40이하':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 0) & (filtered_df['전용면적(㎡)'] <= 40))
            elif selected_area == '40-60':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 40) & (filtered_df['전용면적(㎡)'] <= 60))
            elif selected_area == '60-74':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 60) & (filtered_df['전용면적(㎡)'] <= 74))
            elif selected_area == '74-85':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 74) & (filtered_df['전용면적(㎡)'] <= 85))
            elif selected_area == '85~101':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 85) & (filtered_df['전용면적(㎡)'] <= 101))
            elif selected_area == '101-124':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 101) & (filtered_df['전용면적(㎡)'] <= 124))
            elif selected_area == '124-140':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 125) & (filtered_df['전용면적(㎡)'] <= 140))
            elif selected_area == '140이상':
                area_conditions.append((filtered_df['전용면적(㎡)'] >= 140))

        if area_conditions:             # 여러개 조건을 결합하는 부분.
            combined_area_condition = area_conditions[0]
            for condition in area_conditions[1:]:
                combined_area_condition |= condition  # OR 연산자를 사용하여 조건들을 결합

            filtered_df = filtered_df[combined_area_condition]    


            

        # 필터링된 데이터로 그래프 그리기
        filtered_df = filtered_df.sort_values('계약년월')  # 계약년월을 기준으로 데이터 정렬


        average_deposit = filtered_df.groupby('계약년월')['보증금(만원)'].mean()
        average_monthly = filtered_df.groupby('계약년월')['월세금(만원)'].mean()

        # 그래프 그리기
        
        if lease_type == '전세':
            filtered_df = filtered_df[filtered_df['전월세구분'] == '전세']
            plt.figure(figsize=(10, 6))
            plt.plot(average_deposit.index, average_deposit.values, marker='o', linestyle='-')
            plt.xlabel('년도')
            plt.ylabel('평균 거래금액(만원)')
            plt.title(f'{selected_district} 아파트 전세 - 시간별')
            plt.xticks(rotation=45)
            st.pyplot(plt)

        else:
            filtered_df = filtered_df[filtered_df['전월세구분'] == '월세']
            plt.figure(figsize=(10, 6))
            plt.plot(average_deposit.index, average_deposit.values, marker='o', linestyle='-')
            plt.xlabel('년도')
            plt.ylabel('평균 거래금액(만원)')
            plt.title(f'{selected_district} 아파트 월세 보증금 - 시간별')
            plt.xticks(rotation=45)
            st.pyplot(plt)

            plt.figure(figsize=(10, 6))
            plt.plot(average_monthly.index, average_monthly.values, marker='o', linestyle='-', color='orange')
            plt.xlabel('년도')
            plt.ylabel('평균 거래금액(만원)')
            plt.title(f'{selected_district} 아파트 월세 - 시간별')
            plt.xticks(rotation=45)
            st.pyplot(plt)


elif selected=="연립/다세대":
    with st.sidebar:
        page = st.radio('거래유형', ['매매', '전월세'])
    if page == "매매":
        st.title(":house: 연립/다세대_매매")
        st.sidebar.title('연립/다세대_매매')



    elif page == "전월세":
        st.title(":house: 연립/다세대_전월세")
        st.sidebar.title('연립/다세대_전월세')
    
elif selected=="단독/다가구":
    with st.sidebar:
        page = st.radio('거래유형', ['매매', '전월세'])
    if page == "매매":
        st.title(":house: 단독/다가구_매매")
        st.sidebar.title('단독/다가구_매매')
    


    elif page == "전월세":
        st.title(":house: 단독/다가구_전월세")
        st.sidebar.title('단독/다가구_전월세')


elif selected=="오피스텔":
    with st.sidebar:
        page = st.radio('거래유형', ['매매', '전월세'])
    if page == "매매":
        st.title(":house: 오피스텔_매매")
        st.sidebar.title('오피스텔_매매')
    


    elif page == "전월세":
        st.title(":house: 오피스텔_전월세")
        st.sidebar.title('오피스텔_전월세')



elif selected=="분양/입주권":
    st.header(":building_construction: 분양/입주권")
    st.sidebar.title('분양/입주권_매매')




elif selected=="상업/사무용_매매":
    st.header(":classical_building: 상업/사무용")
    st.sidebar.title('상업/사무용')




elif selected=="토지_매매":
    st.header(":earth_asia: 토지")
    st.sidebar.title('토지_매매')



elif selected=="공장/창고":
    st.header(":earth_asia: 공장/창고")
    st.sidebar.title('공장/창고')



elif selected=="Ranking":
    st.header(":star2: Ranking")
    st.sidebar.title('Ranking')
# elif selected=="":
#   st.header(":house: Apartment")