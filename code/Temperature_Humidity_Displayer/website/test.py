import plotly.tools as tls

tls.set_credentials_file(
        username="waleed-bs",
        api_key="bdeNJOC2IQfL6oB6CppV")

# to get your credentials
credentials = tls.get_credentials_file()


import csv
import plotly.plotly as py

#----------------------------------------------------------------------
def plot_counties(csv_path):
    """
    http://census.ire.org/data/bulkdata.html
    """
    counties = {}
    county = []
    pop = []

    counter = 0
    with open(csv_path) as csv_handler:
        reader = csv.reader(csv_handler)
        for row in reader:
            print row
            if counter  == 0:
                counter += 1
                continue
            county.append(row[0])
            pop.append(row[2])

    trace = dict(x=county, y=pop)
    data = [trace]
    py.plot(data, filename='temperature vs time')

if __name__ == '__main__':
    csv_path = 'temp&humdLog.csv'
    plot_counties(csv_path)
# import pandas as pd
# import numpy as np
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# df = read_csv('temp&humdLog.csv')
# df.head()
#
# trace1 = go.Scatter(
#                     x=df['x'], y=df['logx'], # Data
#                     mode='lines', name='logx' # Additional options
#                    )
# trace2 = go.Scatter(x=df['x'], y=df['sinx'], mode='lines', name='sinx' )
# trace3 = go.Scatter(x=df['x'], y=df['cosx'], mode='lines', name='cosx')
#
# layout = go.Layout(title='Simple Plot from csv data',
#                    plot_bgcolor='rgb(230, 230,230)')
#
# fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
#
# # Plot data in the notebook
# py.iplot(fig, filename='simple-plot-from-csv')
