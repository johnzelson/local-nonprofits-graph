
# py -m pip install graphviz
# py -m pip install streamlit-d3graph
# py -m pip install scikit-learn

import streamlit as st
from streamlit_d3graph import d3graph
from d3graph import d3graph, vec2adjmat
import streamlit.components.v1 as components


APP_TITLE = 'Graph People and Connections in Local Nonprofits'
APP_SUB_TITLE = 'Source:  IRS Tax Returns and IRS BMF '


def main():
    st.set_page_config(APP_TITLE, layout="wide") #, layout="wide")
    st.title(APP_TITLE)
    # st.caption(APP_SUB_TITLE)

    msg = """
    This is a test of graphing people and connections to nonprofit orgs.
    
    """
 
    with open('data/g1.html',encoding="utf8") as f:
        html_data = f.read()
        
    # Show in webpage
    #st.markdown(msg)

    st.components.v1.html(html_data, scrolling=True, width=1000, height=800)

    # st.markdown(html_data, unsafe_allow_html=True)
    #d3.show(filepath='data/g1.html')

        
if __name__ == "__main__":
    main()
