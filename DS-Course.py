#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import numpy as np

#---------------------------------#
#------ Start --------------------#
#---------------------------------#
    
def start():
    st.subheader('Willkommen bei Data Science ')
    st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')
    
    st.write('''
             **Wie zu schauen ist – oder zumindest: wie geschaut werden kann**\n
Anhalten, nachvollziehen, eventuell zurückspulen und dazu eigen Skizzen oder Mitschriebe anfertigen

**Die Veranstaltung besteht aus**\n
ca. 100 Seiten Skript, aufgeteilt in die 3 Teilskripte
ca. 50 Videos  mit >7 Stunden Material
über 100 Jupyter Notebooks  mit >100 Fragen, Aufgaben & Beispielen
>100 Selbstlern-Fragen mit Antworten
>20 Aufgaben zur gemeinsamen Lösung in den Präsenzphasen und den Semester-Projekten
zahlreiche zusätzlicher Dateien für verschiedene Aufgaben

**Manche Videos haben aus rechtlichen Gründen ein Passwort, das lautet:**\n
 Passwort für einige wenige Videos: das erhaltet Ihr von mir

Einordnung der Einheiten für die Abschlussprüfung:
Ich ergänze die Überschriften um die beiden Symbole ◉ (Relevanz) und ▲ (Verständnis). Die Symbole haben eine von 3 Farben, welche anzeigen, wie relevant oder wichtig für das Verständnis ein Thema ist. Die Farben sind: orange: hoch, grün: mittel, blau: weniger. 

             ''')


#---------------------------------#
#------ Globale Suche ------------#
#---------------------------------#
def Vorlesungen_Uebungen():
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
                st.write('Laufzeit: ' + sel_row[0]['Laufzeit'])
                with st.expander('Jupyter Notebooks', expanded=True):
                    if sel_row[0]['Vorlesung ipynb'] != 'none':
                        vorlesung = "[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Vorlesung ipynb'] + ")"
                    else:
                        vorlesung=''
                    if sel_row[0]['Übungen ipynb'] != 'none':
                        uebungen = "[Übungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Übungen ipynb'] + ")"
                    else:
                        uebungen=''
                    if sel_row[0]['Lösungen ipynb'] != 'none':
                        loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Lösungen ipynb'] + ")"
                    else:
                        loesungen=''
                    if vorlesung=='' and uebungen=='' and loesungen=='':
                        st.write('keine vorhanden')
                    else:
                        st.write(vorlesung,uebungen,loesungen)
                with st.expander('Schlagworte', expanded=True):
                    if sel_row[0]['Schlagworte'] != 'none':
                        st.write(sel_row[0]['Schlagworte'])
                    else:
                        st.write('keine vorhannden')
            
            #st.subheader('Beschreibung')
            st.write(sel_row[0]['Beschreibung'])
    
        else:
            st.subheader('Wähle eine Einheit aus obiger Liste')
            

    dfSearchAll = importCourseDatasheet()

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
    'Einführung': start,
    'Vorlesungen & Übungen': Vorlesungen_Uebungen,
    'Kapitel 1': kapitel_1,
    'Kapitel 2': kapitel_2,
    'Kapitel 3': kapitel_3,
}

demo_name = st.sidebar.selectbox("Viele Wege führen zum Erfolg", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()