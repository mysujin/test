import streamlit as st

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('MBTI 박사')

content = st.text_input('MBTI에 관한 궁금증을 물어보세요')

if st.button('MBTI 요청하기'):
    with st.spinner('답변 대기 중 ...'):
        result = chat_model.predict(content + "에 대해 상담을 해줘")
        st.write(result)



