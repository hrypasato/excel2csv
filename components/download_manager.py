"""Gestión de descargas"""
import streamlit as st
import pandas as pd
import io
from utils.csv_generator import create_zip_file

def render_download_section(archivos_csv: dict):
    """Renderiza la sección de descargas"""
    st.divider()
    st.subheader("📥 Descargar archivos")
    
    # Descarga de ZIP
    render_zip_download(archivos_csv)
    
    st.divider()
    
    # Preview y descarga individual
    render_individual_downloads(archivos_csv)

def render_zip_download(archivos_csv: dict):
    """Renderiza botón de descarga del ZIP"""
    zip_data = create_zip_file(archivos_csv)
    
    st.download_button(
        label="📦 Descargar todos los CSV (ZIP)",
        data=zip_data,
        file_name="hojas_excel_separadas.zip",
        mime="application/zip",
        width="stretch"
    )

def render_individual_downloads(archivos_csv: dict):
    """Renderiza preview y descarga individual"""
    st.subheader("👁️ Vista previa y descarga individual:")
    
    for nombre, contenido in archivos_csv.items():
        with st.expander(f"📄 {nombre}"):
            try:
                # Detectar separador del contenido
                separador = ';' if ';' in contenido.split('\n')[0] else ','
                df_preview = pd.read_csv(io.StringIO(contenido), sep=separador)
                
                # Mostrar info
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Filas", len(df_preview))
                with col2:
                    st.metric("Columnas", len(df_preview.columns))
                
                # Mostrar preview
                st.dataframe(df_preview.head(10), width="stretch")
                
                # Botón de descarga
                st.download_button(
                    label=f"📥 Descargar {nombre}",
                    data=contenido.encode('utf-8-sig'),
                    file_name=nombre,
                    mime="text/csv",
                    key=f"download_{nombre}",
                    width="stretch"
                )
                
            except Exception as e:
                st.error(f"Error mostrando preview: {e}")