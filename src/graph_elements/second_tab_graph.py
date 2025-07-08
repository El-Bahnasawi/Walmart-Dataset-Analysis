from src.backend_code.second_tab_code import prepare_pie_charts_for_dashboard
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import src.ids as ids
from src.backend_code.data_loader import *


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(component_id=ids.PIE_CHART, component_property="figure"),
        Input(component_id=ids.PIE_CHARTS_SELECTOR, component_property='value'),
    )
    def update_chart(pie_charts_selector: str):
        return prepare_pie_charts_for_dashboard(load_data(), pie_charts_selector)

    return html.Div(
        dcc.Graph(
            id=ids.PIE_CHART,
            config={"responsive": True},
            style={"width": "100%", "height": "60vh"}
        ),
        style={"width": "100%", "height": "60vh", "padding": "10px"}
    )
