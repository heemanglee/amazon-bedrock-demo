import streamlit as st
import backend as be

st.title("안녕하세요 챗봇입니다")
# 세션 상태에 채팅 기록만 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 이전 대화 내용 표시
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message["text"])

input_text = st.chat_input("질문을 입력하세요.")
if input_text:
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(input_text)

    # 채팅 기록에 사용자 메시지 추가
    st.session_state.chat_history.append({
        "role": "user",
        "text": input_text
    })

    # 메모리 없이 단순 채팅 응답 생성
    chat_response = be.simple_chat(input_text)

    # 챗봇 응답 표시
    with st.chat_message("assistant"):
        st.markdown(chat_response)

    # 채팅 기록에 챗봇 응답 추가
    st.session_state.chat_history.append({
        "role": "assistant",
        "text": chat_response
    })
