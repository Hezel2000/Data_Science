#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

# =============================================================================
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
# =============================================================================


#---------------------------------#
#------ Einführung --------------#
#---------------------------------#
    
def einfuehrung():
    st.subheader('Willkommen zur Einfürhung in Data Sciences')
    st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')
    
    st.video('https://youtu.be/amJkqAgkris')

#---------------------------------#
#------ Vorlesungen & Übungen ----#
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
    
# =============================================================================
#         else:
#             st.subheader('Wähle eine Einheit aus obiger Liste')
# =============================================================================
            

    dfSearchAll = importCourseDatasheet()

    useCourse(dfSearchAll)
    


#---------------------------------#
#------ Überblick ----------------#
#---------------------------------#

def ueberblick():
    import streamlit as st
    
    st.header('Überblick')
        
    st.write('''**Wie zu schauen ist – oder zumindest: wie geschaut werden kann**\n
Anhalten, nachvollziehen, eventuell zurückspulen und dazu eigen Skizzen oder Mitschriebe anfertigen\n
Einige wenige Videos haben aus rechtlichen Gründen ein Passwort, das erhaltet Ihr von mir''')

    st.write('''
**Die Veranstaltung besteht aus**\n
>ca. 100 Seiten Skript, aufgeteilt in die 3 Teilskripte
>ca. 50 Videos  mit insgesamt über 7 Stunden Material
>über 100 Jupyter Notebooks  mit >100 Fragen, Aufgaben & Beispielen
> 00 Selbstlern-Fragen mit Antworten
>20 Aufgaben zur gemeinsamen Lösung in den Präsenzphasen und den Semester-Projekten
>zahlreiche zusätzlicher Dateien für verschiedene Aufgaben''')

    # =============================================================================
    # **Einordnung der Einheiten für die Abschlussprüfung:**
    # Ich ergänze die Überschriften um die beiden Symbole ◉ (Relevanz) und ▲ (Verständnis). Die Symbole haben eine von 3 Farben,
    # welche anzeigen, wie relevant oder wichtig für das Verständnis ein Thema ist. Die Farben sind: orange: hoch, grün: mittel,
    # blau: weniger.
    # =============================================================================



#---------------------------------#
#------ Inhaltsverzeichnis -------#
#---------------------------------#

def inhaltsverzeichnis():
    st.header('Inhaltsverzeichnis')
    
    st.write('*coming soon ...*')
    
    
    
#---------------------------------#
#------ Test  --------------------#
#---------------------------------#  
def test():
    import numpy as np
    from bokeh.layouts import column, row
    from bokeh.models import CustomJS, Slider, Select
    from bokeh.plotting import ColumnDataSource, figure
    
    st.header('Testing')
    
    x = np.linspace(0, 10, 500)
    y = np.sin(x)
    
    source = ColumnDataSource(data=dict(x=x, y=y))
    
    plot = figure(y_range=(-10, 10), width=400, height=400)
    
    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
    plot.xaxis.axis_label='x-axis'
    plot.xaxis.axis_label_text_font_size = '20px'
    
    amp_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
    freq_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Frequency")
    phase_slider = Slider(start=0, end=6.4, value=0, step=.1, title="Phase")
    offset_slider = Slider(start=-5, end=5, value=0, step=.1, title="Offset")
    
    callback = CustomJS(args=dict(source=source, amp=amp_slider, freq=freq_slider, phase=phase_slider, offset=offset_slider),
                        code="""
        const data = source.data;
        const A = amp.value;
        const k = freq.value;
        const phi = phase.value;
        const B = offset.value;
        const x = data['x']
        const y = data['y']
        for (let i = 0; i < x.length; i++) {
            y[i] = B + A*Math.sin(k*x[i]+phi);
        }
        source.change.emit();
    """)
    
    amp_slider.js_on_change('value', callback)
    freq_slider.js_on_change('value', callback)
    phase_slider.js_on_change('value', callback)
    offset_slider.js_on_change('value', callback)
    
    select = Select(title="x-axis", value="Yellow", options=["Red", "Yellow", "Blue", "Green"])
    #select.js_link('value', plot.xaxis, 'axis_label')
    
    layout = row(
        column(amp_slider, freq_slider, phase_slider, offset_slider, select),
        plot
    )
    
    st.bokeh_chart(layout)
    st.subheader('Inhaltsverzeichnis')


    
#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

page_names_to_funcs = {
    'Einführung': einfuehrung,
    'Vorlesungen & Übungen': Vorlesungen_Uebungen,
    'Überblick': ueberblick,
    'Inhaltsverzeichnis': inhaltsverzeichnis,
    'test': test
}

demo_name = st.sidebar.selectbox("Viele Wege führen zum Erfolg", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()