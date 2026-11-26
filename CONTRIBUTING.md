# Contribuir al proyecto

## Ramas

- `main`: versión integrada y estable.
- `feature/santi-extraccion`
- `feature/byron-esquemas`
- `feature/matius-calidad`

## Reglas

1. No hacer commits directamente en `main`.
2. Actualizar la rama propia con los últimos cambios de `main`.
3. No modificar módulos de otro responsable sin coordinarlo.
4. Antes de un Pull Request, ejecutar las pruebas disponibles.
5. Describir qué se cambió, cómo se probó y qué queda pendiente.
6. No subir datos Parquet, credenciales, `.env` ni resultados pesados.
7. No cambiar nombres de columnas o contratos de datos sin avisar a los otros dos.

## Convención de commits

- `feat:` nueva funcionalidad.
- `fix:` corrección.
- `docs:` documentación.
- `test:` pruebas.
- `refactor:` reorganización sin cambiar el resultado.
- `chore:` configuración y mantenimiento.

Ejemplos:

- `feat: agrega lectura segura de archivos Parquet`
- `fix: corrige homologacion de pickup_datetime`
- `docs: documenta reglas de cuarentena`

## Revisión de Pull Request

El Pull Request debe indicar:
- Responsable.
- Fase del proyecto.
- Archivos modificados.
- Pruebas ejecutadas.
- Resultado de las pruebas.
- Riesgos o decisiones pendientes.

Al menos otro integrante debe revisar antes del merge.
