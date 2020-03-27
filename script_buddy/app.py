import streamlit as st
from utils import load_model, generate


# model, tokenizer = load_model()

# sample = generate(model,tokenizer,input_text="          LOCHLAINN looks into DONNACHAS' eyes and feels his erection grow.    ",max_length=600)

st.write("""
# Script Buddy *v2*
Film Script Language Generation with GPT2
***

""")


st.text("hello")

st.sidebar.slider(
    "Max Script Length (Longer length, slower generation)",
    50,
    1000
    )

st.sidebar.button("Generate")
st.sidebar.progress(50)
st.spinner()

