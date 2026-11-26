"""Utilidades compartidas del proyecto."""
from __future__ import annotations

import os
import uuid
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


def load_config(path: str | Path = "config/etl_config.yaml") -> dict[str, Any]:
    """Carga la configuración YAML del proyecto."""
    load_dotenv()
    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    if not isinstance(config, dict):
        raise ValueError("La configuración YAML debe contener un objeto/diccionario.")
    return config


def new_process_id() -> str:
    """Genera un identificador único para cada ejecución."""
    return str(uuid.uuid4())


def postgres_env(config: dict[str, Any]) -> dict[str, str]:
    """Obtiene credenciales PostgreSQL desde variables de entorno, no desde Git."""
    pg = config["postgres"]
    result = {
        "host": pg.get("host", "postgres"),
        "port": str(pg.get("port", 5432)),
        "database": os.environ[pg["database_env"]],
        "user": os.environ[pg["username_env"]],
        "password": os.environ[pg["password_env"]],
    }
    return result


def create_spark_session(config: dict[str, Any]):
    """Crea Spark local para el desarrollo en Docker.

    La dependencia JDBC de PostgreSQL se resuelve desde Maven mediante
    spark.jars.packages; el contenedor necesita acceso a Internet la primera vez.
    """
    from pyspark.sql import SparkSession

    spark_cfg = config["spark"]
    builder = (
        SparkSession.builder
        .appName(spark_cfg.get("app_name", "ETL_NYC_TAXI"))
        .master(spark_cfg.get("master", "local[*]"))
        .config("spark.sql.shuffle.partitions", str(spark_cfg.get("shuffle_partitions", 8)))
        .config("spark.sql.adaptive.enabled", str(spark_cfg.get("adaptive_enabled", True)).lower())
        .config("spark.sql.session.timeZone", spark_cfg.get("session_timezone", "UTC"))
        .config("spark.jars.packages", spark_cfg["postgres_jdbc_package"])
    )
    return builder.getOrCreate()
