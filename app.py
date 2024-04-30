import streamlit as st
import streamlit.components.v1 as components

def run():
    st.set_page_config(layout="wide")
    iframe_src = "https://levihsu-ootdiffusion.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    run()
