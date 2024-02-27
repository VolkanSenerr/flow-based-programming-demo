from barfi import st_barfi, barfi_schemas
import streamlit as st

from blocks import loader, selector

base_blocks = [loader, selector]


barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=True)

barfi_result = st_barfi(base_blocks=base_blocks, compute_engine=compute_engine, load_schema=barfi_schema_name)

if barfi_result:
    st.write(barfi_result['CSV Loader']['block'].get_interface(name='CSV Dosya Yükle'))
    st.write(barfi_result['Select CSV']['block'].get_interface(name='CSV Dosya Seç'))
