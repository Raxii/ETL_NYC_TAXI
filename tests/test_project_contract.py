import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_config_has_five_proposed_monthly_files():
    config = yaml.safe_load((ROOT / "config/etl_config.yaml").read_text(encoding="utf-8"))
    enabled = [item for item in config["datasets"] if item.get("enabled")]
    assert len(enabled) == 5
    assert {item["service_type"] for item in enabled} == {"yellow", "green", "fhvhv"}


def test_canonical_schema_contains_case_minimum_fields():
    schema = json.loads((ROOT / "metadata/canonical_schema_trips.json").read_text(encoding="utf-8"))
    names = {field["name"] for field in schema["fields"]}
    required = {
        "trip_id", "service_type", "pickup_datetime", "dropoff_datetime",
        "trip_distance", "pickup_location_id", "dropoff_location_id",
        "total_amount", "year", "month", "source_file",
        "ingestion_timestamp", "quality_status"
    }
    assert required.issubset(names)


def test_required_sql_tables_are_declared():
    sql = (ROOT / "sql/create_tables.sql").read_text(encoding="utf-8").lower()
    for table in (
        "gold_trips_clean",
        "gold_daily_revenue",
        "gold_location_performance",
        "quality_rejected_records",
        "quality_metrics_summary",
        "audit_file_inventory",
    ):
        assert f"create table if not exists {table}" in sql
