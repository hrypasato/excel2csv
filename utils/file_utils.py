"""Utilidades para manejo de archivos"""
import os
from config.settings import ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB

def validate_file(file) -> tuple[bool, str]:
    """Valida el archivo subido"""
    if file is None:
        return False, "No se seleccionó archivo"
    
    # Validar extensión
    file_extension = file.name.split('.')[-1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        return False, f"Tipo de archivo no soportado. Use: {', '.join(ALLOWED_EXTENSIONS)}"
    
    # Validar tamaño
    file_size_mb = file.size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        return False, f"Archivo muy grande. Máximo: {MAX_FILE_SIZE_MB}MB"
    
    return True, "Archivo válido"

def clean_filename(filename: str) -> str:
    """Limpia el nombre del archivo para evitar caracteres problemáticos"""
    chars_to_replace = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    clean_name = filename
    
    for char in chars_to_replace:
        clean_name = clean_name.replace(char, '_')
    
    return clean_name