import glob
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

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
    options = st.sidebar.multiselect("Select Area", df['Area'].drop_duplicates())

    if options:
        st.markdown("Eviction by Area chart.")
        
        fig = go.Figure()
        for opt in options:
            dt = df.loc[df['Area'].isin([opt])].set_index('Week').sort_index()
            index = dt.index.values.astype(int)
            x=[]
            for i in index:
                x.append('Week ' + str(i))

            fig.add_trace( go.Scatter(
                x=x,
                y=dt["Number"].values,
                mode='none',
                stackgroup='one',
                name=opt
            ))
        fig.update_traces(mode="markers+lines", hovertemplate=None)
        fig.update_layout(hovermode="x unified")
        st.plotly_chart(fig)
