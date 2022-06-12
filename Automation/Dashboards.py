sudo pip3 install dash==1.6.1

!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html

# defining the layout
external_stylesheets = ['<https://codepen.io/chriddyp/pen/bWLwgP.css>']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[

	# forming a header with an HTML tag
	html.H1(children = 'A simple dashboard!'),

])

# dashboard logic

if __name__ == '__main__':
	app.run_server(debug=True)
