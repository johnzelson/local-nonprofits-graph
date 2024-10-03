
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


# test graph
def orgs_blue(df, charge, width, height):


    source = []
    target =[]
    weight = []
    
    #for index, row in all_people_df.head(50).iterrows():
    for index, row in df.iterrows():
        source.append(row['NAME'])
        target.append(row['PersonNm'])
        weight.append(1)
        
    # Create adjacency matrix
    adjmat = vec2adjmat(source, target, weight=weight)

    # Initialize
    d3 = d3graph(charge=charge)

    # Build force-directed graph with default settings
    d3.graph(adjmat)

    # TODO: this should be a seperate def
    # list of unique people, org names/nodes
    orgs = df['NAME'].unique()
    ppl = df['PersonNm'].unique()

    for org in orgs:
        org_id = org.replace(" ", "_")

        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[org_id]['color']="#92b4f0" # 'blue' 
        d3.node_properties[org_id]['size']=15
        d3.node_properties[org_id]['fontsize']=14
        d3.node_properties[org_id]['fontcolor']="#150db8" #"blue"
        #d3.node_properties['Penny']['edge_size']=5
        #d3.node_properties['Penny']['edge_color']='#0000ff' # Blue

    for person in ppl:
        person_id = person.replace(" ", "_")
        person_label = person.title()
        #st.write (org)
        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[person_id]['label']=person_label
        d3.node_properties[person_id]['color']='green' #'#2200FF' 
        d3.node_properties[person_id]['size']=10
        d3.node_properties[person_id]['fontcolor']='black'

    #d3.show(filepath='data/g1.html')
    d3.show(figsize=[width, height])


def people_with_multiple_connections(df_in, charge, width, height):

    df = df_in[df_in['PersonNm'].groupby(df_in['PersonNm']).transform('size')>1]

    source = []
    target =[]
    weight = []
    
    #for index, row in all_people_df.head(50).iterrows():
    for index, row in df.iterrows():
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

    # TODO: this should be a seperate def
    # list of unique people, org names/nodes
    orgs = df['NAME'].unique()
    ppl = df['PersonNm'].unique()

    for org in orgs:
        org_id = org.replace(" ", "_")

        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[org_id]['color']="#92b4f0" # 'blue' 
        d3.node_properties[org_id]['size']=15
        d3.node_properties[org_id]['fontsize']=14
        d3.node_properties[org_id]['fontcolor']="#150db8" #"blue"
        #d3.node_properties['Penny']['edge_size']=5
        #d3.node_properties['Penny']['edge_color']='#0000ff' # Blue

    for person in ppl:
        person_id = person.replace(" ", "_")
        person_label = person.title()
        #st.write (org)
        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[person_id]['label']=person_label
        d3.node_properties[person_id]['color']='green' #'#2200FF' 
        d3.node_properties[person_id]['size']=10
        d3.node_properties[person_id]['fontcolor']='black'

    d3.show(figsize=[width, height], show_slider=False)
    



def orgs_to_people(df, charge, width, height):
    
    source = []
    target =[]
    weight = []
    
    #for index, row in all_people_df.head(50).iterrows():
    for index, row in df.iterrows():
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

    # TODO: this should be a seperate def
    # list of unique people, org names/nodes
    orgs = df['NAME'].unique()
    ppl = df['PersonNm'].unique()

    for org in orgs:
        org_id = org.replace(" ", "_")

        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[org_id]['color']="#92b4f0" # 'blue' 
        d3.node_properties[org_id]['size']=15
        d3.node_properties[org_id]['fontsize']=14
        d3.node_properties[org_id]['fontcolor']="#150db8" #"blue"
        #d3.node_properties['Penny']['edge_size']=5
        #d3.node_properties['Penny']['edge_color']='#0000ff' # Blue

    for person in ppl:
        person_id = person.replace(" ", "_")
        person_label = person.title()
        #st.write (org)
        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[person_id]['label']=person_label
        d3.node_properties[person_id]['color']='green' #'#2200FF' 
        d3.node_properties[person_id]['size']=10
        d3.node_properties[person_id]['fontcolor']='black'

    d3.show(figsize=[width, height], show_slider=False)
    

def orgs_to_emphasis(df, charge, width, height):
    
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
    #d3.show()

    # TODO: this should be a seperate def
    # list of unique people, org names/nodes
    ntee_cats = df[filt]['ntee_cat'].unique()
    orgs = df[filt]['NAME'].unique()

    for ntee in ntee_cats:
        ntee_id =ntee.replace(" ", "_")

        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[ntee_id]['color']="#c9801a" # orangish 
        d3.node_properties[ntee_id]['size']=15
        d3.node_properties[ntee_id]['fontsize']=14
        d3.node_properties[ntee_id]['fontcolor']="#784908" 
        #d3.node_properties['Penny']['edge_size']=5
        #d3.node_properties['Penny']['edge_color']='#0000ff' # Blue

    for org in orgs:
        org_id = org.replace(" ", "_")
        org_label = org.title()
        #st.write (org)
        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[org_id]['label']=org_label
        d3.node_properties[org_id]['color']='green' #'#2200FF' 
        d3.node_properties[org_id]['size']=10
        d3.node_properties[org_id]['fontcolor']='black'

    d3.show(figsize=[width, height], show_slider=False)


def people_to_emphasis(df, charge, width, height):
    
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
    # Note: this must automatically replace spaces with underscore?
    adjmat = vec2adjmat(source, target, weight=weight)

    # Initialize
    d3 = d3graph()

    # Build force-directed graph with default settings
    d3.graph(adjmat)

    ntee_cats = df[filt]['ntee_cat'].unique()
    ppl = df[filt]['PersonNm'].unique()

    for person in ppl:
        person_id = person.replace(" ", "_")
        person_label = person.title()
        #st.write (org)
        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[person_id]['label']=person_label
        d3.node_properties[person_id]['color']='green' #'#2200FF' 
        d3.node_properties[person_id]['size']=10
        d3.node_properties[person_id]['fontcolor']='black'

    for ntee in ntee_cats:
        ntee_id =ntee.replace(" ", "_")

        # Customize the properties of one specific node
        #d3.node_properties['org']['label']='Penny Hofstadter'
       
        # set these       
        d3.node_properties[ntee_id]['color']="#c9801a" # orangish 
        d3.node_properties[ntee_id]['size']=15
        d3.node_properties[ntee_id]['fontsize']=14
        d3.node_properties[ntee_id]['fontcolor']="#784908" 
        #d3.node_properties['Penny']['edge_size']=5
        #d3.node_properties['Penny']['edge_color']='#0000ff' # Blue


    #d3.show(filepath='data/g1.html')
    #d3.show(filepath='ppl_emph.html')
    # d3.show(figsize=[1500, 800], title= 'PPl_Emphs', filepath='d3graph.html')
    
    # add title to edges, too cluttered, tho
    #for index, row in df[filt].iterrows():
    #    person_id = row['PersonNm'].replace(" ", "_")
    #    ntee_id =row['ntee_cat'].replace(" ", "_")
    #    d3.edge_properties[(person_id, ntee_id)]['label']=row['TitleTxt']   

    
    d3.show(figsize=[width, height])
    # d3.show(filepath='data/bigbang.html', notebook=False)

    
    # st.table(d3.edge_properties)

def main():
    st.set_page_config(APP_TITLE, layout="wide")
    #st.title(APP_TITLE)
    #st.caption(APP_SUB_TITLE)


    # load people data
    all_people_df = get_people_df()

    height=800
    width=1100


    # select graph in sidebar
    with st.sidebar:
        msg = """
        ## Visualize Affiliations 

        Directors, Officers, and IRS Contact people connected to Organizations, as listed on IRS documents.

        - People are green
        - Orgs are blue
        -Organization Emphasis Areas are orange-ish

        
        Minimize/Expand sidebar:
        - Mouse over sidebar
        - Use  **<** and **>**  in upper right of sidebar

        Double-click on node to focus on selected node and connections only.
        

        Zoom using "Pinch" or scroll wheel.

        """

        st.markdown(msg)

        with st.expander("Chart Options"):

            charge = st.slider("charge", 100, 300, value=200, 
                            help="Edge length of the network.  Lower number is denser network.")

            col1, col2 = st.columns(2)

            with col1:
                #st.number_input(label, min_value=None, max_value=None, value="min", 
                #                step=None, format=None, key=None, help=None, on_change=None, 
                #                args=None, kwargs=None, *, placeholder=None, 
                #                disabled=False, label_visibility="visible")

                width = st.number_input("Width", min_value=300, max_value=1300, value=width,
                                step=50, help="Width of Graph")
            with col2:
 
                height = st.number_input("Height", min_value=300, max_value=1300, value=height,
                step=50, help="Height of Graph")


            msg_chart = f"""Debug |
            Charge: {charge}
            Width:  {width}
            Height: {height}
    
            """

            st.write (msg_chart)


        options = ["", 
                   "Orgs to People", 
                   "Orgs to Emphasis Area", 
                   "People to Emphasis Area",
                   "People with Multiple Connections", 
                   "Testing"]

        which_graph = st.selectbox("Pick Graph", options, index=0, key="select_graph",  
                    on_change=None)

        #st.write(which_graph)
        #st.write(charge)

        #st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, 
        #             on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", 
        #             disabled=False, label_visibility="visible")



    if which_graph == 'Orgs to People':            
        orgs_to_people(all_people_df, charge, width, height)
        
    elif which_graph == 'Orgs to Emphasis Area':
        orgs_to_emphasis(all_people_df, charge, width, height)
    
    elif which_graph == 'People to Emphasis Area':
        people_to_emphasis(all_people_df, charge, width, height)

    elif which_graph == 'People with Multiple Connections':
        people_with_multiple_connections(all_people_df, charge, width, height)

    elif which_graph == 'Testing':
        orgs_blue(all_people_df, charge, width, height)


    # using example
    # https://github.com/snehankekre/streamlit-d3graph/blob/main/examples/example.py



if __name__ == "__main__":
    main()
