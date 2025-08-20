import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MBTI 학습 유형 진단",
    page_icon="🧠",
)

# --- 세션 상태 초기화 ---
# 'submitted' 상태가 없는 경우 초기화합니다.
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

def reset_session():
    """세션 상태를 초기화하는 콜백 함수"""
    st.session_state.submitted = False
    # 각 질문의 답변도 초기화할 수 있습니다.
    for i in range(1, 8):
        st.session_state[f'q{i}'] = None

# --- 앱 제목 ---
st.title("🚀 MBTI 기반 학습 유형 진단")
st.markdown("자신의 학습 스타일을 발견하고 더 효과적으로 공부해 보세요!")

# --- 진단 문항 ---
# 각 문항은 라디오 버튼으로 구성됩니다.
q1 = st.radio(
    "1. 새로운 과제를 받을 때, 나는...",
    ("먼저 전체적인 그림과 목표를 이해하려고 한다. (N)", "구체적인 지침과 세부 사항부터 확인한다. (S)"),
    key='q1'
)
q2 = st.radio(
    "2. 팀 프로젝트를 할 때, 나는...",
    ("다른 사람들과 의견을 나누며 아이디어를 얻는다. (E)", "혼자 조용히 생각하며 아이디어를 정리하는 편이다. (I)"),
    key='q2'
)
q3 = st.radio(
    "3. 어려운 문제에 부딪혔을 때, 나는...",
    ("논리적이고 객관적인 기준으로 해결책을 찾는다. (T)", "상황이 사람들에게 미칠 영향을 먼저 고려한다. (F)"),
    key='q3'
)
q4 = st.radio(
    "4. 공부 계획을 세울 때, 나는...",
    ("체계적이고 구체적인 계획을 세우고 지키려고 노력한다. (J)", "상황에 따라 유연하게 계획을 변경하는 것을 선호한다. (P)"),
    key='q4'
)
q5 = st.radio(
    "5. 정보를 받아들일 때, 나는...",
    ("경험하고 관찰한 사실을 더 신뢰한다. (S)", "숨겨진 의미나 가능성을 먼저 생각한다. (N)"),
    key='q5'
)
q6 = st.radio(
    "6. 공부를 마친 후, 나는...",
    ("친구들과 이야기하며 에너지를 얻는다. (E)", "혼자만의 시간을 가지며 재충전한다. (I)"),
    key='q6'
)
q7 = st.radio(
    "7. 피드백을 주고받을 때, 나는...",
    ("진실과 사실에 근거하여 솔직하게 말하는 편이다. (T)", "상대방의 감정을 상하지 않게 하려고 노력한다. (F)"),
    key='q7'
)

# --- 제출 버튼 ---
# 버튼을 누르면 'submitted' 상태가 True로 변경됩니다.
submit_button = st.button("결과 확인하기")

if submit_button:
    st.session_state.submitted = True

# --- 결과 처리 로직 ---
# 제출 버튼이 눌렸고, 모든 질문에 답변했는지 확인합니다.
if st.session_state.submitted:
    # 모든 질문에 답변했는지 확인
    answers = [st.session_state.q1, st.session_state.q2, st.session_state.q3, st.session_state.q4, st.session_state.q5, st.session_state.q6, st.session_state.q7]
    if None in answers:
        st.error("⚠️ 모든 질문에 답변해주세요!")
        st.session_state.submitted = False # 오류 발생 시 제출 상태 초기화
    else:
        # MBTI 유형 계산
        e_score = 0
        i_score = 0
        s_score = 0
        n_score = 0
        t_score = 0
        f_score = 0
        j_score = 0
        p_score = 0

        # 각 답변에서 MBTI 코드 추출 및 점수 계산
        type_codes = {
            'E': ['(E)'], 'I': ['(I)'],
            'S': ['(S)'], 'N': ['(N)'],
            'T': ['(T)'], 'F': ['(F)'],
            'J': ['(J)'], 'P': ['(P)'],
        }

        for ans in answers:
            code = ans.split(' ')[-1] # 답변 문자열에서 '(X)' 부분 추출
            if code in type_codes['E']: e_score += 1
            if code in type_codes['I']: i_score += 1
            if code in type_codes['S']: s_score += 1
            if code in type_codes['N']: n_score += 1
            if code in type_codes['T']: t_score += 1
            if code in type_codes['F']: f_score += 1
            if code in type_codes['J']: j_score += 1
            if code in type_codes['P']: p_score += 1

        # 최종 MBTI 유형 결정
        mbti_type = ""
        mbti_type += "E" if e_score > i_score else "I"
        mbti_type += "N" if n_score > s_score else "S"
        mbti_type += "T" if t_score > f_score else "F"
        mbti_type += "J" if j_score > p_score else "P"

        # 결과 설명 (예시)
        learning_styles = {
            "ISTJ": "**소금형 🧂:** 계획을 세우고 꾸준히 실천하는 것을 선호합니다. 실제 데이터를 바탕으로 한 논리적인 학습이 효과적입니다.",
            "ISFJ": "**권력형 💪:** 다른 사람에게 도움이 되는 공부를 할 때 동기부여가 됩니다. 세부 사항을 꼼꼼히 기억하고 실용적인 지식을 중요하게 생각합니다.",
            "INFJ": "**예언자형 🔮:** 아이디어의 이면에 있는 깊은 의미를 탐구하는 것을 즐깁니다. 통찰력을 바탕으로 한 창의적인 학습 방식에 강합니다.",
            "INTJ": "**과학자형 🔬:** 복잡한 이론과 시스템을 이해하는 데 뛰어납니다. 논리적이고 체계적인 학습 환경에서 최고의 효율을 보입니다.",
            "ISTP": "**백과사전형 📖:** 원리를 파악하고 직접 문제를 해결하는 실습 위주의 학습을 선호합니다. 효율성을 중시하며, 유연한 사고를 가졌습니다.",
            "ISFP": "**성인군자형 😇:** 조화로운 분위기에서 개성과 가치를 표현하며 학습하는 것을 좋아합니다. 실습과 체험을 통한 학습이 효과적입니다.",
            "INFP": "**잔다르크형 👩‍🎨:** 자신의 가치와 신념에 부합하는 내용을 학습할 때 열정을 보입니다. 창의적이고 개방적인 학습 환경을 선호합니다.",
            "INTP": "**아이디어형 💡:** 논리적 분석과 추상적인 개념을 다루는 것을 즐깁니다. 지적 호기심이 왕성하며, 토론과 탐구를 통해 학습합니다.",
            "ESTP": "**활동가형 🏃:** 직접 부딪히고 경험하며 배우는 것을 가장 선호합니다. 활동적이고 사교적인 학습 환경에서 두각을 나타냅니다.",
            "ESFP": "**사교형 🎉:** 즐겁고 활기찬 분위기에서 사람들과 어울리며 학습할 때 가장 효과적입니다. 실용적인 정보와 실습을 좋아합니다.",
            "ENFP": "**스파크형 ✨:** 새로운 아이디어와 가능성을 탐험하는 것을 즐깁니다. 열정적이며, 상상력을 자극하는 다양한 학습 방식을 선호합니다.",
            "ENTP": "**발명가형 👨‍🔬:** 지적인 도전을 즐기며, 기존의 방식에 의문을 제기하고 토론하는 것을 좋아합니다. 복잡한 문제를 해결하는 데 능숙합니다.",
            "ESTJ": "**사업가형 👨‍💼:** 목표 지향적이며, 체계적으로 학습 계획을 실행합니다. 명확하고 논리적인 강의와 실용적인 지식을 선호합니다.",
            "ESFJ": "**친선도모형 🤝:** 다른 사람들과 협력하고 도우며 학습할 때 시너지를 냅니다. 조화로운 관계 속에서 학습 효율이 높아집니다.",
            "ENFJ": "**언변능숙형 🎤:** 사람들을 이끌고 영감을 주며 함께 성장하는 학습을 선호합니다. 의사소통과 협업 기반의 학습에 강합니다.",
            "ENTJ": "**지도자형 👑:** 장기적인 비전을 세우고, 목표 달성을 위해 학습을 전략적으로 활용합니다. 도전적이고 지적인 토론을 즐깁니다."
        }
        
        # --- 결과 출력 ---
        st.balloons()
        st.subheader(f"🎉 당신의 학습 유형은 '{mbti_type}' 입니다!")
        st.markdown(learning_styles.get(mbti_type, "결과를 분석 중입니다."))

        # --- 다시하기 버튼 ---
        # on_click 인자를 사용하여 버튼 클릭 시 reset_session 함수를 호출합니다.
        st.button("다시 진단하기", on_click=reset_session)