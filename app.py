import streamlit as st
from components.ui_components import render_header, render_file_uploader
from components.download_manager import render_download_section
from utils.excel_processor import process_excel_file

def main():
    # Configuración de página
    st.set_page_config(
        page_title="Excel to CSV Converter",
        page_icon="📊",
        layout="centered"
    )
    
    # Header
    render_header()
    
    # Upload section
    archivo_subido, separador = render_file_uploader()
    
    if archivo_subido:
        if st.button("🚀 Procesar Excel"):
            with st.spinner("Procesando archivo..."):
                archivos_csv = process_excel_file(archivo_subido, separador)
                
                if archivos_csv:
                    st.session_state.archivos_csv = archivos_csv
                    st.success(f"✅ Se procesaron {len(archivos_csv)} hojas")
    
    # Download section
    if 'archivos_csv' in st.session_state:
        render_download_section(st.session_state.archivos_csv)

if __name__ == "__main__":
    main()