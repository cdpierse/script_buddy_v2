import streamlit as st
from utils import load_model, generate
import time
import json

# model, tokenizer = load_model()
@st.cache(allow_output_mutation=True)
def loader():
    return load_model()


def main():
    st.title(" Script Buddy *v2*")
    st.write("""
    Film Script Language Generation with GPT2
    ***
    """)
    model, tokenizer = loader()
    max_length = st.sidebar.slider(
        """ Max Script Length 
        (Longer length, slower generation)""",
        50,
        1000
    )
    context = st.sidebar.text_area("Context")
    if st.sidebar.button("Generate"):
        start_time = time.time()
        if context:
            sample = generate(model,tokenizer,input_text=context,max_length=max_length)
        else: 
            with open('data/generated/samples.json','r') as f:
                scripts = json.load(f)
            sample = [scripts[1342]]
            print(sample)
            # sample = generate(model,tokenizer,max_length=max_length)
            
        end_time = time.time()

        print(end_time-start_time)
    else:
        sample = ['']

    st.text(sample[0])
    
    


main()