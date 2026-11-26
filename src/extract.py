"""Fase 1: extracción e inventario técnico. Responsable: Santi."""
from pathlib import Path


def inspect_parquet_file(spark, file_path: str | Path, service_type: str, process_id: str):
    """Leer un archivo individual y devolver datos/metadatos de inventario.

    Debe capturar excepciones por archivo para que un fallo no detenga todo el lote.
    Registrar tamaño, ruta, servicio, año/mes, estado, filas, columnas,
    hash del esquema, mensaje de error y fecha de procesamiento.
    """
    raise NotImplementedError("Santi: implementar inspección individual y captura de errores.")


def extract_enabled_datasets(spark, config: dict, process_id: str):
    """Procesar solo datasets enabled=true y conservar RAW sin modificaciones."""
    raise NotImplementedError("Santi: implementar extracción desde archivos locales RAW.")


def build_file_inventory(inventory_rows: list[dict]):
    """Convertir los metadatos recolectados en un DataFrame de Spark."""
    raise NotImplementedError("Santi: implementar DataFrame de inventario.")
