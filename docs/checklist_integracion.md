# Checklist de integración del equipo

## Antes de integrar a main
- [ ] El cambio está en la rama del responsable.
- [ ] No contiene `.env`, contraseñas ni tokens.
- [ ] No contiene archivos Parquet ni datos pesados.
- [ ] El notebook ejecuta sin errores en el entorno Docker común.
- [ ] El módulo tiene pruebas.
- [ ] Se respetan los contratos de `docs/contratos_entre_modulos.md`.
- [ ] El Pull Request explica cambios, pruebas y pendientes.
- [ ] Otro integrante revisó el código.

## Antes de la entrega
- [ ] Selección de archivos aprobada por el docente.
- [ ] Todos los archivos fuente están inventariados.
- [ ] Archivos problemáticos tienen evidencia de cuarentena.
- [ ] Esquema canónico documentado.
- [ ] Registros válidos y rechazados separados.
- [ ] Seis tablas obligatorias cargadas en PostgreSQL.
- [ ] Tres consultas SQL ejecutadas y guardadas como evidencia.
- [ ] Al menos cinco optimizaciones Spark justificadas.
- [ ] `process_id` único por ejecución.
- [ ] Idempotencia demostrada con dos ejecuciones.
- [ ] README e informe técnico completos.
