import streamlit as st
import pandas as pd
from connect_db import insert_data_to_db

st.title("Upload Excel files")

uploaded_files = st.file_uploader("Selecciona los archivos de Excel (clientes y compras)", type=["xls", "xlsx"], accept_multiple_files=True)

if "merged_df" not in st.session_state:
    st.session_state.merged_df = None

if uploaded_files:
    if len(uploaded_files) != 2:
        st.error("Por favor, selecciona exactamente dos archivos.")
    else:
        df1 = pd.read_excel(uploaded_files[0])
        df2 = pd.read_excel(uploaded_files[1])

        
        st.write("Tabla de Clientes:")
        st.dataframe(df1)

        st.write("Tabla de Compras:")
        st.dataframe(df2)

        if st.button("Procesar archivos"):
            
            merged_df = pd.merge(df1, df2, left_on='id_cliente', right_on='id_cliente', how='inner')
            st.session_state.merged_df = merged_df
            st.write("Datos combinados:")
            st.dataframe(merged_df)

if st.session_state.merged_df is not None:
    if st.button("Cargar a base de datos"):
        
        st.write(f"Primeras filas de los datos a insertar:")
        st.dataframe(st.session_state.merged_df.head())

        table_name = "detalles_cliente_compra"

        try:
            insert_data_to_db(st.session_state.merged_df, table_name)
            st.success("Datos cargados exitosamente a la base de datos.")
        except Exception as e:
            st.error(f"Error al cargar los datos a la base de datos: {e}")



