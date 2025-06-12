from fastapi import APIRouter, Query

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/",
    summary="Network map - sites and links",
    description="Returns network topology data for map overlays/filters.",
)
def get_network_map(layer: str = Query("all", description="Overlay layer: all/sites/links/risks")):
    """Mock map data: sites, links, risk overlays, filters."""
    return {
        "sites": [
            {
                "id": "A1", "name": "Central Hub",
                "lat": 47.6101, "lng": -122.342, "status": "active"
            },
            {
                "id": "A2", "name": "North Node",
                "lat": 47.6532, "lng": -122.305, "status": "active"
            },
            {
                "id": "A3", "name": "East Node",
                "lat": 47.625, "lng": -122.276, "status": "planned"
            },
            {
                "id": "A4", "name": "South Node",
                "lat": 47.596, "lng": -122.334, "status": "active"
            },
        ],
        "links": [
            {"source": "A1", "target": "A2", "utilization_pct": 87, "status": "degraded"},
            {"source": "A1", "target": "A3", "utilization_pct": 66, "status": "active"},
            {"source": "A2", "target": "A4", "utilization_pct": 71, "status": "active"},
            {"source": "A4", "target": "A3", "utilization_pct": 43, "status": "planned"},
        ],
        "overlays": [
            {
                "type": "risk",
                "description": "High utilization",
                "color": "#fbbf24",
                "affected_links": ["A1-A2"],
            }
        ],
        "available_layers": ["sites", "links", "risks", "planned"],
    }


# PUBLIC_INTERFACE
@router.get(
    "/filters",
    summary="Network map filters",
    description="Returns available map filters for overlays and layer controls.",
)
def map_filters():
    """Returns filter ops for the frontend map UI."""
    return {
        "filters": [
            {
                "label": "Show Active Sites",
                "value": "active",
                "type": "checkbox",
                "default": True,
            },
            {
                "label": "Show Planned Sites",
                "value": "planned",
                "type": "checkbox",
                "default": True,
            },
            {
                "label": "Show High Utilization Links",
                "value": "util_high",
                "type": "checkbox",
                "default": True,
            },
        ]
    }
