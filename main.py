import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
import statsmodels.formula.api as smf
from bokeh.plotting import figure
from bokeh.io import push_notebook,show,output_notebook
from ipywidgets import interact
# MOST OF THIS FILE IS BEING PORTED TO getfilenames.py and table_generator.py

import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import push_notebook,show,output_notebook
from ipywidgets import interact


protein_name_table = pd.read_csv("protein_names.csv")
disorder_stats = pd.read_csv("tmp.csv")
proteintable_bydisorder =disorder_stats.sort("pct_disord", ascending=False)
y = proteintable_bydisorder.pct_disord
x = proteintable_bydisorder.tot_aa
bokeh_plot = figure(plot_width=1024, plot_height=576)
r = bokeh_plot.scatter(x, y, color="#2222aa")

def updatey(f):
    if f == "Percent Disorder": func = proteintable_bydisorder.pct_disord
    elif f == "Number of Disorderd Segments" : func = proteintable_bydisorder.seg_disord
    elif f == "30 Residues Disordered" : func = proteintable_bydisorder.thirty_disord
    elif f == "50 Residues Disordered" : func = proteintable_bydisorder.fifty_disord
    elif f == "Total Amino Acids" : func = proteintable_bydisorder.tot_aa
    r.data_source.data["y"] = func    
def updatex(f):
    if f == "Percent Disorder": funcx = proteintable_bydisorder.pct_disord
    elif f == "Number of Disorderd Segments" : funcx = proteintable_bydisorder.seg_disord
    elif f == "30 Residues Disordered" : funcx = proteintable_bydisorder.thirty_disord
    elif f == "50 Residues Disordered" : funcx = proteintable_bydisorder.fifty_disord
    elif f == "Total Amino Acids" : funcx = proteintable_bydisorder.tot_aa
    r.data_source.data["x"] = funcx
    push_notebook()

show(bokeh_plot, notebook_handle=True)