"""Procesamiento de archivos Excel"""
import pandas as pd
import streamlit as st
from typing import Dict, Optional
from config.settings import DATE_FORMAT

def process_excel_file(archivo_excel, separador: str = ';') -> Optional[Dict[str, str]]:
    """Procesa el archivo Excel y retorna diccionario con CSVs"""
    try:
        excel_file = pd.ExcelFile(archivo_excel)
        archivos_csv = {}
        
        for sheet_name in excel_file.sheet_names:
            csv_content = process_sheet(archivo_excel, sheet_name, separador)
            if csv_content:
                archivos_csv[f"{sheet_name}.csv"] = csv_content
        
        return archivos_csv if archivos_csv else None
        
    except Exception as e:
        st.error(f"Error procesando Excel: {e}")
        return None

def process_sheet(archivo_excel, sheet_name: str, separador: str) -> Optional[str]:
    """Procesa una hoja específica del Excel"""
    try:
        df = pd.read_excel(archivo_excel, sheet_name=sheet_name)
        
        # Limpieza de datos
        df = clean_dataframe(df)
        
        # Conversión a CSV
        from utils.csv_generator import dataframe_to_csv
        return dataframe_to_csv(df, separador)
        
    except Exception as e:
        st.warning(f"Error procesando hoja '{sheet_name}': {e}")
        return None

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia el DataFrame eliminando filas/columnas vacías y formateando fechas"""
    # Eliminar columnas y filas completamente vacías
    df = df.dropna(axis=1, how='all')
    df = df.dropna(axis=0, how='all')
    
    # Limpiar nombres de columnas
    df.columns = df.columns.str.strip()
    
    # Manejar fechas
    df = format_dates(df)
    
    # Rellenar NaN
    df = df.fillna('')
    
    return df

def format_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Formatea las columnas de fechas"""
    for col in df.columns:
        if df[col].dtype == 'datetime64[ns]':
            df[col] = df[col].dt.strftime(DATE_FORMAT).fillna('')
        elif 'datetime' in str(df[col].dtype):
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime(DATE_FORMAT).fillna('')
    
    return df