import streamlit as st
import pandas

data = {
    'Series_1': [1, 2, 3, 4, 5],
    'Series_2': [9, 23, 25, 40, 129]
}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Indroducing Streamlit in Automate Everything with Python')
st.write('''This is our Web App.
Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, "in Fahrenheit is ", myslider * 9/5 + 32)