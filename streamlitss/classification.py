import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data #so we dont have to load this data from this particular library everytime,cached
def load_data():
    iris = load_iris() #gives dataset inside iris folder
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    #converts into dataframe
    df['species'] = iris.target
    #above is the target feature
    return df, iris.target_names

df,target_names=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])#justify independent and dependent features

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

#below stores the above sliders data
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

## Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")
