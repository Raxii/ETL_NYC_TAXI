"""Fase 4 y salida Silver/Gold de viajes. Responsable: Matius."""


def add_ingestion_metadata(df, service_type: str, source_file: str, process_id: str):
    """Agregar servicio, archivo fuente, timestamp de ingesta y process_id de trabajo."""
    raise NotImplementedError("Matius: implementar metadatos de ingesta.")


def calculate_derived_fields(df):
    """Calcular duración, velocidad, tarifa por milla, propina e indicadores."""
    raise NotImplementedError("Matius: implementar métricas derivadas.")


def generate_trip_id(df):
    """Crear identificador determinístico y reproducible por viaje.

    Documentar columnas usadas y estrategia para evitar colisiones.
    """
    raise NotImplementedError("Matius: implementar trip_id determinístico.")


def remove_technical_duplicates(df):
    """Detectar duplicados técnicos y conservar evidencia de los descartados."""
    raise NotImplementedError("Matius: implementar deduplicación trazable.")


def build_gold_trips_clean(valid_df):
    """Proyectar las columnas requeridas por gold_trips_clean."""
    raise NotImplementedError("Matius: implementar tabla granular Gold.")
