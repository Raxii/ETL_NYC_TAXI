# Arquitectura y flujo de datos

```text
NYC TLC Parquet + Apache Parquet Testing
                 |
                 v
              RAW
    originales sin modificación
                 |
                 v
             BRONZE
 lectura, diagnóstico, homologación
                 |
          +------+------+
          |             |
          v             v
     QUARANTINE       AUDIT
 archivos no         inventario,
 recuperables        errores y métricas
          |
          v
             SILVER
 datos normalizados y validados
          |
          +-------------------+
          |                   |
          v                   v
 gold_trips_clean      quality_rejected_records
          |
          +--------------------------+
          |                          |
          v                          v
 gold_daily_revenue       gold_location_performance
          |
          v
      PostgreSQL
```

## Responsabilidades por etapa

- Santi: RAW, extracción, inventario, PostgreSQL y carga.
- Byron: diagnóstico, homologación, BRONZE y cuarentena de archivos.
- Matius: transformaciones, SILVER, reglas de calidad y rechazados.
- Los tres: construcción/revisión de Gold, pruebas e integración.

## Consideraciones

1. RAW no se modifica.
2. Un error de lectura de un archivo no debe detener el lote completo.
3. Un archivo no recuperable se registra en cuarentena con evidencia.
4. Los registros rechazados deben conservar la regla y razón del rechazo.
5. Las métricas se calculan por servicio, año y mes.
6. PostgreSQL es el destino consultable; Spark sigue siendo el motor principal del ETL.
