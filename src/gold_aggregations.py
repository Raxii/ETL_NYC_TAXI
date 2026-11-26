"""Agregaciones Gold compartidas.

Santi: gold_daily_revenue.
Byron: gold_location_performance.
Matius: gold_trips_clean (en transformations.py).
"""


def build_gold_daily_revenue(valid_trips_df, rejected_df):
    """Agrupar por service_type y fecha; calcular métricas del caso."""
    raise NotImplementedError("Santi: implementar gold_daily_revenue.")


def build_gold_location_performance(valid_trips_df):
    """Agrupar por servicio, zona de recogida y zona de destino."""
    raise NotImplementedError("Byron: implementar gold_location_performance.")
