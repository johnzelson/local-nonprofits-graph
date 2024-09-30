import streamlit as st
from streamlit_d3graph import d3graph
import pandas as pd
from d3graph import d3graph, vec2adjmat


def get_people_df():

    all_people_df = pd.read_csv('data/all_people.csv')
    return all_people_df


@st.cache_data
def init_graph():
    # Initialize
    d3 = d3graph()
    # Load karate example
    #adjmat, df = d3.import_example("karate")

    df = get_people_df()
    source= []
    target = []
    weight = []

    for index, row in df.iterrows():
        source.append(row['NAME'])
        target.append(row['PersonNm'])
        weight.append(1)
        
    # Create adjacency matrix
    adjmat = vec2adjmat(source, target, weight=weight)


    label = df["NAME"].values
    # node_size = df["PersonNm"].values
    node_size = 1

    return d3, adjmat, df, label, node_size


@st.cache_data
def graph_one(_d3, adjmat, df, label, node_size):
    d3.graph(adjmat)
    #d3.set_node_properties(color=df["label"].values)
    return d3


@st.cache_data
def graph_two(_d3, adjmat, df, label, node_size):
    d3.set_node_properties(label=label, color=label, cmap="Set1")
    return d3


@st.cache_data
def graph_three(_d3, adjmat, df, label, node_size):
    d3.set_node_properties(color=label, size=node_size)
    return d3


@st.cache_data
def graph_four(_d3, adjmat, df, label, node_size):
    d3.set_edge_properties(edge_distance=100)
    d3.set_node_properties(color=node_size, size=node_size)
    return d3


@st.cache_data
def graph_five(adjmat, df, label, node_size):
    d3 = d3graph(charge=1000)
    d3.graph(adjmat)
    d3.set_node_properties(color=node_size, size=node_size)
    return d3


@st.cache_data
def graph_six(adjmat, df, label, node_size):
    d3 = d3graph(collision=1, charge=250)
    d3.graph(adjmat)
    d3.set_node_properties(
        color=label, size=node_size, edge_size=node_size, cmap="Set1"
    )
    return d3


@st.cache_data
def graph_seven(adjmat, df, label, node_size):
    d3 = d3graph(collision=1, charge=250)
    d3.graph(adjmat)
    d3.set_node_properties(
        color=label,
        size=node_size,
        edge_size=node_size,
        edge_color="#00FFFF",
        cmap="Set1",
    )
    return d3


d3, adjmat, df, label, node_size = init_graph()

d3 = graph_one(d3, adjmat, df, label, node_size)
d3.show()

"""
d3 = graph_two(d3, adjmat, df, label, node_size)
d3.show()

d3 = graph_three(d3, adjmat, df, label, node_size)
d3.show()

d3 = graph_four(d3, adjmat, df, label, node_size)
d3.show()

d3 = graph_five(adjmat, df, label, node_size)
d3.show()

d3 = graph_six(adjmat, df, label, node_size)
d3.show()

d3 = graph_seven(adjmat, df, label, node_size)
d3.show()

"""
