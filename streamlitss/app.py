import streamlit as st
import pandas as pd
import numpy as np


#Title of the application 
st.title("Hello streamlit") #debug mode like in flask is always seems to be on

###display a simple text 
st.write("this is a simple text")

#create a simple dataframe

df = pd.DataFrame({
    'first column':[1,2,3,4,5],
    'Second column':[20,30,40,45,50]
})

#Display the dataframe
st.write("Here is the dataframe")
st.write(df)



#create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns = ['a','b','c']
)
st.line_chart(chart_data)

