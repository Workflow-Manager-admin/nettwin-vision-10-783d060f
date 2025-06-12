from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .routers import (
    dashboard,
    network_map,
    planning_wizard,
    simulation,
    inventory,
    reports,
    mock_api,
    ui_meta,
)


THEME = {
    "primary": "#2563eb",
    "secondary": "#0f172a",
    "accent": "#fbbf24",
    "scheme": "auto",
    "components": {
        "card": {
            "border_radius": "1rem",
            "shadow": "sm",
            "bg_light": "#fff",
            "bg_dark": "#172033",
        },
        "sidebar": {"bg_light": "#f8fafc", "bg_dark": "#0f172a"},
        "header": {"bg_light": "#fff", "bg_dark": "#18181b"},
        "text_light": "#111827",
        "text_dark": "#f4f4f5",
    },
}


app = FastAPI(
    title="NetTwin Vision-10 Backend",
    description=(
        "Demo backend for Network Digital Twin Platform (NetTwin Vision-10). "
        "FastAPI + Modular API endpoints for card-based UI demos."
    ),
    version="0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "filter": True,
        "displayRequestDuration": True,
        "docExpansion": "none",
    },
    openapi_tags=[
        {"name": "Dashboard", "description": "KPIs, widgets, and high-level network overview"},
        {"name": "Map", "description": "Network infrastructure, overlays, filters"},
        {"name": "Planning Wizard", "description": "Site/upgrade planning, before/after data"},
        {"name": "Simulation", "description": "Scenario simulation, results, alerts"},
        {"name": "Inventory", "description": "Digital twin table/list, config, search"},
        {"name": "Reports", "description": "Charts, planning, CSV/PDF export"},
        {"name": "Mock API", "description": "Mocked endpoints for frontend/demo"},
        {"name": "UI Meta", "description": "Theme, color, component meta and docs for UI"},
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="src/api/static"), name="static")

templates = Jinja2Templates(directory="src/api/templates")

app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["Dashboard"])
app.include_router(network_map.router, prefix="/api/v1/map", tags=["Map"])
app.include_router(planning_wizard.router, prefix="/api/v1/planning", tags=["Planning Wizard"])
app.include_router(simulation.router, prefix="/api/v1/simulation", tags=["Simulation"])
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["Inventory"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(mock_api.router, prefix="/api/v1/mock", tags=["Mock API"])
app.include_router(ui_meta.router, prefix="/api/v1/ui", tags=["UI Meta"])


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def root_landing(request: Request):
    """Minimal landing route, demo-only."""
    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "theme": THEME,
            "app_name": "NetTwin Vision-10",
        }
    )


@app.get("/healthz", response_model=dict)
def health_check():
    return {"healthy": True}


@app.exception_handler(404)
def not_found_demo(request, exc):
    if str(request.url).endswith(".ico"):
        return JSONResponse(status_code=204, content={})
    return JSONResponse(
        status_code=404,
        content={
            "error": "This endpoint does not exist. See /docs for available demo APIs."
        }
    )
