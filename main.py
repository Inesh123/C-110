import pandas as pd
import csv 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
df = pd.read_csv('newdata.csv')
data=df['average'].tolist()
def randomsetofmeans(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)    
    return mean
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig = ff.create_distplot([df],['average'],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name = 'mean'))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print('mean of sampling distribution: ',mean)
setup()
populationmean = statistics.mean(data)
print('mean of population: ',mean)
def standard_Deviation():
    mean_list=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        mean_list.append(setofmeans)
    standard_deviation=statistics.stdev(mean_list)
    print('standard deviation of sample distribution: ',standard_deviation)
standard_Deviation()