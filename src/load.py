"""Fase 7: carga idempotente a PostgreSQL. Responsable: Santi."""


def write_spark_df_jdbc(df, table_name: str, config: dict, mode: str = "append"):
    """Escribir DataFrame Spark mediante JDBC.

    Antes de usar append, implementar una estrategia idempotente (por ejemplo,
    reemplazo transaccional de particiones o upsert por clave de negocio).
    No asumir que append por sí solo es idempotente.
    """
    raise NotImplementedError("Santi: implementar carga JDBC segura e idempotente.")


def load_required_tables(table_map: dict, config: dict):
    """Cargar las seis tablas finales y registrar el resultado de cada carga."""
    raise NotImplementedError("Santi: implementar carga coordinada de tablas.")
