from tkinter import *
from tkinter import ttk

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import ReadData as rd

def read_msg(type_,year_):
    if type_=="" and year_=="":
        return 'please enter: \ntype and year to read' , 'red'
    elif type_ =="":
        return 'please enter: \ntype to read' ,'red'
    elif year_=="":
        return 'please enter: \nyear to read','red'
    else:
        return 'Read '+type_+" "+year_ ,'green'

    

def sort_msg(type_,year_):

    if type_=="" and year_=="":
        return 'please enter: \ntype and year to sort','red'
    elif type_ =="":
        return 'please enter: \ntype to sort' ,'red'
    elif year_=="":
        return 'please enter: \nyear to sort' , 'red'
    else:
        return 'Sorted '+type_+" "+year_, 'green'
    
    

def analysis_msg(type_,year_):

    if type_=="" and year_=="":
        return 'please enter: \ntype and year to analyze','red'
    elif type_ =="":
        return 'please enter: \ntype to analyze','red'
    elif year_=="":
        return 'please enter: \nyear to analyze' , 'red'
    else:
        return 'Analyzed '+type_+" "+year_ , 'green'
    
    

def map_msg (type_,year_):
    
    if type_=="" and year_=="":
        return 'please enter: \ntype and year to map','red'
    elif type_ =="":
        return 'please enter: \ntype to map','red'
    elif year_=="":
        return 'please enter: \nyear to map','red'
    else:
        return 'Mapped '+type_+" "+year_,'green'
    
    

def read_func(type_,year_):

    #header to print to gui
    if type_== 'Traffic Volume':
        header =["year", "secname", "the_geom", "shape_leng", "volume"]
    elif type_ == 'Accidents':
        header =["incident info", "description", "start_dt", "modified_dt", "quadrant", "longitude", "latitude", "location", "count"]

    return header

def sort_func(type_,year_):
    
    #header to print to gui
    if type_== 'Traffic Volume':
        header =["year", "secname", "the_geom", "shape_leng", "volume"]
    elif type_ == 'Accidents':
        header =["incident info", "description", "start_dt", "modified_dt", "quadrant", "longitude", "latitude", "location", "count"]

    return header
        

def analysis_func(type_,year_):

    # TO be Removed and replaced with database plot, must return figure to plot
    #here
    r = rd.ReadData('2016')
    x = [2016, 2017, 2018]
    y = r.yearly_data(type_)

    fig, ax = plt.subplots()
    ax.plot(x, y, linestyle = 'dashed', marker = 'o', markerfacecolor = 'blue')

    if type_ == 'Traffic Volume':
        ax.set(xlabel='Year', ylabel='Volume',
            title='Volume vs. Year')
    else:
        ax.set(xlabel='Year', ylabel='Number of Incidents',
            title='Number of Incidents vs. Year')
    ax.set_xticks(x)

    #to here defines the figure to display

    return fig 
    


values = np.arange(0, 2500, 500)
value_increment = 1000


def map_func(type_,year_):
    pass
    