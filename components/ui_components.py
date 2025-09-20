"""Componentes de interfaz de usuario"""
import streamlit as st
from config.settings import DEFAULT_SEPARATOR, AVAILABLE_SEPARATORS
from utils.file_utils import validate_file

def render_header():
    """Renderiza el header de la aplicación"""
    st.title("📊 Separador de Hojas Excel a CSV")
    st.write("Convierte cada hoja de tu archivo Excel en archivos CSV separados")
    st.divider()

def render_file_uploader():
    """Renderiza la sección de upload de archivos"""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        archivo_subido = st.file_uploader(
            "Selecciona tu archivo Excel",
            type=['xlsx', 'xls', 'xlsm'],
            help="Tamaño máximo: 10MB"
        )
    
    with col2:
        separador = st.selectbox(
            "Separador CSV:",
            AVAILABLE_SEPARATORS,
            index=AVAILABLE_SEPARATORS.index(DEFAULT_SEPARATOR),
            help="';' para plantillas europeas, ',' para anglosajonas"
        )
    
    # Validar archivo si se subió
    if archivo_subido:
        is_valid, message = validate_file(archivo_subido)
        if not is_valid:
            st.error(message)
            return None, separador
        else:
            st.success(f"✅ Archivo válido: {archivo_subido.name}")
    
    return archivo_subido, separador

def render_file_info(archivos_csv: dict):
    """Renderiza información de los archivos procesados"""
    st.subheader("📋 Archivos generados:")
    
    for i, nombre in enumerate(archivos_csv.keys(), 1):
        st.write(f"{i}. {nombre}")