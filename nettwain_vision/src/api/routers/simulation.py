from fastapi import APIRouter, Query

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/scenarios",
    summary="List simulation scenarios",
    description="Returns available scenario types for simulation.",
)
def get_sim_scenarios():
    """Enumerate supported demo scenario types."""
    return {
        "scenarios": [
            {"id": "load_growth", "label": "Load Growth"},
            {"id": "failure", "label": "Failure Event"},
            {"id": "congestion", "label": "Congestion"},
            {"id": "expansion", "label": "Expansion"},
        ]
    }


# PUBLIC_INTERFACE
@router.get(
    "/",
    summary="Run simulation",
    description="Returns simulated result for selected scenario."
)
def run_simulation(scenario: str = Query("load_growth")):
    """Returns simulated network results for scenario."""
    if scenario == "failure":
        # Mock: north node fails, availability drops
        return {
            "alerts": [
                {
                    "type": "failure",
                    "site": "North Node",
                    "severity": "high",
                    "color": "#fbbf24"
                }
            ],
            "kpis": {
                "availability": 88.3,
                "max_utilization": 96,
                "risk_score": 7.8
            },
            "heatmap": [
                {"id": "A2", "value": 100, "color": "#ee4444"},
                {"id": "A1", "value": 68, "color": "#fbbf24"},
            ]
        }
    # Default/mock: load_growth
    return {
        "alerts": [
            {
                "type": "capacity",
                "site": "Central Hub",
                "severity": "medium",
                "color": "#fbbf24"
            }
        ],
        "kpis": {
            "availability": 94.5,
            "max_utilization": 91,
            "risk_score": 6.8
        },
        "heatmap": [
            {"id": "A1", "value": 91, "color": "#fbbf24"},
            {"id": "A3", "value": 47, "color": "#2563eb"},
            {"id": "A4", "value": 61, "color": "#2563eb"}
        ]
    }
