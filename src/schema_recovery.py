"""Fases 2 y 3: diagnóstico, homologación y recuperación. Responsable: Byron."""


def inspect_schema(spark, file_path: str):
    """Obtener el esquema real de un archivo Parquet."""
    raise NotImplementedError("Byron: implementar inspección de esquema.")


def compare_schemas(actual_schema, expected_schema: dict):
    """Identificar columnas faltantes, adicionales y tipos incompatibles."""
    raise NotImplementedError("Byron: implementar comparación de esquemas.")


def normalize_service_columns(df, service_type: str):
    """Homologar nombres de columnas de Yellow, Green o FHVHV."""
    raise NotImplementedError("Byron: implementar matriz de homologación del caso.")


def recover_to_canonical(df, service_type: str, canonical_schema: dict):
    """Agregar columnas ausentes controladas y convertir tipos con manejo de errores."""
    raise NotImplementedError("Byron: implementar reconstrucción al esquema canónico.")


def classify_file_failure(exception: Exception, file_path: str):
    """Clasificar el archivo usando las siete categorías establecidas en el caso."""
    raise NotImplementedError("Byron: implementar clasificación de archivos problemáticos.")


def write_file_quarantine_record(record: dict, quarantine_path: str):
    """Guardar referencia, motivo, excepción, fecha, etapa y acción recomendada."""
    raise NotImplementedError("Byron: implementar cuarentena de archivos.")
