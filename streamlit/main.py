import streamlit as st
import pandas

data = {
    'Series_1': [1, 2, 3, 4, 5],
    'Series_2': [10, 20, 30, 40, 50]
}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Indroducing Streamlit in Automate Everything with Python')
st.write('''This is our Web App.
Enjoy it!
''')

st.write(df)