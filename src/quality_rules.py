"""Fase 5: reglas de calidad, rechazados y métricas. Responsable: Matius."""


def validate_required_fields(df, critical_fields: list[str]):
    """Evaluar nulidad de campos críticos."""
    raise NotImplementedError("Matius: implementar validación de nulos.")


def classify_trip_records(df, rules: dict):
    """Separar registros válidos, rechazados y sospechosos con trazabilidad.

    No confundir 'sospechoso' con 'rechazado': aplicar la decisión acordada
    con el ingeniero y documentada en metadata/business_rules.json.
    """
    raise NotImplementedError("Matius: implementar clasificación de calidad.")


def build_quality_rejected_records(rejected_df, process_id: str):
    """Construir las columnas de quality_rejected_records."""
    raise NotImplementedError("Matius: implementar tabla de rechazados.")


def build_quality_metrics(valid_df, rejected_df, all_df, process_id: str):
    """Calcular métricas por servicio, año y mes."""
    raise NotImplementedError("Matius: implementar resumen de calidad.")
