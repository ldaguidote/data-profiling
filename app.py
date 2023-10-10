import streamlit as st
import os
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pandas as pd

import warnings
# import matplotlib
warnings.filterwarnings("ignore")

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar:
    st.image('swiftsight.png')
    # st.title('FA Toolkit')
    st.caption('This portal aims to facilitate the work of functional analysts through '
               'automated data quality profiling and exploratory data analysis')

    choice = st.radio('Navigation', ['Upload Data', 'Data Quality Profile'])

if choice == 'Upload Data':
    st.title('File Upload')
    st.subheader('Choose a file for analysis')
    file = st.file_uploader('Choose a file')

    if file:

        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == 'Data Quality Profile':
    st.title("Data Quality Profile")
    profile_df = df.profile_report()
    st_profile_report(profile_df)

 
