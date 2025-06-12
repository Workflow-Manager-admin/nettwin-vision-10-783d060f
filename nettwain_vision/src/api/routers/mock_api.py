from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/metadata",
    summary="Infra object metadata (mock)",
    description="Returns sample object types and config metadata.",
)
def get_obj_metadata():
    """Infra object types, fields, status enums, etc. - demo."""
    return {
        "objects": [
            {
                "type": "cell_site",
                "fields": [
                    {"name": "id", "type": "str"},
                    {"name": "name", "type": "str"},
                    {"name": "lat", "type": "float"},
                    {"name": "lng", "type": "float"},
                    {
                        "name": "status",
                        "type": "str",
                        "options": ["active", "planned"]
                    },
                ]
            },
            {
                "type": "link",
                "fields": [
                    {"name": "source", "type": "str"},
                    {"name": "target", "type": "str"},
                    {"name": "utilization_pct", "type": "int"},
                    {
                        "name": "status",
                        "type": "str",
                        "options": ["active", "degraded", "planned"]
                    },
                ]
            },
        ],
        "status_list": ["active", "planned", "degraded"]
    }


# PUBLIC_INTERFACE
@router.get(
    "/metrics",
    summary="Mock metrics API",
    description="Returns metric values for demo objects.",
)
def get_metrics():
    """Returns fake metric values for map/dashboard."""
    return {
        "metrics": [
            {"obj": "A1", "kpi": {"availability": 98.3, "utilization": 66}},
            {"obj": "A2", "kpi": {"availability": 96.9, "utilization": 87}},
            {"obj": "A3", "kpi": {"availability": None, "utilization": None}},
            {"obj": "A4", "kpi": {"availability": 97.5, "utilization": 55}},
        ]
    }


# PUBLIC_INTERFACE
@router.get(
    "/relations",
    summary="Mock link/relationship API",
    description="Returns object graph for demo.",
)
def get_relations():
    """Demo: object relationships graph."""
    return {
        "graph": [
            {"source": "A1", "target": "A2", "relation": "fiber-backhaul"},
            {"source": "A1", "target": "A3", "relation": "planned-link"},
            {"source": "A2", "target": "A4", "relation": "fiber-backhaul"},
            {"source": "A4", "target": "A3", "relation": "planned-link"},
        ]
    }
