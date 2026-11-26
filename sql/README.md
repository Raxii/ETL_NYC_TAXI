# SQL

`create_tables.sql` crea las seis tablas obligatorias en PostgreSQL.
`validation_queries.sql` contiene las tres consultas de verificación indicadas en el caso.

El DDL es una base inicial. Revisar tipos, claves y restricciones con los esquemas reales antes de la carga final.
Si el volumen PostgreSQL ya fue inicializado, modificar el archivo de inicialización no ejecuta automáticamente los cambios: aplicar los cambios con una migración o ejecutar el SQL de forma controlada.
