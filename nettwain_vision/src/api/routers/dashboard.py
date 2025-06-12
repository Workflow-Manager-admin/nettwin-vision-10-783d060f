from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/",
    summary="Dashboard overview cards & KPIs",
    description="Returns summary widgets, KPIs, quick actions for dashboard landing.",
)
def get_dashboard_overview():
    """Mock dashboard top-level cards and KPIs."""
    return {
        "cards": [
            {
                "title": "Active Sites",
                "icon": "tower-broadcast",
                "value": 42,
                "trend": "+3.5%",
                "color": "primary",
                "description": "Total live sites in network",
            },
            {
                "title": "Planned Upgrades",
                "icon": "arrow-up-right-dots",
                "value": 7,
                "trend": "-12%",
                "color": "accent",
                "description": "Planned upgrades in queue",
            },
            {
                "title": "Site Alerts",
                "icon": "bell-warning",
                "value": 2,
                "trend": "",
                "color": "secondary",
                "description": "Active alerts flagged by simulations",
            },
            {
                "title": "Network Health",
                "icon": "activity-heartbeat",
                "value": 98.3,
                "unit": "%",
                "trend": "+0.8%",
                "color": "primary",
                "description": "Overall health (availability, SLAs, latency)",
            },
        ],
        "theme": {
            "primary": "#2563eb",
            "accent": "#fbbf24",
            "secondary": "#0f172a",
        },
        "actions": [
            {"label": "New Plan", "to": "/planning/wizard", "type": "primary"},
            {"label": "Inventory", "to": "/inventory", "type": "secondary"},
        ],
    }


# PUBLIC_INTERFACE
@router.get(
    "/trend",
    summary="Dashboard KPI trends",
    description="Returns network KPIs time-series for widgets.",
)
def get_kpi_trends():
    """Mock time-series for dashboard KPI charts (trend sparklines, etc)."""
    return {
        "kpi_trends": [
            {
                "metric": "availability",
                "label": "Availability %",
                "times": [
                    "2024-06-15",
                    "2024-06-16",
                    "2024-06-17",
                    "2024-06-18",
                ],
                "values": [97.2, 97.7, 98.3, 98.3],
            },
            {
                "metric": "site_alerts",
                "label": "Active Alerts",
                "times": [
                    "2024-06-15",
                    "2024-06-16",
                    "2024-06-17",
                    "2024-06-18",
                ],
                "values": [2, 3, 2, 2],
            },
        ]
    }
