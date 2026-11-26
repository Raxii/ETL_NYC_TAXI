"""Orquestación del pipeline. Integración de los tres responsables."""


def run_pipeline(config_path: str = "config/etl_config.yaml"):
    """Ejecutar fases en orden y propagar process_id.

    Orden:
    1. extracción/inventario (Santi)
    2. diagnóstico/reconstrucción/cuarentena de archivos (Byron)
    3. transformación/calidad/Silver (Matius)
    4. agregaciones Gold (los tres)
    5. carga PostgreSQL (Santi)
    6. auditoría final y métricas

    No implementar la orquestación hasta que los contratos de cada módulo estén
    acordados y las pruebas unitarias de cada responsable pasen.
    """
    raise NotImplementedError("Equipo: integrar las fases y ejecutar end-to-end.")
