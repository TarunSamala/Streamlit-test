import streamlit as st
import random

st.title('🎲 Tiny Random Number Generator')
st.write('This is a minimal Streamlit app that generates random numbers!')

min_val = st.number_input('Minimum value', value=1)
max_val = st.number_input('Maximum value', value=100)

if st.button('Generate Random Number'):
    result = random.randint(min_val, max_val)
    st.success(f'Your random number: {result}')
