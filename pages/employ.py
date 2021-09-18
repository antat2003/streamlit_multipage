import glob
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from openpyxl import load_workbook
import re
from static.us_state_to_abbrev import us_state_to_abbrev

# https://www.census.gov/data-tools/demo/hhp/#/?measures=EVICTFOR&periodSelector=36

@st.cache
def read_data():
    path = r'static'
    filenames = glob.glob(path + "/employ1_week*.xlsx")
    dfs = []    
    for filename in filenames:
        week_number = re.search(r'week\d*', filename)[0]
        wb = load_workbook(filename = filename)
        sheet_names = ['US']
        for state, core in us_state_to_abbrev.items():
            sheet_names.append(core)
        for sheet in sheet_names:
            try:
                sheet_ranges = wb[sheet]
                columns = ['A','B','C','D','E']
                rows = [8,10,11,12,13,14,16,17,37,38,39,40,41,43,44,45,46,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73]    
                for r in rows:
                    dfc = [week_number,sheet]
                    for c in columns:
                        data = sheet_ranges['{}{}'.format(c,r)].value
                        if isinstance(data, str):
                            data = re.sub(r"^\s+","",data)
                        if data is None:
                            data = 0
                        if data == "-":
                            data = 0
                        dfc.append(data)        
                    dfs.append(dfc)
            except: 
                print("Can't read sheetname: {}".format(sheet))
    return dfs

def app():
    
    
    data =read_data()
    df = pd.DataFrame(np.array(data), columns=['Week','Code','Category','Total','Yes','No','Did not report'])
    df['Yes'] = df['Yes'].astype(int)
    df['Total'] = df['Total'].astype(int)
    df['No'] = df['No'].astype(int)
    options = df['Week'].drop_duplicates().sort_values(ascending=False)
    st.write("## Employment Data for the US")

    st.write("Experienced loss of employment income in the last 4 weeks (for self or household member)")    
    US_loss_empl = df.loc[(df['Code'] == 'US') & (df['Category']=="Total")].sort_values(by="Week")
    
    fig = px.line(US_loss_empl, x="Week", y="Yes", color='Code', markers=True)
    st.plotly_chart(fig)

    week_number = st.sidebar.selectbox("Select week number", options)
    if week_number:
        
        st.dataframe(df.loc[df['Week'].isin([week_number])])    
    