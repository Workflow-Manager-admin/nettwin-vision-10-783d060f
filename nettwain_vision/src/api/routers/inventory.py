from fastapi import APIRouter, Query

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/",
    summary="Inventory table/list",
    description="Returns table of all digital twins and filter/search support.",
)
def inventory_table(
    status: str = Query("all", description="Status filter: all/active/planned"),
    search: str = Query(None, description="Search keyword for name or ID"),
    page: int = Query(1),
    page_size: int = Query(10),
):
    """Returns a table of digital twins and search/filter options."""
    twins = [
        {
            "id": "A1", "name": "Central Hub", "type": "cell_site",
            "status": "active", "kpis": {"availability": 98.3}
        },
        {
            "id": "A2", "name": "North Node", "type": "cell_site",
            "status": "active", "kpis": {"availability": 96.9}
        },
        {
            "id": "A3", "name": "East Node", "type": "cell_site",
            "status": "planned", "kpis": {}
        },
        {
            "id": "A4", "name": "South Node", "type": "cell_site",
            "status": "active", "kpis": {"availability": 97.5}
        },
    ]
    filtered = [
        t for t in twins if (status == "all" or t["status"] == status)
    ]
    if search:
        filtered = [
            t for t in filtered
            if search.lower() in t["name"].lower() or search.lower() in t["id"].lower()
        ]
    start = (page - 1) * page_size
    end = start + page_size
    paged = filtered[start:end]
    return {
        "twins": paged,
        "count": len(filtered),
        "page": page,
        "page_size": page_size,
        "status_opts": ["all", "active", "planned"],
    }


# PUBLIC_INTERFACE
@router.get(
    "/{twin_id}",
    summary="Digital twin detail",
    description="Returns detail for a specific digital twin instance.",
)
def twin_detail(twin_id: str):
    """Detail mock for selected digital twin."""
    details = {
        "A1": {
            "id": "A1",
            "name": "Central Hub",
            "type": "cell_site",
            "status": "active",
            "location": {"lat": 47.6101, "lng": -122.342},
            "config": {
                "vendor": "Ericsson",
                "model": "XR12",
                "capacity_Gbps": 20
            },
            "kpis": {"availability": 98.3, "utilization": 66},
        },
        "A2": {
            "id": "A2",
            "name": "North Node",
            "type": "cell_site",
            "status": "active",
            "location": {"lat": 47.6532, "lng": -122.305},
            "config": {
                "vendor": "Nokia",
                "model": "Flex5G",
                "capacity_Gbps": 12
            },
            "kpis": {"availability": 96.9, "utilization": 87},
        },
        "A3": {
            "id": "A3",
            "name": "East Node",
            "type": "cell_site",
            "status": "planned",
            "location": {"lat": 47.625, "lng": -122.276},
            "config": {
                "vendor": "Huawei",
                "model": "CloudEdge",
                "capacity_Gbps": 16
            },
            "kpis": {}
        },
        "A4": {
            "id": "A4",
            "name": "South Node",
            "type": "cell_site",
            "status": "active",
            "location": {"lat": 47.596, "lng": -122.334},
            "config": {
                "vendor": "Ericsson",
                "model": "XR10",
                "capacity_Gbps": 10
            },
            "kpis": {"availability": 97.5, "utilization": 55}
        }
    }
    return details.get(twin_id, {"error": f"No twin found with id '{twin_id}'"})
