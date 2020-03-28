import streamlit as st
from utils import load_model, generate


# model, tokenizer = load_model()
@st.cache(allow_output_mutation=True)
def loader():
    return load_model()


def main():
    st.write("""
    # Script Buddy *v2*
    Film Script Language Generation with GPT2
    ***

    """)
    model, tokenizer = loader()
    max_length = st.sidebar.slider(
        """ # Max Script Length /n 
        ## (Longer length, slower generation)""",
        50,
        1000
    )
    
    context = st.sidebar.text_area("Context")
    if st.sidebar.button("Generate"):
        if context:
            sample = generate(model,tokenizer,input_text=context,max_length=max_length)[0]
        else: 
            sample = generate(model,tokenizer,max_length=max_length)[0]
    else:
        sample = ''

    st.text(sample)


main()