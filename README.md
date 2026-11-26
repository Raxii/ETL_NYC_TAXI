# ETL_NYC_TAXI — Proyecto colaborativo de Ingeniería de Datos

Repositorio de trabajo para el proyecto de Modelado Avanzado de Base de Datos. El equipo está formado por **Santi, Byron y Matius**.

## 1. Objetivo

Construir un pipeline ETL con **Apache Spark / PySpark** que lea archivos Parquet de NYC Taxi & Limousine Commission, diagnostique diferencias de esquemas y archivos problemáticos, unifique los datos, aplique reglas de calidad, genere capas analíticas y cargue los resultados en **PostgreSQL**.

La arquitectura contempla las capas:

- `raw`: archivos originales, sin modificación.
- `bronze`: datos leídos y reconstruidos bajo una estructura común.
- `silver`: datos normalizados, validados y separados entre válidos e inválidos.
- `gold`: tablas analíticas.
- `quarantine`: referencias y evidencias de archivos o registros rechazados.
- `audit`: inventario y métricas de ejecución.

## 2. Tecnologías acordadas

- Docker y Docker Compose.
- Python 3.11.
- Java 17.
- Apache Spark / PySpark 3.5.3.
- JupyterLab.
- PostgreSQL 16.
- pgAdmin o `psql` (opcional, para administrar PostgreSQL).
- Git y GitHub.

**Importante:** tener Jupyter en Docker no demuestra por sí solo que Spark esté operativo. El contenedor `jupyter` de este repositorio instala PySpark y Java.

## 3. Conjunto de datos propuesto

Selección inicial de cinco archivos mensuales completos:

| Servicio | Archivo |
|---|---|
| Yellow | `yellow_tripdata_2023-01.parquet` |
| Yellow | `yellow_tripdata_2023-02.parquet` |
| Green | `green_tripdata_2023-01.parquet` |
| Green | `green_tripdata_2023-02.parquet` |
| FHVHV | `fhvhv_tripdata_2023-01.parquet` |

También se incorporarán archivos de prueba problemáticos del repositorio Apache Parquet Testing.

**Pendiente de aprobación/documentación:** el PDF del caso enumera 11 archivos mínimos, pero el equipo indica que el docente autorizó seleccionar una cantidad menor. Antes de cerrar el conjunto de datos, conservar la confirmación del docente. No se debe afirmar que estos cinco archivos cumplen el mínimo escrito de 11 sin esa autorización.

Fuentes indicadas en el caso:

- NYC TLC Trip Record Data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Apache Parquet Testing: https://github.com/apache/parquet-testing

Descargar archivos completos de cada mes seleccionado; no sustituirlos por CSV ni convertir todo el procesamiento a Pandas.

## 4. Estructura del repositorio

```text
ETL_NYC_TAXI/
├── .github/                 # plantillas y validación básica
├── config/                  # configuración externa YAML
├── data/                    # datos locales; no se suben a GitHub
├── docs/                    # arquitectura, acuerdos y responsabilidades
├── metadata/                # esquemas y reglas
├── notebooks/               # notebooks de las cinco etapas
├── scripts/                 # utilidades de descarga/validación
├── sql/                     # DDL y consultas SQL
├── src/                     # módulos Python
├── tests/                   # pruebas automáticas
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 5. Inicio rápido con Docker

Requisitos: Docker Desktop o Docker Engine con Docker Compose.

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

Editar `.env` y cambiar las contraseñas y el token de Jupyter.

### Linux / macOS

```bash
cp .env.example .env
```

Luego, desde la raíz del repositorio:

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f jupyter
```

Abrir JupyterLab:

- http://localhost:8888

La contraseña/token se define en `.env` mediante `JUPYTER_TOKEN`.

PostgreSQL queda disponible desde el equipo anfitrión en:

- Host: `localhost`
- Puerto: `5432` (o el valor definido en `POSTGRES_PORT`)
- Base de datos: `etl_nyc_taxi` (o `POSTGRES_DB`)
- Usuario: `etl_user` (o `POSTGRES_USER`)
- Contraseña: la definida en `.env`

**Entre contenedores**, el host de PostgreSQL es `postgres`, no `localhost`.

### Comprobar PySpark

En una celda de Jupyter:

```python
import pyspark
from pyspark.sql import SparkSession

print("PySpark:", pyspark.__version__)

spark = (
    SparkSession.builder
    .appName("ETL_NYC_TAXI_Check")
    .master("local[*]")
    .getOrCreate()
)

spark.range(5).show()
```

### Comprobar PostgreSQL

```bash
docker compose exec postgres psql -U etl_user -d etl_nyc_taxi -c "\dt"
```

Si se cambiaron los nombres de usuario o base de datos en `.env`, adaptar el comando.

### Detener servicios

```bash
docker compose down
```

Para borrar también el volumen de PostgreSQL (esto elimina la base de datos persistida):

```bash
docker compose down -v
```

No ejecutar `down -v` si se desea conservar el trabajo almacenado en PostgreSQL.

## 6. GitHub: forma obligatoria de colaborar

Se usará una rama por integrante:

- `main`: versión integrada y estable.
- `feature/santi-extraccion`: Santi.
- `feature/byron-esquemas`: Byron.
- `feature/matius-calidad`: Matius.

Flujo recomendado:

1. Actualizar `main`.
2. Cambiar a la rama propia.
3. Desarrollar y probar localmente.
4. Revisar `git status`.
5. Hacer commit con un mensaje descriptivo.
6. Subir la rama.
7. Crear un Pull Request hacia `main`.
8. Otro integrante revisa el código.
9. Integrar solamente cuando las pruebas pasen.

Ejemplo:

```bash
git checkout main
git pull origin main
git checkout feature/santi-extraccion
git merge main

# trabajar y probar
git add src/extract.py notebooks/01_extraccion.ipynb
git commit -m "feat: implementa extraccion de Parquet"
git push origin feature/santi-extraccion
```

No trabajar directamente sobre `main`. No subir `.env`, contraseñas, archivos Parquet ni resultados pesados.

## 7. Archivos de datos: política del equipo

Los Parquet y los resultados intermedios **no se guardan en GitHub**. Cada integrante debe obtener los mismos archivos en su equipo y mantenerlos en `data/raw/`.

- `data/raw/`: archivos fuente originales.
- `data/bronze/`, `data/silver/`, `data/gold/`: salidas reproducibles.
- `data/quarantine/`: evidencias de archivos/registros rechazados.
- `data/audit/`: resultados de auditoría.

El `.gitignore` excluye el contenido de esas carpetas, pero conserva los directorios mediante `.gitkeep`.

No subir los datos a Git LFS sin acuerdo previo del equipo y del docente.

## 8. Responsabilidades

- **Santi:** Docker, entorno, extracción, inventario, PostgreSQL, carga y `gold_daily_revenue`.
- **Byron:** diagnóstico de esquemas, esquema canónico, archivos problemáticos, cuarentena de archivos y `gold_location_performance`.
- **Matius:** transformaciones, reglas de calidad, registros rechazados, métricas y `gold_trips_clean`.
- **Los tres:** integración, revisión cruzada, pruebas, optimización Spark, consultas SQL, informe y exposición.

Los detalles y criterios de aceptación están en `docs/roles/LEEME_SANTI.txt`, `docs/roles/LEEME_BYRON.txt` y `docs/roles/LEEME_MATIUS.txt`.

## 9. Orden de ejecución del pipeline

1. `01_extraccion.ipynb`: archivos originales e inventario.
2. `02_diagnostico_reconstruccion.ipynb`: comparación y reconstrucción de esquemas; cuarentena de archivos.
3. `03_transformacion_validacion.ipynb`: transformaciones, reglas de calidad y separación de registros.
4. Construcción de tablas Gold: viajes limpios, ingresos diarios y rendimiento por zonas.
5. `04_carga_postgres.ipynb`: carga de las seis tablas obligatorias.
6. `05_reporte_calidad_conclusiones.ipynb`: métricas, resultados y conclusiones.
7. Ejecutar `sql/validation_queries.sql` y pruebas de idempotencia.

## 10. Tablas finales obligatorias

1. `gold_trips_clean`
2. `gold_daily_revenue`
3. `gold_location_performance`
4. `quality_rejected_records`
5. `quality_metrics_summary`
6. `audit_file_inventory`

El DDL inicial está en `sql/create_tables.sql`. Revisarlo y adaptarlo cuando se confirme el esquema físico final. La guía presenta una inconsistencia entre `naudit_file_inventory` en una sección y `audit_file_inventory` en la lista final; este repositorio usa `audit_file_inventory`, que es el nombre de la entrega final.

## 11. Reglas técnicas que no se deben olvidar

- Spark/PySpark es el motor principal; Pandas solo para inspecciones auxiliares pequeñas.
- Mantener `raw` inalterada.
- No ignorar archivos corruptos: registrar excepción, etapa y evidencia.
- No eliminar registros sin registrar la regla y la razón.
- Distinguir archivo corrupto, error de esquema y error de calidad de negocio.
- Generar un `process_id` único por ejecución.
- Diseñar la carga para que una segunda ejecución no duplique resultados.
- Recibir parámetros desde `config/etl_config.yaml`.
- Justificar e implementar al menos cinco técnicas de optimización Spark.
- No guardar secretos en el repositorio.

## 12. Estado del código

Este repositorio es un **andamiaje inicial de trabajo**: contiene estructura, configuración, contratos, DDL, notebooks guía y módulos con puntos de implementación. No representa todavía un ETL terminado. Cada responsable debe implementar, probar y documentar su parte antes de integrarla.
