from fastapi import APIRouter, Query

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/",
    summary="Available reports for planning",
    description="Returns available report types (mock).",
)
def list_reports():
    """List report types/available exports."""
    return {
        "reports": [
            {"id": "site_plan", "label": "Site Planning Report"},
            {"id": "utilization", "label": "Utilization Summary"},
            {"id": "risk", "label": "Risk & Alerts Report"},
        ]
    }


# PUBLIC_INTERFACE
@router.get(
    "/summary",
    summary="Summary report data",
    description="Returns planning summary with chart/table mock data.",
)
def summary_report():
    """Planning report summary with chart/table (for demo)."""
    return {
        "charts": [
            {
                "type": "bar",
                "title": "Planned Upgrades per Quarter",
                "labels": ["Q1", "Q2", "Q3", "Q4"],
                "values": [2, 1, 3, 1]
            },
            {
                "type": "pie",
                "title": "Alerts by Type",
                "labels": ["Capacity", "Failure"],
                "values": [3, 1]
            }
        ],
        "table": [
            {"site": "Central Hub", "status": "Active",
             "planned": 1, "alerts": 0},
            {"site": "North Node", "status": "Active",
             "planned": 2, "alerts": 1},
            {"site": "East Node", "status": "Planned",
             "planned": 1, "alerts": 1},
        ]
    }


# PUBLIC_INTERFACE
@router.get(
    "/export",
    summary="Report export API (CSV/PDF mock)",
    description="Demo-mock: Export report to CSV/PDF (returns file link(s)).",
)
def export_report(format: str = Query("CSV", description="CSV | PDF")):
    """Return mock download url for report file."""
    link = (
        "/static/mock_site_report.csv"
        if format.lower() == "csv"
        else "/static/mock_site_report.pdf"
    )
    return {"format": format.upper(), "url": link}
