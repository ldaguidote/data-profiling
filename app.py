import streamlit as st
import os
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
from utils import *

import warnings

if os.path.exists('./dataset.csv') : 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar:
    st.image('assets/swiftsight.png')
    st.caption('This portal aims to facilitate the work of functional analysts through '
               'automated data quality profiling and exploratory data analysis')

    choice = st.radio('Navigation', ['Upload Data', 'Data Profiling'])

if choice == 'Upload Data':
    st.title('File Upload')
    st.subheader('Choose a file for analysis')
    filetype = st.radio('File Type', ['CSV', 'XLSX'])
    file = st.file_uploader('Choose a file')

    if file:
        if filetype == 'CSV':
            df = pd.read_csv(file, index_col=None)

        elif filetype == 'XLSX':
            df = pd.read_excel(file, index_col=None)

        # df = transform_dates(df)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == 'Data Profiling':
    st.title("Data Profiling Report")
    profile_df = df.profile_report(interactions=None, correlations=None)
    st_profile_report(profile_df)
    profile_df.to_file('report.html')

    with open("report.html", "rb") as file:
        btn = st.download_button(
                    label="Download Report",
                    data=file,
                    file_name="report.html",
                    mime="text/html"
                    )

 
