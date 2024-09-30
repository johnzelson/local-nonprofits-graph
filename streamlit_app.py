
# py -m pip install graphviz
# py -m pip install streamlit-d3graph
# py -m pip install scikit-learn

import streamlit as st
import pandas as pd
#import folium  
from streamlit_folium import st_folium
import geopandas as gpd
import math
from folium.features import DivIcon  #TODO: move import

import streamlit.components.v1 as components

import csv
import re
import math
from datetime import datetime
import urllib.parse

import graphviz
from streamlit_d3graph import d3graph, vec2adjmat
#import streamlit_d3graph

APP_TITLE = 'Graph People and Connections in Local Nonprofits'
APP_SUB_TITLE = 'Source:  IRS Tax Returns and IRS BMF '

@st.cache_data
def get_people_df():

    all_people_df = pd.read_csv('data/all_people.csv')
    return all_people_df


def orgs_people(all_people_df):
    
    source = []
    target =[]
    weight = []
    
    #for index, row in all_people_df.head(50).iterrows():
    for index, row in all_people_df.iterrows():
        source.append(row['NAME'])
        target.append(row['PersonNm'])
        weight.append(1)
        
    # Create adjacency matrix
    adjmat = vec2adjmat(source, target, weight=weight)

    # Initialize
    d3 = d3graph()

    # Build force-directed graph with default settings
    d3.graph(adjmat)
    #d3.show(filepath='data/g1.html')
    d3.show()
    

def orgs_emphasis_graph(df):
    
    source = []
    target =[]
    weight = []
    
    filt = df['ntee_cat'] != 'no_NTEE'


    #for index, row in all_people_df.head(50).iterrows():
    for index, row in df[filt].iterrows():
        source.append(row['NAME'])
        target.append(row['ntee_cat'])
        weight.append(1)
        
    # Create adjacency matrix
    adjmat = vec2adjmat(source, target, weight=weight)

    # Initialize
    d3 = d3graph()

    # Build force-directed graph with default settings
    d3.graph(adjmat)
    #d3.show(filepath='data/g1.html')
    d3.show()


def people_by_emphasis_graph(df):
    
    source = []
    target =[]
    weight = []


    filt = df['ntee_cat'] != 'no_NTEE'


    #for index, row in all_people_df.head(50).iterrows():
    for index, row in df[filt].iterrows():
        source.append(row['PersonNm'])
        target.append(row['ntee_cat'])
        weight.append(1)
        
    # Create adjacency matrix
    adjmat = vec2adjmat(source, target, weight=weight)

    # Initialize
    d3 = d3graph()

    # Build force-directed graph with default settings
    d3.graph(adjmat)
    #d3.show(filepath='data/g1.html')
    #d3.show()
    d3.show(filepath='data/ppl_emph.html')


def main():
    st.set_page_config(APP_TITLE, layout="wide")
    #st.title(APP_TITLE)
    #st.caption(APP_SUB_TITLE)


    with st.sidebar:
        msg = """
        ## Visualize Affiliations 
        
        Minimize/Expand sidebar:
        - Mouse over sidebar
        - Use  **<** and **>**  in upper right of sidebar

        Double-click on node to focus
        
        """

        st.markdown(msg)

        options = ["", "Orgs and People", "Orgs and Emphasis Area", "People by Emphasis"]
        which_graph = st.selectbox("Pick Graph", options, index=0, key="select_graph",  
                    on_change=None)

        st.write(which_graph)



    all_people_df = get_people_df()


    #st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, 
    #             on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", 
    #             disabled=False, label_visibility="visible")



    if which_graph == 'Orgs and People':            
        orgs_people(all_people_df)
        
    elif which_graph == 'Orgs and Emphasis Area':
        orgs_emphasis_graph(all_people_df)
    
    elif which_graph == 'People by Emphasis':
        people_by_emphasis_graph(all_people_df)

    # using example
    # https://github.com/snehankekre/streamlit-d3graph/blob/main/examples/example.py



if __name__ == "__main__":
    main()
