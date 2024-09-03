import pandas as pd
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
})
st.write(df)

option = st.selectbox(
'Which number do you like best?',
df['first column'])
'You selected: ', option

add_selectbox = st.sidebar.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone')
)

st.write("DB username:", st.secrets["DB_USERNAME"])
st.write("DB password:", st.secrets["DB_TOKEN"])
