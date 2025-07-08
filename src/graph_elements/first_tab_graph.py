# Import necessary modules
from src.backend_code.first_tab_code import select_and_prepare_dashboard_barcharts
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import src.ids as ids
from src.backend_code.data_loader import load_data

# Define the render function
def render(app: Dash) -> html.Div:
    # Define the callback to update the chart and control visibility of dropdown and H5 element
    @app.callback(
        Output(component_id=ids.BAR_CHART, component_property="figure"),
        Output(component_id=ids.SELECTOR_DROPDOWN, component_property='style'),
        Output(component_id=ids.FIRST_TAB_H5, component_property='style'),
        Input(component_id=ids.IDENTIFIER_RADIO_ITEMS, component_property='value'),
        Input(component_id=ids.SELECTOR_DROPDOWN, component_property='value')
    )
    def update_chart(identifier: str, select_type: str):
        # Update the chart based on user inputs
        figure = select_and_prepare_dashboard_barcharts(load_data(), identifier, select_type)
        
        # Set default styles for dropdown and H5 element
        dropdown_style = {'width': '180px', 'background-color': '#343a40', 'color': '#1E88E5', 'display': 'block'}
        h5_style = {"color": '#FFAA00', 'display': 'block'}

        # Conditionally hide dropdown and H5 element based on identifier
        if identifier in ["Dept Sales: Holiday vs Non-Holiday", "Top 5 Departments", "Bottom 5 Departments"]:
            dropdown_style['display'] = 'none'
            h5_style['display'] = 'none'

        # Return updated chart and styles
        return figure, dropdown_style, h5_style
    
    # Return the dcc.Graph component
    return dcc.Graph(
        id=ids.BAR_CHART,
        config={"responsive": True},
    )