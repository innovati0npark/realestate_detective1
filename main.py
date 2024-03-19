import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import apartment as apartment
import multigen
import solo
import office
# 좌측 메인메뉴
with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home", "아파트", "연립/다세대", "단독/다가구", "오피스텔", ],
    icons = ["house", "building", "house", "house" ,"building"],
    menu_icon = "cast",
    default_index = 0,
    # "분양/입주권", "상업/사무용", "토지", "공장/창고" , "Ranking"
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



#-------------------------------------------------------------------



elif selected=="아파트":
    with st.sidebar:
        page = st.radio('페이지 선택', ['매매', '전월세'])

    if page == "매매":
        apartment.sell()



    elif page == '전월세':
        apartment.lease()



#-------------------------------------------------------------------



elif selected=="연립/다세대":
    with st.sidebar:
        page = st.radio('거래유형', ['매매', '전월세'])
    if page == "매매":
        multigen.sell()



    elif page == "전월세":
        multigen.lease()



#-------------------------------------------------------------------



elif selected=="단독/다가구":
    with st.sidebar:
        page = st.radio('거래유형', ['매매', '전월세'])
    if page == "매매":
        solo.sell()



    elif page == "전월세":
        solo.lease()



#-------------------------------------------------------------------



elif selected=="오피스텔":
    with st.sidebar:
        page = st.radio('거래유형', ['매매', '전월세'])


    if page == "매매":
        office.sell()



    elif page == "전월세":
        office.lease()
        




#-------------------------------------------------------------------





# elif selected=="분양/입주권":
#     st.header(":building_construction: 분양/입주권")
#     st.sidebar.title('분양/입주권_매매')




# elif selected=="상업/사무용_매매":
#     st.header(":classical_building: 상업/사무용")
#     st.sidebar.title('상업/사무용')




# elif selected=="토지_매매":
#     st.header(":earth_asia: 토지")
#     st.sidebar.title('토지_매매')



# elif selected=="공장/창고":
#     st.header(":earth_asia: 공장/창고")
#     st.sidebar.title('공장/창고')



# elif selected=="Ranking":
#     st.header(":star2: Ranking")
#     st.sidebar.title('Ranking')