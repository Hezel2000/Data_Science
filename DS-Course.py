#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

#---------------------------------#
#------ Start --------------------#
#---------------------------------#
    
def start():
    st.subheader('Willkommen bei Data Science ')
    st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')


#---------------------------------#
#------ Globale Suche ------------#
#---------------------------------#
def globale_suche():
    import streamlit as st
    st.subheader('Wähle Deine Einheit')

    @st.cache
    def importCourseDatasheet():
        dfSearchAll= pd.read_csv('https://raw.githubusercontent.com/Hezel2000/Data_Science/main/course_material.csv')
        return dfSearchAll

    
    def useCourse(dfSearchAll):
        dfSearchAll = dfSearchAll
        gd = GridOptionsBuilder.from_dataframe(dfSearchAll)
        gd.configure_pagination(enabled=True)
        gd.configure_default_column(editable=True,groupable=True)
        gd.configure_selection(selection_mode='single', use_checkbox=True)
        gridoptions = gd.build()
        grid_table = AgGrid(dfSearchAll, gridOptions=gridoptions, update_mode = GridUpdateMode.SELECTION_CHANGED, theme='material')
        sel_row = grid_table['selected_rows']
    
        if len(sel_row) > 0:    
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.video(sel_row[0]['Youtube'])
            with col2:
                with st.expander('Jupyter Notebooks', expanded=True):
                    st.write("[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Vorlesung ipynb'] + ")")
                    st.write("[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Uebung ipynb'] + ")")
                    st.write("[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Lösung ipynb'] + ")")
                with st.expander('Resources', expanded=True):
                    ('noch extra was')
                with st.expander('Downloads', expanded=True):
                    ('noch was')            
                with st.expander('Keywords', expanded=True):
                    ('noch extra was')
            
            #st.subheader('Beschreibung')
            
            st.write(sel_row[0]['Vorlesung ipynb'])
            
            st.write(sel_row[0]['Beschreibung'])
    
        else:
            st.subheader('Wähle eine Einheit aus obiger Liste')
            
    
    dfSearchAll = importCourseDatasheet()
    st.write(dfSearchAll['Vorlesung ipynb'])
    useCourse(dfSearchAll)
    


def kapitel_1():
    import streamlit as st
    st.header('Kapitel 1')
        
    # Text files
    
    text_contents = '''
    Foo, Bar
    123, 456
    789, 000
    '''
    
    # Different ways to use the API
    
    st.download_button('Download CSV', text_contents, 'text/csv')
    st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'
    
    with open('myfile.csv') as f:
       st.download_button('Download CSV', f)  # Defaults to 'text/plain'
    
    # ---
    # Binary files
    
    binary_contents = b'whatever'
    
    # Different ways to use the API
    
    st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'
    
    with open('myfile.zip', 'rb') as f:
       st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'
    
    # You can also grab the return value of the button,
    # just like with any other button.
    
    if st.download_button(...):
       st.write('Thanks for downloading!')


def kapitel_2():
    st.write('test 2')


def kapitel_3():
    st.write('test 3')



page_names_to_funcs = {
    'Start': start,
    'Globale Suche': globale_suche,
    'Kapitel 1': kapitel_1,
    'Kapitel 2': kapitel_2,
    'Kapitel 3': kapitel_3,
}

demo_name = st.sidebar.selectbox("Viele Wege führen zum Erfolg", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()