# Contratos de integración entre módulos

Este documento evita que cada integrante utilice nombres, columnas o rutas diferentes.

## 1. Contrato de extracción — Santi

Entrada:
- `config/etl_config.yaml`
- Archivos mensuales descargados.

Salida:
- Archivos originales en `data/raw/<service_type>/year=YYYY/month=MM/`.
- Inventario técnico con `process_id`, archivo, servicio, partición, tamaño, estado, filas, columnas, hash, error y fecha.

Regla:
- No modificar los archivos RAW.
- Procesar cada archivo con captura de excepciones individual.

## 2. Contrato de diagnóstico — Byron

Entrada:
- Archivos de `data/raw/`.
- Esquemas esperados caracterizados a partir de los archivos reales.
- `metadata/canonical_schema_trips.json`.

Salida:
- DataFrames/archivos reconstruidos en BRONZE.
- Reporte de diferencias de esquema.
- Registros de cuarentena de archivos no recuperables.

Regla:
- No inventar columnas ni tipos. Documentar mapeos y conversiones.
- Mantener una clasificación técnica por archivo.

## 3. Contrato de transformación y calidad — Matius

Entrada:
- Datos reconstruidos de BRONZE.
- Reglas de `metadata/business_rules.json`.

Salida:
- Registros válidos en SILVER.
- Registros rechazados con `process_id`, `trip_id` si existe, servicio, archivo, etapa, regla, columna, valor original, razón técnica, razón de negocio y fecha.
- Métricas por servicio, año y mes.

Regla:
- No confundir registro sospechoso con registro rechazado.
- Mantener evidencia de cada regla aplicada.

## 4. Contrato Gold

- `gold_trips_clean`: Matius; granularidad de un registro por viaje.
- `gold_daily_revenue`: Santi; granularidad servicio-fecha.
- `gold_location_performance`: Byron; granularidad servicio-zona-origen-zona-destino.

Todos deben usar los mismos nombres y tipos acordados en el esquema final.

## 5. Contrato de carga — Santi

Entrada:
- DataFrames/archivos Gold, rechazados, métricas e inventario.

Salida:
- Seis tablas PostgreSQL requeridas por el caso.

Regla:
- La carga debe ser idempotente. No asumir que `append` evita duplicados.
- Documentar clave de negocio y estrategia de reemplazo/upsert.

## 6. Convenciones comunes

- Nombres de columnas: `snake_case`.
- Tipos y nulos: definidos después de inspeccionar los archivos.
- Timestamps: acordar zona horaria y mantener consistencia.
- Identificador: `process_id` único por ejecución.
- Rutas: configuradas en `config/etl_config.yaml`.
- No introducir cambios incompatibles sin Pull Request y revisión del equipo.
