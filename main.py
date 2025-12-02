import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import plotly
import plotly.express as px

data=pd.read_csv("/Users/Tanishq/Desktop/Datascience/Lesson13/gaming_console_dataset.csv")

top_7=pd.DataFrame(data.groupby("Country")["Sales"].mean().nlargest(7).sort_values(ascending=False))
print(top_7)
print(top_7.index)


fig1=px.scatter(top_7,x=top_7.index,y="Sales",size="Sales",size_max=230,color=top_7.index,title="Top 7 Countries by sales")
fig1.write_html("Fig1.html",auto_open=True)

top_7a=pd.DataFrame(data.groupby("Country")["Profit"].mean().nlargest(7).sort_values(ascending=False))
print(top_7a)
print(top_7a.index)

fig2=px.scatter(top_7a,x=top_7a.index,y="Profit",size="Profit",size_max=230,color=top_7.index,title="Top 7 Countries by profit")
fig2.write_html("Fig2.html",auto_open=True)

top_7b=pd.DataFrame(data.groupby("Country")["Date"].mean().nlargest(7).sort_values(ascending=False))
print(top_7b)
print(top_7b.index)

fig3=px.scatter(top_7b,x=top_7b.index,y="Date",size="Date",size_max=230,color=top_7.index,title="Top 7 Countries by date")
fig3.write_html("Fig3.html",auto_open=True)