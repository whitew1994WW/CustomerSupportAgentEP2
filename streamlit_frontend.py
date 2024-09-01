import streamlit as st
from vector_store import FlowerShopVectorStore

st.set_page_config(layout='wide', page_title='Flower Shop Chatbot', page_icon='💐')
vector_store = FlowerShopVectorStore()

if 'message_history' not in st.session_state:
    st.session_state.message_history = [{'content': "Hiya, Im the flower shop chatbot. How can I help?", 'type': 'assistant'}]

left_col, main_col, right_col = st.columns([1, 2, 1])

# 1. Buttons for chat - Clear Button

with left_col:
    if st.button('Clear Chat'):
        st.session_state.message_history = []

    collection_choice = st.radio('Which collection?', ['faqs', 'inventory'])
        

# 2. Chat history and input
with main_col:
    user_input = st.chat_input("Type here...")

    if user_input:
        if collection_choice == 'faqs':
            related_questions = vector_store.query_faqs(user_input)
        else:
            related_questions = vector_store.query_inventories(user_input)
        st.session_state.message_history.append({'content': user_input, 'type': 'user'})
        st.session_state.message_history.append({'content': related_questions, 'type': 'assistant'})

    for i in range(1, len(st.session_state.message_history) + 1):
        this_message = st.session_state.message_history[-i]
        message_box = st.chat_message(this_message['type'])
        message_box.markdown(this_message['content'])
# 3. State variables

with right_col:
    st.text(st.session_state.message_history)