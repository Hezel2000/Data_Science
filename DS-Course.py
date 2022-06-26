#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

def start():
    dfSearchAll = pd.read_csv('https://raw.githubusercontent.com/Hezel2000/Data_Science/main/course_material.csv')
    
    gd = GridOptionsBuilder.from_dataframe(dfSearchAll)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=True,groupable=True)
    
    sel_mode = st.radio('sel', ['single', 'multiple'])
    gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
    gridoptions = gd.build()
    
    grid_table = AgGrid(dfSearchAll, gridOptions=gridoptions, update_mode = GridUpdateMode.SELECTION_CHANGED)
    
    sel_row = grid_table['selected_rows']
    
    st.write(sel_row[0]['Vimeo'])

    st.video(sel_row[0]['Vimeo'])



def kapitel_1():
    st.header('Kapitel 1')


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