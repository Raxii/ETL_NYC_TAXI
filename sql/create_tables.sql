-- DDL inicial basado en las columnas del caso de estudio.
-- Revisar tipos y restricciones después de inspeccionar los Parquet reales.
-- Se ejecuta automáticamente solo al inicializar un volumen PostgreSQL nuevo.

CREATE TABLE IF NOT EXISTS audit_file_inventory (
    inventory_id BIGSERIAL PRIMARY KEY,
    process_id VARCHAR(100) NOT NULL,
    source_system TEXT,
    service_type TEXT,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size_mb NUMERIC(14,3),
    partition_year SMALLINT,
    partition_month SMALLINT CHECK (partition_month BETWEEN 1 AND 12),
    read_status TEXT NOT NULL,
    record_count BIGINT,
    column_count INTEGER,
    schema_hash TEXT,
    error_message TEXT,
    processed_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (process_id, file_path)
);

CREATE TABLE IF NOT EXISTS quality_rejected_records (
    rejected_record_id BIGSERIAL PRIMARY KEY,
    process_id VARCHAR(100) NOT NULL,
    trip_id TEXT,
    service_type TEXT,
    source_file TEXT,
    rejection_stage TEXT,
    rejection_rule TEXT,
    rejection_column TEXT,
    original_value JSONB,
    technical_reason TEXT,
    business_reason TEXT,
    rejected_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS quality_metrics_summary (
    quality_metric_id BIGSERIAL PRIMARY KEY,
    process_id VARCHAR(100) NOT NULL,
    service_type TEXT NOT NULL,
    year SMALLINT NOT NULL,
    month SMALLINT NOT NULL CHECK (month BETWEEN 1 AND 12),
    total_records BIGINT NOT NULL DEFAULT 0,
    valid_records BIGINT NOT NULL DEFAULT 0,
    rejected_records BIGINT NOT NULL DEFAULT 0,
    duplicate_records BIGINT NOT NULL DEFAULT 0,
    null_critical_records BIGINT NOT NULL DEFAULT 0,
    suspicious_records BIGINT NOT NULL DEFAULT 0,
    quality_percentage NUMERIC(7,3),
    processed_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (process_id, service_type, year, month)
);

CREATE TABLE IF NOT EXISTS gold_trips_clean (
    trip_id TEXT PRIMARY KEY,
    service_type TEXT NOT NULL,
    pickup_datetime TIMESTAMPTZ,
    dropoff_datetime TIMESTAMPTZ,
    trip_duration_minutes NUMERIC(14,4),
    trip_distance NUMERIC(14,4),
    pickup_location_id INTEGER,
    dropoff_location_id INTEGER,
    payment_type INTEGER,
    fare_amount NUMERIC(14,2),
    tip_amount NUMERIC(14,2),
    total_amount NUMERIC(14,2),
    tip_percentage NUMERIC(14,4),
    average_speed_mph NUMERIC(14,4),
    year SMALLINT,
    month SMALLINT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS gold_daily_revenue (
    gold_daily_revenue_id BIGSERIAL PRIMARY KEY,
    service_type TEXT NOT NULL,
    trip_date DATE NOT NULL,
    total_trips BIGINT NOT NULL,
    total_revenue NUMERIC(18,2),
    average_fare NUMERIC(14,2),
    average_tip NUMERIC(14,2),
    average_trip_distance NUMERIC(14,4),
    average_trip_duration NUMERIC(14,4),
    rejected_records BIGINT DEFAULT 0,
    quality_percentage NUMERIC(7,3),
    UNIQUE (service_type, trip_date)
);

CREATE TABLE IF NOT EXISTS gold_location_performance (
    gold_location_performance_id BIGSERIAL PRIMARY KEY,
    service_type TEXT NOT NULL,
    pickup_location_id INTEGER,
    dropoff_location_id INTEGER,
    total_trips BIGINT NOT NULL,
    total_revenue NUMERIC(18,2),
    average_fare NUMERIC(14,2),
    average_distance NUMERIC(14,4),
    average_duration NUMERIC(14,4),
    suspicious_trip_count BIGINT DEFAULT 0,
    UNIQUE (service_type, pickup_location_id, dropoff_location_id)
);

CREATE INDEX IF NOT EXISTS idx_gold_trips_service_datetime
    ON gold_trips_clean (service_type, pickup_datetime);

CREATE INDEX IF NOT EXISTS idx_quality_metrics_period
    ON quality_metrics_summary (year, month, service_type);

CREATE INDEX IF NOT EXISTS idx_audit_inventory_process
    ON audit_file_inventory (process_id);
