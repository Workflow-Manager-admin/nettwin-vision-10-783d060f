from fastapi import APIRouter, Query

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/start",
    summary="Start new planning flow",
    description="Initiate a new site or upgrade plan. Returns wizard steps and config.",
)
def planning_wizard_start():
    """Returns wizard config/steps for demo planning flow."""
    return {
        "wizard_id": "demo-pw-001",
        "steps": [
            {"step": 1, "label": "Select Site/Upgrade Type"},
            {"step": 2, "label": "Configure Site Parameters"},
            {"step": 3, "label": "Review Before/After Impact"},
            {"step": 4, "label": "Approve and Save"},
        ],
        "types": ["greenfield-site", "capacity-upgrade", "failover-addition"],
        "default_values": {
            "site_type": "capacity-upgrade",
            "target_node": "A2"
        }
    }


# PUBLIC_INTERFACE
@router.get(
    "/impact",
    summary="Planning before/after impact view",
    description="Returns simulated before/after network state for planning scenario.",
)
def planning_impact(wizard_id: str = Query(None), type: str = Query(None)):
    """Returns before/after data for demo scenario."""
    return {
        "before": {
            "site": "North Node",
            "kpis": {
                "availability": 96.9,
                "max_utilization": 87,
                "risk_score": 6.5
            },
            "alerts": ["High utilization on A1-A2"]
        },
        "after": {
            "site": "North Node",
            "kpis": {
                "availability": 98.2,
                "max_utilization": 66,
                "risk_score": 2.7
            },
            "alerts": []
        },
        "wizard_id": wizard_id
    }


# PUBLIC_INTERFACE
@router.post(
    "/finalize",
    summary="Approve and save plan",
    description="Finalize and 'save' a demo plan (mock).",
)
def planning_finalize():
    """Pretend to approve/save a site/upgrade plan in demo workflow."""
    return {"status": "success", "msg": "Plan saved", "plan_id": "plan-442"}
