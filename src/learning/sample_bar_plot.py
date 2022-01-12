import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


def main():
    print('executing main')
    app = dash.Dash(__name__)

    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    # sample data frame to display something \O/
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    app.run_server(debug=True)
    print('finished')


if __name__ == '__main__':
    main()
