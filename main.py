from barfi import st_barfi, barfi_schemas
import streamlit as st

from blocks import loader, selector, minmax, result

base_blocks = [loader, selector, minmax, result]


barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=True)

barfi_result = st_barfi(base_blocks=base_blocks, compute_engine=compute_engine, load_schema=barfi_schema_name)

if barfi_result:
    res = barfi_result['Display Result-1']['block'].get_interface(name='disp_input')[0]
    st.write("Min: " + res)
    res = barfi_result['Display Result-2']['block'].get_interface(name='disp_input')[0]
    st.write("Max:" + res)

