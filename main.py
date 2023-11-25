import streamlit as st 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from random import choices
def factorial(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x

def combination(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def binompmf(k,n,p):
    return combination(n,k)*(p**k)*((1-p)**(n-k))

n = st.slider('Samples',0 , 1000 , 100)
p = st.slider('Probability',0.00 , 1.00 , 0.2)
r = st.slider('Samples',0 , n , n//2)
range1 = list(range(r   ))
R = choices(range1,k = r)
dist = [binompmf(k, n, p) for k in range1]

fig = make_subplots(rows = 1 , cols = 1)

# Bar for Budget
fig.add_trace(go.Bar(
               x = range1,
               y = dist,
               name = 'Budget'         
    ),row = 1 ,col = 1)


# Set layout of the plot 
fig.update_layout(
                height = 600,
                width = 800,
                title = 'Binomial Dist',
                title_x = 0.185,
                xaxis_title = 'r',
                yaxis_title = 'dist'
    )


st.plotly_chart(fig)