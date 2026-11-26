# Plan de trabajo del equipo

## Equipo

- Santi
- Byron
- Matius

## Responsables

| Integrante | Responsabilidad principal | Entregables |
|---|---|---|
| Santi | Docker, extracción, inventario, PostgreSQL y carga | Docker, `extract.py`, `load.py`, inventario, `gold_daily_revenue` |
| Byron | Diagnóstico, esquema canónico y recuperación | `schema_recovery.py`, metadatos, cuarentena de archivos, `gold_location_performance` |
| Matius | Transformación y calidad | `transformations.py`, `quality_rules.py`, rechazados, métricas, `gold_trips_clean` |

## Responsabilidad compartida

- Selección final de datos aprobada por el docente.
- Contratos de datos.
- Revisión cruzada de Pull Requests.
- Pruebas de integración.
- Idempotencia.
- Cinco técnicas de optimización Spark como mínimo.
- Consultas SQL.
- README e informe técnico.
- Preparación de exposición y defensa.

## Dependencias

1. Santi debe entregar archivos RAW e inventario.
2. Byron necesita RAW para caracterizar esquemas y producir BRONZE.
3. Matius necesita BRONZE y reglas aprobadas para producir SILVER.
4. Los tres generan/verifican las salidas GOLD.
5. Santi coordina la carga de las seis tablas a PostgreSQL.
6. Los tres ejecutan consultas y pruebas finales.

## Revisión de avances

Cada responsable sube cambios a su rama y abre Pull Request. Otro integrante revisa antes de integrar a `main`.

No se considera terminada una tarea solo porque el código exista: debe incluir una prueba reproducible y evidencia del resultado.
