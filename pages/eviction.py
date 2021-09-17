import glob
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from static.us_state_to_abbrev import us_state_to_abbrev

# https://www.census.gov/data-tools/demo/hhp/#/?measures=EVICTFOR&periodSelector=36

@st.cache
def read_data():
    path = r'static/'
    filenames = glob.glob(path + "/export*.csv")
    dfs = []
    for file in filenames:
        dfs.append( pd.read_csv(file) )
    return pd.concat(dfs, ignore_index=True)

def app():
    st.markdown("## Eviction Data")
    df = read_data()
    st.dataframe(df.sort_values(['Week']))
    
    st.markdown("## Eviction Data Scatter Plot Week 36")
    dt = df.loc[df['Week'].isin(['36'])]
    dtscat = dt.loc[~dt['Area'].str.contains("United")]
    fig = px.scatter(dtscat, x="Percent", y="Number", size="Total Population age 18+", color="Area",
            hover_name="Area", log_x=True, size_max=60)
    st.plotly_chart(fig)
    
    dtleth = df.loc[df['Week'].isin(['36'])]
    dtleth = dtleth.loc[~dtleth['Area'].str.contains("Area")]
    dtleth = dtleth.loc[~dtleth['Area'].str.contains("United")]

    code = []
    for i in dtleth["Area"]:
        code.append(us_state_to_abbrev[i])

    dtleth['code'] = code
    fig = px.choropleth(locations=dtleth["code"], locationmode="USA-states", color=dtleth["Number"], scope="usa")
    st.plotly_chart(fig)

    options = st.sidebar.multiselect("Select Area", df['Area'].drop_duplicates())
    if options:
        st.markdown("Eviction by Area.")
        chart_type = st.sidebar.radio("Chart Type", ("Area", "Line", "Bar"))
        dt = df.loc[df['Area'].isin(options)].sort_values(by="Week")

        if chart_type == "Line":
            fig = px.line(dt, x="Week", y="Number", color='Area', markers=True)
            st.plotly_chart(fig)
        elif chart_type == "Bar":
            fig = px.bar(dt, x="Week", y="Number", color='Area')
            st.plotly_chart(fig)
        else:
            fig = px.area(dt, x="Week", y="Number", color='Area', markers=True)
            st.plotly_chart(fig)

            