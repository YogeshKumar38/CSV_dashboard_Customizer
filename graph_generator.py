import matplotlib.pyplot as plt
import plotly.express as px

def generate_plot(df, x_col, y_col, chart_type, title):
    if chart_type == 'Line':
        fig = px.line(df, x=x_col, y=y_col, title=title)
    elif chart_type == 'Bar':
        fig = px.bar(df, x=x_col, y=y_col, title=title)
    elif chart_type == 'Scatter':
        fig = px.scatter(df, x=x_col, y=y_col, title=title)
    elif chart_type == 'Pie':
        fig = px.pie(df, names=x_col, values=y_col, title=title)
    else:
        fig = px.line(df, x=x_col, y=y_col, title=title)  # fallback
    return fig
