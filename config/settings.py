"""Configuraciones de la aplicación"""

# Configuración de CSV
DEFAULT_SEPARATOR = ';'
AVAILABLE_SEPARATORS = [';', ',']
ENCODING = 'utf-8-sig'

# Configuración de archivos
ALLOWED_EXTENSIONS = ['xlsx', 'xls', 'xlsm']
MAX_FILE_SIZE_MB = 10

# Configuración de fechas
DATE_FORMAT = '%d/%m/%Y'

# Mensajes
MESSAGES = {
    'success_processing': "✅ Se procesaron {count} hojas",
    'error_processing': "❌ Error procesando Excel: {error}",
    'empty_file': "⚠️ El archivo está vacío o no tiene hojas válidas"
}