import streamlit as st
import random

# 가상의 LLM 모델 대답을 생성하기 위한 함수 (실제 LLM 구현은 포함하지 않음)
def generate_fake_responses(prompt):
    # 여기에 LLM을 연결하여 실제 답변을 생성하는 코드를 추가할 수 있습니다.
    # 현재는 단순히 가짜 응답을 반환합니다.
    fake_responses = [
        f"현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. {prompt}",
        f"현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. 현재는 단순히 가짜 응답을 반환합니다. {prompt}"
    ]
    return fake_responses


# Streamlit 애플리케이션의 메인 페이지 설정
def main(default_a, default_b):
    st.title("한국어 챗봇 정성평가 Arena")

    # 사이드바에 규칙과 리더보드 정보 표시
    with st.sidebar:
        st.header("Rules")
        st.write("- Ask any question to two anonymous models (e.g., ChatGPT, Claude, Llama) and vote for the better one!")
        st.write("- You can continue chatting until you identify a winner.")
        st.write("- Vote won't be counted if model identity is revealed during conversation.")
        
        st.header("Arena Elo Leaderboard")
        st.write("We collect 300k+ human votes to compute an Elo-based LLM leaderboard. Find out who is the 🏆 LLM Champion!")


    # 두 모델의 답변을 표시
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Model A")
        response_a = st.text_area(default_a, height=300, key="text_a")
        
    with col2:
        st.subheader("Model B")
        response_b = st.text_area(default_b, height=300, key="text_b")


    if user_question := st.chat_input("Enter your prompt and press ENTER"):
        updated_responses = generate_fake_responses(user_question)  # 여기를 실제 LLM 답변 생성 코드로 교체
        default_a = updated_responses[0]
        default_b = updated_responses[1]
    
    # 두 모델의 답변을 표시
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Vote for Model A'):
            st.success("You voted for Model A!")
        
    with col2:
        if st.button('Vote for Model B'):
            st.success("You voted for Model B!")


# 애플리케이션 실행
if __name__ == "__main__":
    main("", "")
