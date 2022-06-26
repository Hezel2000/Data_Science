#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

def start():
    dfSearchAll = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    AgGrid(dfSearchAll)



def kapitel_1():
    st.write('test 1')


def kapitel_2():
    st.write('test 2')


def kapitel_3():
    st.write('test 3')



page_names_to_funcs = {
    'Start': start,
    'Kapitel 1': kapitel_1,
    'Kapitel 2': kapitel_2,
    'Kapitel 3': kapitel_3,
}

demo_name = st.sidebar.selectbox("Start your flank method analysis journey here", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()