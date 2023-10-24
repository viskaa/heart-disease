import streamlit as st
import pandas as pd

def intro():
    import streamlit as st

    st.write("# Welcome To My Machine Learning Dashboard! 👋")
    st.sidebar.success("Select a heart disease above.")

    st.markdown(
        """
        This dashboard created by : Fiska

        This app predicts the **Heart Disease**
    
        Data obtained from the [Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) by UCIML. 
    """
    )

def mapping_demo():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        The dashboard will provide information about heart disease.
        """
    )

    @st.cache_data
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)
   
def iris_species():
    import streamlit as st
    import time
    import numpy as np
    
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        The dashboard will provide information about iris species.
        """
    )
    
    df1=pd.read_csv("iris.csv")
    #progress_bar = st.sidebar.progress(0)
    #status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.bar_chart(last_rows)

    for i in range(1, 10):
        new_rows = last_rows[0, :] + np.random.randn(1, 3).cumsum(axis=0)
        #status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        #progress_bar.progress(i)
        last_rows = new_rows
        #time.sleep(0.05)

    #progress_bar.empty()

def heart_disease():
    import streamlit as st
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        The dashboard will provide information about heart disease.
        """
    )
    
    add_selectitem = st.selectbox("Pilih Jenis Kelamin", ("Laki-Laki", "Perempuan"))

    add_selectitem = st.slider("Pilih Usia", 29, 77, (29, 77))

    add_selectitem = st.selectbox("Pilih Tipe Nyeri Dada", ("Angina", "Tidak Stabil", "Tidak Stabil Yang Parah", "Tidak Terkait Dengan Masalah Jantung"))

    add_selectitem = st.selectbox("Apakah Nyeri Dada Disebabkan Karena Olahraga?", ("Ya", "Tidak"))

    add_selectitem = st.selectbox("Tes Thalium", ("Normal", "Defek tetap pada Thalassemia"))

    add_selectitem = st.slider("Jumlah Pembuluh Darah Utama", 0, 3, (0, 3))

    add_selectitem = st.button("Tampilkan Hasil Prediksi")

page_names_to_funcs = {
    "—": intro,
    "Iris Species": iris_species,
    "Heart Disease!": heart_disease,
}

demo_name = st.sidebar.selectbox("Want to open about?", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()