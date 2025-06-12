from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/theme",
    summary="UI Theme colors & layout meta",
    description="Returns supported theme/colors and layout for demo UI.",
)
def get_theme_data():
    """Theme meta for frontend: colors, dark/light, sample cards/typography."""
    return {
        "theme": {
            "primary": "#2563eb",
            "secondary": "#0f172a",
            "accent": "#fbbf24",
            "auto_scheme": True,
            "components": {
                "card": {
                    "radius": "1rem",
                    "shadow": "sm",
                    "bg_light": "#fff",
                    "bg_dark": "#172033",
                },
                "sidebar": {
                    "bg_light": "#f8fafc",
                    "bg_dark": "#0f172a"
                },
                "header": {
                    "bg_light": "#fff",
                    "bg_dark": "#18181b"
                },
                "text_light": "#111827",
                "text_dark": "#f4f4f5",
            },
        },
        "layout": {
            "sidebar": True,
            "cards": True,
            "widgets": True,
            "responsive": True,
            "toasts_modals": True,
            "support_light_dark": True,
        },
        "demo": {
            "ui_patterns": [
                "card", "sidebar-nav", "chart-widget", "modal", "table"
            ]
        }
    }


# PUBLIC_INTERFACE
@router.get(
    "/components",
    summary="UI Components API",
    description="Returns information about modular UI components/cards for demo apps.",
)
def get_ui_components():
    """Describe available modular UI cards/components for demo/proof-of-concept."""
    return {
        "components": [
            {
                "name": "DashboardKpiCard",
                "desc": "KPI number + trend + icon, primary color, optional chart mini-sparkline."
            },
            {
                "name": "MapCard",
                "desc": "Map visual with overlays, legend, filter controls, click for details."
            },
            {
                "name": "SidebarNav",
                "desc": "Sidebar nav with theming and icons, collapsible for mobile."
            },
            {
                "name": "PlanningWizard",
                "desc": "Stepper/wizard for multi-step planning workflows, actions at each step."
            },
            {
                "name": "TwinTable",
                "desc": "Table/list view of all digital twins, sortable/filterable, quick actions."
            },
            {
                "name": "Chart",
                "desc": "Responsive charts (bar, pie, line) for trends, using preset data or API."
            },
            {
                "name": "Toast",
                "desc": "In-app notification popper, theme-aware (light/dark, accent/primary)."
            },
            {
                "name": "Modal",
                "desc": "Modal overlay dialog for confirm/detail, theme and cards aware."
            },
        ]
    }
