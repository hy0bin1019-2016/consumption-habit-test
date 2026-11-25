import streamlit as st
import random

# 1. 데이터 구조 (리스트): 소비 유형별 특징 및 랜덤 소비 미션 리스트
practical_features = ["필요한 물건만 꼼꼼히 구매함", "충동구매가 적고 저축을 잘함", "가격만 보다가 품질을 놓칠 수 있음"]
trend_features = ["주변 유행과 트렌드에 민감함", "새로운 물건에 관심이 많음", "유행을 따라가다 과소비할 수 있음"]
eco_features = ["환경과 사회적 가치를 먼저 생각함", "친환경 및 착한 기업 제품을 선호함", "가격 비교를 꼼꼼히 할 필요가 있음"]

saving_missions = [
    "오늘 하루 무지출 챌린지 도전하기!",
    "물건 사기 전 장바구니에 하루만 담아두기!",
    "편의점 1+1 상품 대신 꼭 필요한 것만 사기!",
    "안 쓰는 물건 중고로 판매해 용돈 벌기!"
]

# 2. 함수 (def): 구매 기준과 용돈을 받아 소비 유형, 점수, 특징 리스트를 반환하는 함수
def analyze_spending(criteria, allowance):
    # 3. 선택구조 (if-elif-else): 구매 기준에 따라 유형과 기본 점수 결정
    if criteria == "가성비":
        user_type = "알뜰한 실속형 소비자"
        score = 80
        features = practical_features
    elif criteria == "유행":
        user_type = "트렌드에 민감한 유행추구형 소비자"
        score = 60
        features = trend_features
    else:
        user_type = "가치를 생각하는 착한 소비자"
        score = 85
        features = eco_features

    # 한 달 용돈이 10만 원 이하이면 합리적 소비 지수에 10점 가산
    if allowance <= 10:
        score = score + 10

    return user_type, score, features


# --- Streamlit 웹 화면 구성 ---
st.title("🛍️ 나의 소비 성향 테스트 & 소비 습관 진단기")
st.write("한 달 용돈을 설정하고, 물건을 살 때 가장 중요하게 보는 기준 버튼을 눌러보세요!")

# 슬라이더로 한 달 용돈 입력 받기
monthly_allowance = st.slider(
    "1. 한 달 평균 용돈은 얼마인가요? (단위: 만 원)",
    min_value=1,
    max_value=50,
    value=15
)

st.write("2. 가장 중요하게 보는 구매 기준을 선택하세요:")

# 버튼 3개 나란히 배치 (st.columns 활용)
col1, col2, col3 = st.columns(3)
selected_criteria = ""

with col1:
    if st.button("💰 가성비", use_container_width=True):
        selected_criteria = "가성비"
with col2:
    if st.button("🔥 유행", use_container_width=True):
        selected_criteria = "유행"
with col3:
    if st.button("🌱 환경", use_container_width=True):
        selected_criteria = "환경"

# 버튼 중 하나가 눌렸을 때 결과 분석 및 출력
if selected_criteria != "":
    # 함수 호출
    result_type, result_score, result_features = analyze_spending(selected_criteria, monthly_allowance)

    st.divider()

    # 결과 출력 1: 강조 수치 (Metric)
    st.metric(label="나의 합리적 소비 지수", value=f"{result_score}점")

    # 결과 출력 2: 점수에 따른 축하 효과(balloons) 및 색깔 상자 분기
    if result_score >= 80:
        st.balloons()
        st.success(f"축하합니다! 당신은 **{result_type}**입니다!")
    else:
        st.warning(f"당신은 **{result_type}**입니다! 계획적인 소비 습관을 길러보세요.")

    # 결과 출력 3: 반복구조 (for)를 활용해 특징 리스트를 표(테이블)로 출력
    st.subheader("📋 내 소비 유형의 특징")
    table_data = []
    categories = ["특징", "장점", "주의할 점"]

    for i in range(len(result_features)):
        table_data.append({
            "구분": categories[i],
            "내용": result_features[i]
        })

    st.table(table_data)

    # 결과 출력 4: random 라이브러리를 활용한 오늘의 랜덤 소비 미션 추천
    today_mission = random.choice(saving_missions)
    st.info(f"🎲 **오늘의 랜덤 소비 미션:** {today_mission}")
