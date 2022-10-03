import plotly.express as plotly


plot = plotly.pie(labels=["A1", "A2", "A3"], values=[1, 2, 3])
plot.show()