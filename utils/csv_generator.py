"""Generación de archivos CSV"""
import pandas as pd
import io
from config.settings import ENCODING

def dataframe_to_csv(df: pd.DataFrame, separador: str) -> str:
    """Convierte DataFrame a string CSV"""
    csv_buffer = io.StringIO()
    
    df.to_csv(
        csv_buffer,
        index=False,
        encoding=ENCODING,
        sep=separador,
        quotechar='"',
        quoting=0,
        lineterminator='\n',
        na_rep='',
        float_format='%.10g'
    )
    
    return csv_buffer.getvalue()

def create_zip_file(archivos_csv: dict) -> bytes:
    """Crea archivo ZIP con todos los CSV"""
    import zipfile
    
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for nombre_archivo, contenido_csv in archivos_csv.items():
            zip_file.writestr(nombre_archivo, contenido_csv.encode(ENCODING))
    
    return zip_buffer.getvalue()